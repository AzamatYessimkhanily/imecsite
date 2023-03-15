from urllib import request
from flask import render_template, session, abort, redirect, request, url_for, send_from_directory, flash
from sqlalchemy.event import listens_for
import os.path as op
import smtplib
from email.mime.text import MIMEText
from werkzeug.security import generate_password_hash, check_password_hash
from myclass import User,Post,Certificates
from app import app, db
from flask_ckeditor import upload_fail, upload_success
import os


file_path = op.join(op.dirname(__file__), 'static/files')

@app.route("/forward/<string:user>/<string:phone>", methods=['GET', 'POST'])
def smail(user, phone):
    sender = "salomat423@gmail.com"
    password = "221502Ernur@"
    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls()

    message = user + " " + phone

    try:
        server.login(sender, password)
        msg = MIMEText(message, _charset='utf-16')
        msg["Subject"] = "Innovation Medical Engineering Center"
        server.sendmail(sender, sender, msg.as_string())

        return redirect("/")
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"

@app.route('/')
def index():
    session['logged_in'] = False
    session.clear()
    return render_template('index1.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        login = request.form['login']
        password = generate_password_hash(request.form['password'])

        # Create a new user record in the database        
        user = User(name=name, email=email, login=login, password=password)
        db.session.add(user)
        db.session.commit()

        flash('Registration successful!')
        return redirect(url_for('index'))

    return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(login=login).first()

        if user and check_password_hash(user.password, password) and user.is_admin:
            session['logged_in'] = True            
            return redirect("/admin")
        else:
            return render_template("login.html", failed=True)

    return render_template("login.html")
@app.route('/logout')
def logout():
    session['logged_in'] = False
    session.clear()
    return redirect('/login')


@app.route('/news/<string:lol>')
def newsstr():
    return redirect('/news/1')


@app.route('/news')
def news():
    return redirect('/news/1')


@app.route('/news/<int:page_num>')
def news_articles(page_num):
    news_articles = Post.query.order_by(Post.id.desc()).paginate(page=page_num, per_page=4, error_out=True)
    return render_template("news.html", news_articles=news_articles)


@app.route('/cert')
def cert():
    cert = Certificates.query.order_by(Certificates.id.desc())
    return render_template("cert_page.html", cert=cert)


@app.route('/news_page/<int:num>')
def news_page(num):
    if num:
        news_articles = Post.query.filter_by(id=num)
        return render_template('news_page.html', news_articles=news_articles)
    else:
        return abort(403)


@app.route('/files/<filename>')
def uploaded_files(filename, target):
    f = request.files.get('upload')
    path = app.config['UPLOADED_PATH']
    print(app.config['UPLOADED_PATH'] + '/' + filename)
    flash(f(app.config['UPLOADED_PATH'] + '/' + filename), 'success')
    return send_from_directory(path, target.id)


@app.route('/upload', methods=['POST'])
def upload(target):
    f = request.files.get('upload')
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    flash(f(app.config['UPLOADED_PATH'] + '/' + f.filename), 'success')
    f.save(os.path.join(app.config['UPLOADED_PATH'], target.id))
    url = url_for('uploaded_files', filename=target.id)
    return upload_success(url=url)
@listens_for(Post, 'after_delete')
def del_image(target):
    if target.path:
        try:
            print(target.id)
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass


@listens_for(Certificates, 'after_delete')
def del_image(target):
    if target.path:
        try:
            print(target.id)
            os.remove(op.join(cert, target.path))
        except OSError:
            pass