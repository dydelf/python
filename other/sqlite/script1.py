"""
Test of the sqlite3 database.
"""

import sqlite3


def create_table():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store ")
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete(item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item=?", (item,))
    connection.commit()
    connection.close()

def update(quantity, price, item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?",
            (quantity, price, item))
    connection.commit()
    connection.close()

#insert("Coffee Break", 10, 30)
#insert("Test", 1, 1)
update(2, 2, "Test")
#delete("Coffee Cup")
#delete("Coffee Break")
print(view())