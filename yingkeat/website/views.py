from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Club
from . import db\



views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("reviews.html") #This should be the homepage.