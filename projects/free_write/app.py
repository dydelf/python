"""
Main file of the Free Writing App.

In this application people can free write in a textbox and retrieve their
texts later from the database.

Functionalities:
- registered users
- logs of all free writes
- logs answering to the important questions
- analyzing the texts added (how many words, what phrases most used)

More functionalities will be added.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
