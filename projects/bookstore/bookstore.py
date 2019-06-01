"""
Bookstore application for desktop usage.
Stores details about the books in a database:
Title, Author
Year, ISBN

Funcionalities:
    view all records
    search an entry
    add entry
    update entry
    delete
"""

from tkinter import *
import backend


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        view_command()
        #list1.insert(END, "Please view the elemens first")
        #pass

def view_command():
    list1.delete(0, END)
    for row in backend.view_all():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search_entry(title_entry.get(), year_entry.get(), author_entry.get(), isbn_entry.get()):
        list1.insert(END, row)

def add_command():
    backend.add_entry(title_entry.get(), year_entry.get(), author_entry.get(), isbn_entry.get())
    list1.delete(0, END)
    list1.insert(END, (title_entry.get(), year_entry.get(), author_entry.get(), isbn_entry.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title_entry.get(), year_entry.get(), author_entry.get(), isbn_entry.get())

def clear_command():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


window = Tk()
window.title("Bookstore Database")

#Collection of labels
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Year")
l2.grid(row=1, column=0)

l3 = Label(window, text="Author")
l3.grid(row=0, column=2)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

#Collection of entry textboxes
title_entry = StringVar()
e1 = Entry(window, textvariable=title_entry)
e1.grid(row=0, column=1)

year_entry = StringVar()
e2 = Entry(window, textvariable=year_entry)
e2.grid(row=1, column=1)

author_entry = StringVar()
e3 = Entry(window, textvariable=author_entry)
e3.grid(row=0, column=3)

isbn_entry = StringVar()
e4 = Entry(window, textvariable=isbn_entry)
e4.grid(row=1, column=3)

#Collection of buttons
b1 = Button(window, text="View all / Refresh", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

b7 = Button(window, text="Clear", width=10, command=clear_command)
b7.grid(row=2, column=2)

#Scrollbar
s1 = Scrollbar(window)
s1.grid(row=3, column=2, rowspan=5)

#Textbox
list1 = Listbox(window, height = 8, width = 30, yscrollcommand=s1.set)
list1.grid(row=2, rowspan=6, column=0, columnspan=2)
list1.bind('<<ListboxSelect>>', get_selected_row)

s1.config(command=list1.yview)

window.mainloop()
