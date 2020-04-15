from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fdced14f698bc27173c0444f560ffe2de7b16c10a1ada6e280afd252ba4aa8c4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#-models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    profile_pic = db.Column(db.String(20), nullable=False, default='def.jpg')
    password = db.Column(db.String(60), nullable=False)
    #one to many rel users -> posts
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.profile_pic}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    #rel to users
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"

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
            flash('Invalid Login. Please try again.', category='danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)