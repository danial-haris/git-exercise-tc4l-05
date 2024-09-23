from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A list to keep the clubs 
clubs = []


def load_clubs():
    global clubs
    try:
        with open('club_data.txt', 'r') as file:
            clubs = [{'name': line.strip(), 'members': []} for line in file if line.strip()]
    except FileNotFoundError:
        clubs = []

# Save clubs to .txt file
def save_clubs():
    with open('club_data.txt', 'w') as file:
        for club in clubs:
            file.write(club['name'] + '\n')

# Home route
@app.route('/')
def home():
    load_clubs()  # Load saved clubs
    return render_template('index.html', clubs=clubs)

# Create a club route
@app.route('/create_club', methods=['POST'])
def create_club():
    club_name = request.form.get('club-name')
    if club_name:
        clubs.append({'name': club_name, 'members': []})
        save_clubs()  # Save updated list of clubs
        return redirect(url_for('president_interface'))

    return redirect(url_for('home'))

# Join a club route
@app.route('/join_club', methods=['POST'])
def join_club():
    club_name = request.form.get('join-club')
    if club_name:
        for club in clubs:
            if club['name'] == club_name:
                
                club['members'].append('New Member')
                save_clubs()  # Save updated club data
                break
    return redirect(url_for('home'))

# President Interface route
@app.route('/president_interface')
def president_interface():
    load_clubs() 
    return render_template('interface.html')

if __name__ == '__main__':
    app.run(debug=True)
