from flask import render_template, url_for, flash, redirect
from flaskapp import app, db, bcrypt
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User, Post
from flask_login import login_user

#-dummy data
posts = [ 
    {
        'author': 'Kyle Reece',
        'title': 'Post 1',
        'content': 'first post content',
        'date_posted': 'March 24, 2020'
    },
    {
        'author': 'Not Kyle',
        'title': 'Post 2',
        'content': 'second post content',
        'date_posted': 'March 25, 2020'
    }
]


#-routes
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created. You can now log in!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Incorrect email or password. Try again.', category='danger')
    return render_template('login.html', title='Login', form=form)

#@app.route("/account")
#@login_required
#def account():
#   return "nice!"