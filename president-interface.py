from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Set the folder where uploaded files will be saved
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('interface.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return redirect(request.url)

    image = request.files['image']
    if image.filename == '':
        return redirect(request.url)

    if image:
        # Save the image to the upload folder
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
        
        # Get other form data like caption, date, and location
        caption = request.form['caption']
        date = request.form['date']
        location = request.form['location']
        
        # You can save the data to a database or perform other actions
        return redirect(url_for('home'))

@app.route('/members')
def members():
    return "List of members will go here"

@app.route('/events')
def events():
    return "Event details will go here"

if __name__ == '__main__':
    app.run(debug=True)
