from tkinter import *
import pandas as p
import glob
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #

FONT_NAME = "Courier"
EMAIL = "test@test.com"


# ---------------------------- Search Function ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='You need to add a password first before searching!')
    else:
        if website in data:
            username = data[website]['username']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Username: {username}\nPassword: {password}')
        else:
            messagebox.showinfo(title=website, message=f'No details for {website} exists')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # List comprehensions
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(letters) for _ in range(randint(2, 4))]
    password_numbers = [choice(letters) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_entry.delete(0, END)
    password_entry.insert(END, string=password)

    # pyperclip will save the password in the OS clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = str(website_entry.get())
    username = str(username_entry.get())
    password = str(password_entry.get())
    new_data = {
        website: {
            'username': username,
            'password': password
        }
    }  # new_data creates a dictionary for JSON

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title='Error', message='There is no value in the entry')
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                # Saving updated data
                data = json.load(data_file)
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

        # Alternative writing using Pandas to push to csv
        credential_dict = {"Website": [website], "Username": [username], "Password": [password]}
        dict_to_csv = p.DataFrame(credential_dict).to_csv('data.csv', mode='a', index=False, header=False)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, highlightthickness=0, borderwidth=0)

canvas = Canvas(width=200, height=200)
myPass_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=myPass_img)
canvas.grid(column=1, row=0)

# ``````````````````````````````Labels ```````````````````````````````````` #

website_label = Label(text="Website:", font=(FONT_NAME, 10, 'normal'))
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", font=(FONT_NAME, 10, 'normal'))
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=(FONT_NAME, 10, 'normal'))
password_label.grid(column=0, row=3)

# `````````````````````````````` Entries  ```````````````````````````````````` #

website_entry = Entry(width=35)
website_entry.insert(END, string="")
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=35)
username_entry.insert(END, string=EMAIL)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=35)
password_entry.insert(END, string="")
password_entry.grid(column=1, row=3, columnspan=2)

# `````````````````````````````` Buttons  ```````````````````````````````````` #

search = Button(text='Search', width=15, command=find_password)
search.grid(column=3, row=1, columnspan=2)

generate = Button(text="Generate Password", width=15, command=generate_password)
generate.grid(column=3, row=3, columnspan=2)

add = Button(text="Add", width=30, command=add_password)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
