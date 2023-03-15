from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_mail import Mail
from flask_babel import Babel
from flask import Flask
from admin import init_admin
from config import Config

app = Flask(__name__)
babel=Babel(app)
app.config.from_object(Config)
mail = Mail(app)  # instantiate the mail class
ckeditor = CKEditor(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = init_admin(app, db)

from routes import *

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
