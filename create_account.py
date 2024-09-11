from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

clubs = []  # You can replace this with file/database storage

@app.route('/')
def home():
    return render_template('index.html', clubs=clubs)

@app.route('/create_club', methods=['POST'])
def create_club():
    club_name = request.form.get('club_name')
    if club_name:
        clubs.append(club_name)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
