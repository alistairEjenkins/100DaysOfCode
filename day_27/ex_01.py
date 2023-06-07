from tkinter import *


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)


def button_clicked():
    my_label["text"] = my_entry.get()

# labels
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "new text"
#my_label.pack()
# my_label.place(x=200, y=150)
my_label.grid(row=0, column=0)

# buttons
my_button = Button(text="Click me", command=button_clicked)
#my_button.pack()
my_button.grid(row=1, column=1)

my_button2 = Button(text="new button")
#my_button.pack()
my_button2.grid(row=0, column=2)

# Entry
my_entry =Entry(width=30)
#my_entry.pack()
my_entry.grid(row=2, column=3)





window.mainloop()










































































































































































































































































































