from datetime import datetime
from flask import session, abort
from flask_sqlalchemy import SQLAlchemy
from flask_admin import form
from flask_admin.contrib.sqla import ModelView
import os.path as op
from flask_ckeditor import CKEditorField
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
file_path = op.join(op.dirname(__file__), 'static/files')
cert_path = op.join(op.dirname(__file__), 'static/cert')

class ImageView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)
    form_overrides = dict(content=CKEditorField)
    create_template = 'edit.html'
    edit_template = 'edit.html'
    form_extra_fields = {
        'path': form.ImageUploadField('Image',
                                      base_path=file_path) }
    
    
class CertView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)
    form_overrides = dict(content=CKEditorField)
    create_template = 'cert.html'
    edit_template = 'cert.html'
    form_extra_fields = {
        'path': form.ImageUploadField('Image',
                                      base_path=cert_path)}
    

class UserView(ModelView):
    column_list = ('name', 'email', 'login' ,'password','is_admin')
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)
    create_template = 'user_view.html'
    edit_template = 'user_view.html'



class User(db.Model):
    __tablename__ = 'username'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    login = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(1000))
    is_admin = db.Column(db.Boolean, default=False)



class Post(db.Model):
    __tablename__ = "post1"
    id = db.Column(db.Integer, primary_key=True)
    title_en = db.Column(db.String(), unique=False, nullable=False)
    title_ru = db.Column(db.String(), unique=False, nullable=False)
    title_kz = db.Column(db.String(), unique=False, nullable=False)
    en = db.Column(db.Text(), nullable=False)
    ru = db.Column(db.Text(), nullable=False)
    kz = db.Column(db.Text(), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    path = db.Column(db.Unicode(128), nullable=False)


class Certificates(db.Model):
    __tablename__ = "cert"
    id = db.Column(db.Integer, primary_key=True)
    title_en = db.Column(db.String(), unique=False, nullable=False)
    title_ru = db.Column(db.String(), unique=False, nullable=False)
    title_kz = db.Column(db.String(), unique=False, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    path = db.Column(db.Unicode(128), nullable=False)


