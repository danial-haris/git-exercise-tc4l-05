from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Club
from . import db


views = Blueprint('views',__name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        club = request.form.get('club')

        if len(club) < 1:
            flash('Club name is too short!', category='error') 
        else:
            new_club = Club(data=club, user_id=current_user.id)  
            db.session.add(new_club) 
            db.session.commit()
            flash('Club created!', category='success')

    return render_template("home.html", user=current_user)