from flask import render_template

from . import market

@market.route('/', methods=['GET'])
def index():
    return render_template('market/index.html')
