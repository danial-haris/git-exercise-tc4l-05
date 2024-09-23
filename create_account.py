from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Define Club model
class Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    members = db.relationship('User', secondary='club_members')

# Association table between Clubs and Users
club_members = db.Table('club_members',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('club_id', db.Integer, db.ForeignKey('club.id'))
)

# Create the database and tables
with app.app_context():
    db.create_all()

# Home route
@app.route('/')
@app.route('/home')
def home():
    clubs = Club.query.all()  # Get all clubs
    return render_template('index.html', clubs=clubs)

# Create a club route
@app.route('/create_club', methods=['POST'])
def create_club():
    club_name = request.form.get('club-name')
    if club_name:
        new_club = Club(name=club_name)
        db.session.add(new_club)
        db.session.commit()  # Save new club to the database
        return redirect(url_for('president_interface'))

    return redirect(url_for('home'))

# Join a club route
@app.route('/join_club', methods=['POST'])
def join_club():
    club_name = request.form.get('join-club')
    username = request.form.get('username')  # Username of the member joining
    email = request.form.get('email')
    if club_name and username and email:
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username, email=email)
            db.session.add(user)
            db.session.commit()
        club = Club.query.filter_by(name=club_name).first()
        if club:
            club.members.append(user)
            db.session.commit()  # Update club with new member
    return redirect(url_for('home'))

# President Interface route
@app.route('/president_interface')
def president_interface():
    clubs = Club.query.all()  # Get all clubs for the interface
    return render_template('interface.html', clubs=clubs)

if __name__ == '__main__':
    app.run(debug=True)
