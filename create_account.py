from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A list to store the clubs (each club will be a dictionary with a name and a list of members)
clubs = []

# Load existing clubs from a .txt file
def load_clubs():
    global clubs
    try:
        with open('club_data.txt', 'r') as file:
            clubs = [{'name': line.strip(), 'members': []} for line in file if line.strip()]
    except FileNotFoundError:
        clubs = []

# Save clubs to a .txt file
def save_clubs():
    with open('club_data.txt', 'w') as file:
        for club in clubs:
            file.write(club['name'] + '\n')

# Home route
@app.route('/')
def home():
    load_clubs()  # Load the saved clubs
    return render_template('index.html', clubs=clubs)

# Create a club route
@app.route('/create_club', methods=['POST'])
def create_club():
    club_name = request.form.get('club-name')
    if club_name:
        clubs.append({'name': club_name, 'members': []})
        save_clubs()  # Save the updated list of clubs
        return redirect(url_for('president_interface'))

    return redirect(url_for('home'))

# Join a club route
@app.route('/join_club', methods=['POST'])
def join_club():
    club_name = request.form.get('join-club')
    if club_name:
        for club in clubs:
            if club['name'] == club_name:
                # For now, simply adding a generic member to the club
                club['members'].append('New Member')
                save_clubs()  # Save the updated club data
                break
    return redirect(url_for('home'))

# President Interface route
@app.route('/president_interface')
def president_interface():
    load_clubs()  # Ensure clubs are loaded
    return render_template('interface.html')

if __name__ == '__main__':
    app.run(debug=True)
