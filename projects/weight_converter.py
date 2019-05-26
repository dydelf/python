"""
Convert weight to grams, pounds and ounces easily.
"""

from tkinter import *


def kg_to_other():
    """ Convert weight to other units. """
    t1.delete(1.0, END)
    t2.delete(1.0, END)
    t3.delete(1.0, END)
    try:
        kg = float(weight.get())
        grams = 1000*kg
        pounds = 2.20462*kg
        ounces = 35.274*kg
        t1.insert(END, grams)
        t2.insert(END, pounds)
        t3.insert(END, ounces)
    except ValueError:
        t1.insert(END, "Please provide a number!")
    
window = Tk()
window.title("Weight Converter")

l4 = Label(window, text="kg", justify=CENTER)
l4.grid(row=0, column=1)

weight = StringVar()
e1 = Entry(window, textvariable=weight)
e1.grid(row=0, column=2)

b1 = Button(window, text="Convert", command=kg_to_other)
b1.grid(row=0, column=3)

t1 = Text(window, height=1, width=30)
t1.grid(row=1, column=2)
l1 = Label(window, text="grams", justify=CENTER)
l1.grid(row=1, column=1)

t2 = Text(window, height=1, width=30)
t2.grid(row=2, column=2)
l2 = Label(window, text="pounds", justify=CENTER)
l2.grid(row=2, column=1)

t3 = Text(window, height=1, width=30)
t3.grid(row=3, column=2)
l3 = Label(window, text="ounces", justify=CENTER)
l3.grid(row=3, column=1)

window.mainloop()
