from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Get the base directory (Sorfina folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    # Serve index.html from the Sorfina folder
    return send_from_directory(BASE_DIR, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
