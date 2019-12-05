"""
Файл с формами.
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField


class SendMessage(FlaskForm):
    """
    Форма для кнопки.
    """
    input_str = StringField("Введите IP адрес")
    submit = SubmitField("Отправить")
