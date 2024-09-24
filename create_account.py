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
    message = ''
    
    if club_name:
        user = User.query.first()  # Assuming the first user
        club = Club.query.filter_by(name=club_name).first()
        if club and user:
            # If you want to add user membership logic, do it here
            message = f"You have successfully joined the club '{club_name}'!"

    clubs = Club.query.all()  # Get all clubs to display
    return render_template('index.html', clubs=clubs, message=message)

# President Interface route
@app.route('/president_interface')
def president_interface():
    clubs = Club.query.all()  # Get all clubs for the interface
    return render_template('interface.html', clubs=clubs)

# User clubs route
@app.route('/user_clubs')
def user_clubs():
    user = User.query.first()  # For simplicity, assuming the first user
    # Since there's no club_members table, we won't have user clubs
    user_clubs = []  # No clubs to display
    return render_template('user_clubs.html', user_clubs=user_clubs)

if __name__ == '__main__':
    app.run(debug=True)
