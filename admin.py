from flask_admin import Admin
from flask_admin.base import MenuLink
from myclass import ImageView, CertView, UserView, User, Post, Certificates

def init_admin(app, db):
    admin = Admin(app, template_mode='bootstrap4')
    admin.add_view(ImageView(Post, db.session, name='News'))
    admin.add_view(CertView(Certificates, db.session, name='Certificates'))
    admin.add_view(UserView(User, db.session, name='User'))
    admin.add_link(MenuLink(name='Main page', endpoint='index'))
    admin.add_link(MenuLink(name='Logout', endpoint='logout'))
    return admin
