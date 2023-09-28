from flask import Blueprint, render_template, url_for, redirect
from flask_login import logout_user, login_required

pictapp = Blueprint(
    'pictapp',
    __name__,
    template_folder='templates_pict',
    static_folder='static_pict',
)


from flask import render_template
from flask_login import login_required 
from sqlalchemy import select 
from flask import request 
from flask_paginate import Pagination, get_page_parameter


@pictapp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    stmt = select(
        modelpict.UserPicture).order_by(modelpict.UserPicture.create_at.desc())
    entries = db.session.execute(stmt).scalars().all()
    page = request.args.get(
        get_page_parameter(), type=int, default=1)
    res = entries[(page - 1)*6: page*6]
    pagination = Pagination(
        page=page,          
        total=len(entries), 
        per_page=6)        
    return render_template('top.html', user_picts=res, pagination=pagination)


from flask import send_from_directory 

@pictapp.route('/images/<path:filename>')
def image_file(filename):
    return send_from_directory(
        current_app.config['UPLOAD_FOLDER'], filename)



import uuid 
from pathlib import Path 
from flask_login import current_user 
from flask import current_app 

from apps.app import db 
from apps.pictapp import forms 
from apps.pictapp import models as modelpict 

@pictapp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = forms.UploadImageForm()

    if form.validate_on_submit():
        file = form.image.data
        suffix = Path(file.filename).suffix
        imagefile_uuid = str(uuid.uuid4()) + suffix
        image_path = Path(
            current_app.config['UPLOAD_FOLDER'], imagefile_uuid)
        file.save(image_path)

        upload_data = modelpict.UserPicture(
            user_id=current_user.id,
            username = current_user.username,
            title=form.title.data,
            contents=form.message.data,
            image_path=imagefile_uuid
        )

        db.session.add(upload_data)
        db.session.commit()
        return redirect(url_for('pictapp.index'))
    
    return render_template('upload.html', form=form)