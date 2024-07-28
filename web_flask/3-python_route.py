#!/usr/bin/python3
"""
Task 3. Python is cool!
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Root endpoint
    Return: Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    hbnb endpoint
    Return: HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Return: “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Return: “Python ”, followed by the value of the text variable
        (replace underscore _ symbols with a space )
    The default value of text is “is cool”
    """
    return "Python " + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
