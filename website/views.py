from flask import Blueprint, render_template, request, flash,url_for,redirect
from flask_login import login_required, current_user
from .models import Club,Review
from . import db
from django.shortcuts import render, get_object_or_404
from .models import Club, Review



views = Blueprint('views',__name__)

@views.route('/')
def mainpage():
    return render_template("mainpage.html")


