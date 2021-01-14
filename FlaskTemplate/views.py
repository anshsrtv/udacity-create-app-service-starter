from flask import render_template, request
from FlaskTemplate import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    
    try:
        name = request.args['name']
    except:
        name = "</>"

    return render_template(
        'index.html',
        # Display the name on the website.
        name = name
    )

