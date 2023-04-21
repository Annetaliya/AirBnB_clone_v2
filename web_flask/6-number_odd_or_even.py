#!/usr/bin/python3
''' a script that starts a Flask web application'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''function that displays hello hbnb'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display():
    '''A function that returns HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text_diplay(text):
    '''displays “C ” followed by the value of the text variable'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_py(text='is cool'):
    '''display “Python ”, followed by the value of the text'''
    return 'Python {}' .format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_nu(n):
    '''display “n is a number” only if n is an integer'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_nu(n):
    '''display a HTML page only if n is an integer '''
    return render_template('5-number.html', index_num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    '''display a HTML page only if n is an integer'''
    if n % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'

    return render_template('6-number_odd_or_even.html', n=n, num=odd_or_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
