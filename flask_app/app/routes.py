"""
Файл навигации по приложению.
"""
from flask import render_template
from app import app
from app.forms import SendMessage
from ip_validator.ip_validator import Validate


@app.route('/', methods=['POST', 'GET'])
def index():
    """
    Отображение единственной странички на сайте.
    """
    form = SendMessage()
    if form.validate_on_submit():
        text = form.input_str.data
        val = Validate()
        result = val.validateIPAddress([text])
        return render_template('index.html', form=form, result=result)
    return render_template('index.html', form=form)
