from tkinter import *

window = Tk()
window.title("Miles to TK Converter")
window.minsize(width=300, height=200)

def miles_to_km():
    answer_label["text"] = 1.609 * int(miles_entry.get())

miles_entry = Entry(width=50)
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equals_label = Label(text="is equal to")
equals_label.grid(row=1, column=1)

answer_label = Label(text="0")
answer_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(row=2, column=1)

window.mainloop()

