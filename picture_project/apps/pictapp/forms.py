from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadImageForm(FlaskForm):
    title = StringField(
        "タイトル",
        validators=[DataRequired(message="入力が必要です。"),
                    length(max=200, message="200文字以内で入力してください。"),]
    )

    message = TextAreaField(
        "メッセージ",
        validators=[DataRequired(message="入力が必要です。"),])

    image = FileField(
        validators=[
        FileRequired("画像ファイルを選択してください。"),
        FileAllowed(['png', 'jpg', 'jpeg'],
                    'サポートされていないファイル形式です。'),]
    )
    
    submit = SubmitField('投稿する')
