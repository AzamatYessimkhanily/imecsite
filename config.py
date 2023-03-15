import os

class Config:
    FLASK_APP = 'app.py'
    FLASK_ENV = 'development'
    SECRET_KEY = 'anykey'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CKEDITOR_FILE_UPLOADER = 'upload'
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = 587
    MAIL_USERNAME = 'yessimkhanuly@gmail.com'
    MAIL_PASSWORD = '18032004aZa@'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    FLASK_ADMIN_SWATCH = 'flatly'  # lumen cyborg flatly
    SQLALCHEMY_DATABASE_URI = "postgresql://userimec:Pin.1234@172.16.1.13:5432/pyapp1"
    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_PKG_TYPE = 'full'
    CKEDITOR_SERVE_LOCAL = True
    CKEDITOR_HEIGHT = 400
    CKEDITOR_WIDTH = 600
    CKEDITOR_FILE_BROWSER = 'true'
