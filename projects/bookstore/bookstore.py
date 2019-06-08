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
from backend import Database


database = Database("database.db")

class Window(object):
    """Creating a window object for tkinter module."""

    def __init__(self, window):
        self.window = window
        self.window.title("Bookstore Database")

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
        self.title_entry = StringVar()
        self.e1 = Entry(window, textvariable=self.title_entry)
        self.e1.grid(row=0, column=1)

        self.year_entry = StringVar()
        self.e2 = Entry(window, textvariable=self.year_entry)
        self.e2.grid(row=1, column=1)

        self.author_entry = StringVar()
        self.e3 = Entry(window, textvariable=self.author_entry)
        self.e3.grid(row=0, column=3)

        self.isbn_entry = StringVar()
        self.e4 = Entry(window, textvariable=self.isbn_entry)
        self.e4.grid(row=1, column=3)

        #Collection of buttons
        b1 = Button(window, text="View all / Refresh", width=12,
                command=self.view_command)
        b1.grid(row=2, column=3)

        b2 = Button(window, text="Search entry", width=12,
                command=self.search_command)
        b2.grid(row=3, column=3)

        b3 = Button(window, text="Add entry", width=12,
                command=self.add_command)
        b3.grid(row=4, column=3)

        b4 = Button(window, text="Update", width=12,
                command=self.update_command)
        b4.grid(row=5, column=3)

        b5 = Button(window, text="Delete", width=12,
                command=self.delete_command)
        b5.grid(row=6, column=3)

        b6 = Button(window, text="Close", width=12, command=window.destroy)
        b6.grid(row=7, column=3)

        b7 = Button(window, text="Clear", width=10,
                command=self.clear_command)
        b7.grid(row=2, column=2)

        #Scrollbar
        s1 = Scrollbar(window)
        s1.grid(row=3, column=2, rowspan=5)

        #Textbox
        self.list1 = Listbox(window, height = 8, width = 30,
                yscrollcommand=s1.set)
        self.list1.grid(row=2, rowspan=6, column=0, columnspan=2)
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        s1.config(command=self.list1.yview)

    def get_selected_row(self, event):
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, self.selected_tuple[4])
        except IndexError:
            #Window.view_command()
            #self.list1.insert(END, "Please view the elemens first")
            pass

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view_all():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search_entry(self.title_entry.get(),
                self.year_entry.get(), self.author_entry.get(),
                self.isbn_entry.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.add_entry(self.title_entry.get(), self.year_entry.get(),
                self.author_entry.get(), self.isbn_entry.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_entry.get(), self.year_entry.get(),
            self.author_entry.get(), self.isbn_entry.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        database.update(self.selected_tuple[0], self.title_entry.get(),
                self.year_entry.get(), self.author_entry.get(),
                self.isbn_entry.get())

    def clear_command(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)


window = Tk()
Window(window)
window.mainloop()
