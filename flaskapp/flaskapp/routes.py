from flask import render_template, url_for, flash, redirect
from flaskapp import app
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User, Post

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
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@nrvlive.com' and form.password.data == 'password':
            flash('You have been logged in!', category='success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect email or password. Try again.', category='danger')
    return render_template('login.html', title='Login', form=form)