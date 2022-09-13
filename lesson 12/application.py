from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect

import utils

from webargs import fields
from webargs.flaskparser import use_kwargs


app = Flask(__name__)


# home page
@app.route('/')
def index():
    return render_template('index.html')


# page to show all rates
@app.route('/all_rates')
def show_all_rates():
    data = utils.get_data()
    return render_template('show_all.html', data=data)


# search page
@app.route('/search')
def search_by_currency():
    return render_template('search.html')


# search data by the given currency
@app.route('/rates')
@use_kwargs({'currency': fields.Str(required=True)}, location='query')
def find_data(currency):
    found_data = utils.find_data(currency)

    if not found_data:
        return redirect('/search')

    return render_template('exchange_rate.html', data=found_data)


if __name__ == '__main__':
    app.run(debug=True, port=5050)
