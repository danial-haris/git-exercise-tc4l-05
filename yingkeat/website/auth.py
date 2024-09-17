from flask import Blueprint,render_template,request,flash,redirect,url_for,Flask
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash (user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))#homepage
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html",user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists!',category='error')
        elif len(email) < 10:
            flash('Please use your MMU account.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif len(first_name) < 5:
                flash('Please use your full name.', category='error')
                
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1,method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)
            flash('Account created!',category='success')
            return redirect(url_for('views.home'))#homepage


    return render_template("sign_up.html",user=current_user)

@auth.route('/main')
def mainpage():
    return render_template("mainpage.html")

reviews = []

@auth.route('/', methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        rating = request.form['rating']
        comment = request.form['comment']
        
        review = {
            'rating': rating,
            'comment': comment
        }
        reviews.append(review)

        return redirect(url_for('auth.review'))

    return render_template('review_club.html', reviews=reviews)

# clubs = [
#     {'name': 'Photography Club', 'role': 'Member', 'join_date': '9 September 2024'},
#     {'name': 'Book Lovers Club', 'role': 'Admin', 'join_date': '9 September 2024'}
# ]

# @auth.route('/member')
# def member():
#     return render_template('member.html', clubs=clubs)









