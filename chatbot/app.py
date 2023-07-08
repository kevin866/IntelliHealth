from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle the form submission
        selected_option = request.form['option']
        # Do something with the selected option
        
    # Render the HTML template
    return render_template('index.html')

