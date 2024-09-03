from flask import Flask, render_template

App = Flask(__name__)

@App.route('/')
@App.route('/home')
def home():
    return render_template('home.html')

@App.route('/admin')
def admin():
    return render_template('admin.html')

@App.route('/user')
def user():
    return render_template('user.html')

@App.route('/clubs')
def clubs():
    return render_template('clubs.html')

if __name__ == '__main__' :
    App.run(debug=True)
    