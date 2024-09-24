from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    reset_token = db.Column(db.String(150), nullable=True)
    reset_token_expiration = db.Column(db.DateTime, nullable=True)
    security_question = db.Column(db.String(255))
    security_answer = db.Column(db.String(255))  
    # role = db.Column(db.String(50), nullable=False)  # Define the role column
    # participated_events = db.Column(db.PickleType, default=[])  # Define participated events



# class Club(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     data = db.Column(db.String(100))
#     data = db.Column(db.DateTime(timezone=True),default=func.now())
#     user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
class Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'Member' or 'Admin'
    join_date = db.Column(db.String(50), nullable=False)  # Storing as string for simplicity

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    club = db.relationship('Club', backref=db.backref('events', lazy=True))

# class Event(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     date = db.Column(db.String(50), nullable=False)
#     description = db.Column(db.Text, nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign key to User model
    user = db.relationship('User', backref='reviews')  # Relationship to access User info



