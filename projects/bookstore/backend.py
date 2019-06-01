"""
Backend connecting to the database sqlite3 for the bookstore app.
"""

import sqlite3


def connect():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, author TEXT, isbn INTEGER)")
    connection.commit()
    connection.close()

def view_all():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM bookstore")
    rows = cursor.fetchall()
    connection.close()
    return rows

def search_entry(title="", year="", author="", isbn=""):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM bookstore WHERE title=? OR year=? OR author=? OR isbn=?", (title, year, author, isbn))
    rows = cursor.fetchall()
    connection.close()
    return rows

def add_entry(title, year, author, isbn):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO bookstore VALUES (NULL, ?, ?, ?, ?)", (title, year, author, isbn))
    connection.commit()
    connection.close()

def update(id, title, year, author, isbn):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE bookstore SET title=?, year=?, author=?, isbn=? WHERE id=?", (title, year, author, isbn, id))
    connection.commit()
    connection.close()

def delete(id):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM bookstore WHERE id=?", (id,))
    connection.commit()
    connection.close()


connect()
