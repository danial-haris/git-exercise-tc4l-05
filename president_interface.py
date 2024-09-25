from flask import Flask, render_template, request, redirect, url_for 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Club model
class Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

# Event model
class Event(db.Model):
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
    return render_template('interface.html')

# Members route
@app.route('/members', methods=['GET', 'POST'])
def members():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('members'))
    
    members = User.query.all()
    return render_template('members.html', members=members)

# Events route
@app.route('/events', methods=['GET', 'POST'])
def events():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_event = Event(name=name, description=description)
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('events'))
    
    events = Event.query.all()
    return render_template('event.html', events=events)

# Delete a member
@app.route('/members/delete/<int:id>', methods=['POST'])
def delete_member(id):
    member_to_delete = User.query.get_or_404(id)
    db.session.delete(member_to_delete)
    db.session.commit()
    return redirect(url_for('members'))

# Make a member an admin (newly added route)
@app.route('/make_admin/<int:id>', methods=['POST'])
def make_admin(id):
    # Here, you would implement the logic to promote a member to admin.
    # For demonstration purposes, we'll just redirect back to members.
    return redirect(url_for('members'))

# Delete an event
@app.route('/events/delete/<int:id>', methods=['POST'])
def delete_event(id):
    event_to_delete = Event.query.get_or_404(id)
    db.session.delete(event_to_delete)
    db.session.commit()
    return redirect(url_for('events'))

if __name__ == '__main__':
    app.run(debug=True)
