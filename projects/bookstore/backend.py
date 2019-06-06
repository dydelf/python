"""
Backend connecting to the database sqlite3 for the bookstore app.
"""

import sqlite3


class Database():


    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, author TEXT, isbn INTEGER)")
        self.connection.commit()

    def view_all(self):
        self.cursor.execute("SELECT * FROM bookstore")
        rows = self.cursor.fetchall()
        return rows

    def search_entry(self, title="", year="", author="", isbn=""):
        self.cursor.execute("SELECT * FROM bookstore WHERE title=? OR year=? OR author=? OR isbn=?", (title, year, author, isbn))
        rows = self.cursor.fetchall()
        return rows

    def add_entry(self, title, year, author, isbn):
        self.cursor.execute("INSERT INTO bookstore VALUES (NULL, ?, ?, ?, ?)", (title, year, author, isbn))
        self.connection.commit()

    def update(self, id, title, year, author, isbn):
        self.cursor.execute("UPDATE bookstore SET title=?, year=?, author=?, isbn=? WHERE id=?", (title, year, author, isbn, id))
        self.connection.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM bookstore WHERE id=?", (id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
