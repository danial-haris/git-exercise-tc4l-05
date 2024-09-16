from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

App = Flask(__name__)

# configure sqlite database
App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///management.db'
App.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(App)

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
with App.app_context():
    db.create_all()

#home route
@App.route('/')
@App.route('/home')
def home():
    return render_template('home.html')

#admin route
@App.route('/admin')
def admin():
    return render_template('admin.html')

#user management route
@App.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('user'))
    
    # retrieve all users from the database
    users = User.query.all()
    return render_template('user.html', users=users)
# Delete a user
@App.route('/user/delete/<int:id>', methods=['POST'])
def delete_user(id):
    user_to_delete = User.query.get_or_404(id)
    db.session.delete(user_to_delete)
    db.session.commit()
    return redirect(url_for('user'))

#club management route
@App.route('/clubs', methods=['GET','POST'])
def clubs():
    if request.method == 'POST' :
        #add new club
        name = request.form['name']
        description = request.form['description']
        new_club = Club(name=name, description=description)
        db.session.add(new_club)
        db.session.commit()
        return redirect(url_for('clubs'))
    
    # retrieve all clubs from the database
    clubs = Club.query.all()
    return render_template('clubs.html', clubs=clubs)

# Delete a club
@App.route('/clubs/delete/<int:id>', methods=['POST'])
def delete_club(id):
    club_to_delete = Club.query.get_or_404(id)
    db.session.delete(club_to_delete)
    db.session.commit()
    return redirect(url_for('clubs'))

if __name__ == '__main__':
    App.run(debug=True)