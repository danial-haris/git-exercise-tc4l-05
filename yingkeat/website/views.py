from flask import Blueprint, render_template, request, flash,url_for,redirect
from flask_login import login_required, current_user
from .models import Club,Review
from . import db
from django.shortcuts import render, get_object_or_404
from .models import Club, Review



views = Blueprint('views',__name__)

@views.route('/')
def mainpage():
    return render_template("mainpage.html") #This should be the homepage.

reviews = []

@views.route('/review', methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        rating = request.form['rating']
        comment = request.form['comment']
        
        new_review = Review(rating=rating, comment=comment)
        
        db.session.add(new_review)
        db.session.commit()
        
        return redirect(url_for('views.review'))

    reviews = Review.query.all()
    return render_template('review.html', reviews=reviews)
