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
from functools import wraps

from data import articles


app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'pyxis'
app.config['MYSQL_PASSWORD'] = 'pyxispyxis'
app.config['MYSQL_DB'] = 'freewrite'
# Cursor returns a dictionary from a query
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


# User registration

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


# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                # Close connection
                cur.close()

                return redirect(url_for('dashboard'))
            else:
                error = "Invalid password"
                app.logger.info('PASSWORD NOT MATCHED')
                return render_template('login.html', error=error)

        else:
            error = "Username not found"
            app.logger.info('USER NOT FOUND')
            return render_template('login.html', error=error)

    return render_template('login.html')


# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, please log in!', 'danger')
            return redirect(url_for('login'))
    return wrap


# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


@app.route('/dashboard')
@is_logged_in
def dashboard():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    result = cur.execute("SELECT * FROM logs")

    logs = cur.fetchall()

    if result > 0:
        return render_template('dashboard.html', logs=logs)
    else:
        msg = 'No articles found'
        return render_template('dashboard.html', msg=msg)


class LogForm(Form):
    title = StringField('Title', [validators.Length(min=0, max=200)])
    body = TextAreaField('Body', [validators.Length(min=30)])
    tags = StringField('Tags', [validators.Length(min=0, max=255)])

# Add log
@app.route('/add_log', methods=['GET', 'POST'])
@is_logged_in
def add_log():
    form = LogForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data
        tags = form.tags.data

        # Create cursor
        cur = mysql.connection.cursor()

        # Get the name of the user
        # ERROR!!!!!!!!!!!!!
        author = session['username']
        name = cur.execute("SELECT name FROM users WHERE username = %s", (author,))

        # Execute
        cur.execute("INSERT INTO logs(username, title, author, body, tags) VALUES(%s, %s, %s, %s, %s)", (session['username'], title, name, body, tags))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Log created', 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_log.html', form=form)


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
