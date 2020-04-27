from flask import render_template, request, url_for, Blueprint
from flask_login import login_required
from flaskapp.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    #Query param
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/event_calendar")
@login_required
def event_calendar():
    return render_template('events.html', title='Calendar')

@main.route("/locations")
def locations():
    loc_imgs = [url_for('static', filename='loc_images/' + 'img1.jpg'),
                url_for('static', filename='loc_images/' + 'img2.jpg'),
                url_for('static', filename='loc_images/' + 'img3.jpg'),
                url_for('static', filename='loc_images/' + 'img4.jpg'),
                url_for('static', filename='loc_images/' + 'img5.jpg') ]
    return render_template('locations.html', title='Locations', loc_imgs=loc_imgs)