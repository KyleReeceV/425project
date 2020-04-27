from flask import render_template, request, url_for, Blueprint
from flask_login import login_required
from flaskapp.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    home_imgs = [url_for('static',filename='home_images/' + 'h_img1.png'),
                url_for('static', filename='home_images/' + 'h_img2.png'),
                url_for('static', filename='home_images/' + 'h_img3.png'),
                url_for('static', filename='home_images/' + 'h_img4.png') ]
    return render_template('home.html', home_imgs=home_imgs)

@main.route("/blog")
def blog():
    #Query param
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', posts=posts)

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

@main.route("/contact")
def contact():
    return render_template('contact.html', title="Contact Us!")