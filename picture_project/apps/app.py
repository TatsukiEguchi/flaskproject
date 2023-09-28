from flask import Flask, render_template, url_for, redirect, flash
from apps import forms, models
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('settings.py')

db = SQLAlchemy()
db.init_app(app)

Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = 'index'
login_manager.login_message = ''
login_manager.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.SignupForm()
    if form.validate_on_submit():
        user = models.User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        if user.is_duplicate_email():
            flash('登録済みのメールアドレスです')
            return redirect(url_for('index'))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('index.html', form=form)


from apps.authapp.views import authapp
app.register_blueprint(authapp, url_prefix='/auth')

from apps.pictapp.views import pictapp
app.register_blueprint(pictapp, url_prefix='/picture')
