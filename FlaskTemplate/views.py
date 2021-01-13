from flask import render_template
from FlaskTemplate import app

# TODO: Replace YOUR_NAME with your name e.g. Grace 
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        name = "<YOUR_NAME>"
    )

