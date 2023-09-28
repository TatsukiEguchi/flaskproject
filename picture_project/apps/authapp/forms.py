from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField(
        'メールアドレス',
        validators=[DataRequired(message='入力が必要です'), Email(message='メールアドレスの形式で入力してください')]
    )
    password = PasswordField(
        'パスワード',
        validators=[DataRequired(message='入力が必要です')]
    )
    submit = SubmitField('ログイン')