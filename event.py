from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/president-interface')
def president_interface():
    return render_template('president-interface.html')

@app.route('/create_event')
def create_event():
    return render_template('event.html')

@app.route('/submit_event', methods=['POST'])
def submit_event():
    event_name = request.form['eventName']
    event_date = request.form['eventDate']
    event_time = request.form['eventTime']
    event_location = request.form['eventLocation']
    event_description = request.form['eventDescription']
    
    # Process the event information (e.g., save to a database)

    return "Event created successfully!"

if __name__ == '__main__':
    app.run(debug=True)
