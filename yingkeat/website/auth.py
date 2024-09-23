from flask import Blueprint,render_template,request,flash,redirect,url_for,Flask
from .models import User,Club,Event
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
                # return redirect(url_for('member.html'))#homepage
                return render_template("member.html")
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









