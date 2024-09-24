from flask import Blueprint,render_template,request,flash,redirect,url_for,flash,jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message
import os
import secrets
from datetime import datetime, timedelta
from .models import User,Club,Event,Review
from sqlalchemy import func


auth = Blueprint('auth',__name__)

# @auth.route('/login',methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')

#         user = User.query.filter_by(email=email).first()
#         if user:
#             if check_password_hash (user.password, password):
#                 flash('Logged in successfully!', category='success')
#                 login_user(user, remember=True)
#                 # return redirect(url_for('member.html'))#homepage
#                 return render_template("review.html")
#             else:
#                 flash('Incorrect password, try again.', category='error')
#         else:
#             flash('Email does not exist.', category='error')

#     return render_template("login.html",user=current_user)
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Debug: print email and password (remove in production)
        print(f"Received email: {email}")
        print(f"Received password: {password}")

        # Basic validation
        if not email or not password:
            flash('Please fill out both fields.', category='error')
            return render_template("login.html")

        user = User.query.filter(func.lower(User.email) == email.lower()).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                # return redirect(url_for('auth.member'))  # Redirect after login
                return render_template("member.html")
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html")


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
            return redirect(url_for('views.review'))#homepage


    return render_template("sign_up.html",user=current_user)

@auth.route('/myclubs')
def my_clubs():
    clubs = Club.query.all()
    return render_template('my_clubs.html', clubs=clubs)

@auth.route('/club/<int:club_id>')
def club_details(club_id):
    club = Club.query.get_or_404(club_id)
    events = Event.query.filter_by(club_id=club.id).all()
    return render_template('club_details.html', club=club, events=events)

# Email Configuration
mail = Mail()

@auth.route('/reset-password-request', methods=['GET', 'POST'])
def reset_password_request():
    if request.method == 'POST':
        email = request.form.get('email').strip().lower()
        user = User.query.filter(db.func.lower(User.email) == email).first()

        if user is None:
            flash('User not found', 'error')
            return redirect(url_for('auth.login'))

        # Generate reset token
        user.reset_token = secrets.token_urlsafe(16)
        user.reset_token_expiration = datetime.now() + timedelta(hours=1)
        db.session.commit()

        reset_url = url_for('auth.reset_password', token=user.reset_token, _external=True)
        msg = Message("Password Reset Request", recipients=[user.email])
        msg.body = f"""To reset your password, visit the following link:
{reset_url}

If you did not make this request, simply ignore this email and no changes will be made.
"""
        try:
            mail.send(msg)
        except Exception as e:
            flash('Error sending email, please try again.', 'error')
            return redirect(url_for('auth.login'))

        flash('Password reset email sent!', 'success')
        return redirect(url_for('auth.login'))

    return render_template('reset_password_request.html')

@auth.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    # Filter by reset token and check if the token has not expired
    user = User.query.filter(User.reset_token == token, User.reset_token_expiration > datetime.now()).first()

    if request.method == 'POST':
        new_password = request.form.get('password')
        if user:  # Make sure the user is found before updating
            user.password = generate_password_hash(new_password)
            user.reset_token = None  # Invalidate the token after use
            user.reset_token_expiration = None
            db.session.commit()

            flash('Your password has been reset!', 'success')
            return redirect(url_for('auth.login'))

    if user is None:
        flash('Token is invalid or has expired', 'error')
        return redirect(url_for('auth.login'))

    return render_template('reset_password.html', token=token)

@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        # Check if current password matches
        if not check_password_hash(current_user.password, current_password):
            flash('Incorrect current password', 'error')
            return redirect(url_for('auth.change_password'))

        # Check if new passwords match
        if new_password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('auth.change_password'))

        # Update password
        current_user.password = generate_password_hash(new_password)
        db.session.commit()

        flash('Your password has been changed!', 'success')
        return redirect(url_for('auth.change_password'))

    return render_template('change_password.html')

@auth.route('/reset-password-question', methods=['GET', 'POST'])
def reset_password_question():
    if request.method == 'POST':
        email = request.form.get('email').strip().lower()
        security_answer = request.form.get('security_answer')

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.security_answer, security_answer):
            return redirect(url_for('auth.reset_password_form', email=user.email))

        flash('Incorrect answer to the security question', 'error')
        return redirect(url_for('auth.reset_password_question'))

    return render_template('reset_password_question.html')


reviews = []
@auth.route('/review', methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        rating = request.form['rating']
        comment = request.form['comment']
        
        new_review = Review(rating=rating, comment=comment)
        
        db.session.add(new_review)
        db.session.commit()
        
        return redirect(url_for('auth.review'))

    reviews = Review.query.all()
    return render_template('review.html', reviews=reviews)

@auth.route('/club/<int:club_id>')
def club_profile(club_id):
    # Fetch club information
    club = get_club_info(club_id)
    
    # If club data is found, pass it to the template, else display error
    if club:
        club_name, club_description = club
        return render_template('club_profile.html', club_name=club_name, club_description=club_description)
    else:
        return "Club not found", 404











