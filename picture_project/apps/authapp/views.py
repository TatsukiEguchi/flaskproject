from flask import Blueprint, url_for, flash, redirect, render_template
from flask_login import login_user
from sqlalchemy import select
from apps.authapp import forms
from apps import models
from apps.app import db

authapp = Blueprint(
    'authapp',
    __name__,
    template_folder='templates_auth',
    static_folder='static_auth',
)


@authapp.route('/', methods=['GET', 'POST'])
def index():
    form = forms.LoginForm()
    if form.validate_on_submit():
        stmt = (
            select(models.User).filter_by(email=form.email.data).limit(1)
        )
        user = db.session.execute(stmt).scalars().first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('pictapp.index'))
        flash('認証に失敗しました')
    return render_template('login.html', form=form)
