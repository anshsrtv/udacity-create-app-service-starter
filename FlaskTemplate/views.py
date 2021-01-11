from flask import render_template
from FlaskTemplate import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        name = "Ansh Srivastava"
    )

