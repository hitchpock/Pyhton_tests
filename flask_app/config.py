import os


class Config(object):
    """
    Ключ для генерации подписей и токенов.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
