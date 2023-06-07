# GUI Password Generator

from random import choice, shuffle, randint
from tkinter import *
from tkinter import messagebox
import json
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# --------------- PASSWORD GENERATOR --------------------------------- #
def choose_characters(character_set, num_required):
    return [choice(character_set) for _ in range(num_required)]

def generate_password():

    nr_letters = randint(8, 10)
    nr_numbers = randint(2, 4)
    nr_symbols = randint(2, 4)
    password = choose_characters(letters, nr_letters) \
                   + choose_characters(numbers, nr_numbers)\
               + choose_characters(symbols, nr_symbols)
    shuffle(password)
    password = ''.join(password)

    password_entry.insert(0,password)
    pyperclip.copy(password)

# --------------- SAVE LOGIN DETAILS --------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }


    entries = [website, email, password]
    for entry in entries:
        if not entry:
            messagebox.showerror("Oops!", "Need a website address; email and password!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                #saving updates data
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #saving updates data
                json.dump(new_data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            messagebox.showinfo(message="Login details stored")

# ----------------- SEARCH ------------------------------------------ #
def search():

    website = website_entry.get()
    if len(website) == 0:
        messagebox.showerror(title="Oops!", message="No website entered!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            for site in data:
                if site == website:
                    email = data[website]['email']
                    password = data[website]['password']
                    break
            else:
                print("not found")
                raise KeyError
        except FileNotFoundError:
            messagebox.showerror(title="Oops!", message="No passwords stored yet!")
        except KeyError:
            messagebox.showerror(title="Oops!", message="No matching website found!")
        else:
            messagebox.showinfo(title=f"{website}", message=f"Password:"
                                                            f" {password}\nEmail/User: {email}")

# --------------- CREATE UI ------------------------------------------ #
window = Tk()
window.title("Password Helper")
window.config(padx=20, pady=20)

canvas =Canvas(width=200, height=190)
logo = PhotoImage(file="images/logo.png")
canvas.create_image(100,95, image=logo)
canvas.grid(row=0, column=1)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/User:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)
email_entry = Entry(width=60)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "alistairedwardjenkins.gmail.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)
generate_button= Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()