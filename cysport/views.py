from flask import current_app as app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/a-line')
def a_line():
    return render_template('a-line.html')
