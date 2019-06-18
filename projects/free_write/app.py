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

from flask import (Flask, render_template, flash, redirect, url_for, session,
                   logging, request)
from flask_mysqldb import MySQL
from wtforms import (Form, StringField, TextAreaField, PasswordField,
                     validators)
from passlib.hash import sha256_crypt

from data import articles


app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'pyxis'
app.config['MYSQL_PASSWORD'] = 'pyxispyxis'
app.config['MYSQL_DB'] = 'freewrite'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MySQL
mysql = MySQL(app)

articles = articles()


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/logs')
def logs():
    return render_template('logs.html', articles=articles)


@app.route('/log/<string:id>/')
def log(id):
    return render_template('log.html', id=id)


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match'),
    ])
    confirm = PasswordField('Confirm Password')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query

        cur.execute("INSERT INTO users(name, username, email, password) VALUES(%s, %s, %s, %s)", (name, username, email, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can log in.', 'success')

        return redirect(url_for('index'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
