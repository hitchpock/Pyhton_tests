from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField


class SendMessage(FlaskForm):
    input_str = StringField("Введите IP адрес")
    submit = SubmitField("Отправить")
