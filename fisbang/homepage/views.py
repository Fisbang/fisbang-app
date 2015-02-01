from flask import render_template

from . import homepage

@homepage.route('/', methods=['GET'])
def index():
    return render_template('homepage/index.html')
