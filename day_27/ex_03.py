from tkinter import *

window = Tk()
window.title("test")

def update_label():

    my_label.config(text = my_entry.get())

my_label = Label(text="starting text")
my_label.pack()

my_button = Button(text="Click me", command=update_label)
my_button.pack()

my_entry = Entry(width=10)
my_entry.pack()

window.mainloop()