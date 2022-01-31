from tkinter import *
import pandas as p
import glob
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #

FONT_NAME = "Courier"
EMAIL = "test@test.com"


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

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title='Error', message='There is no value in the entry')
    else:
        answer = messagebox.askokcancel(title=website,
                                        message=f'These are the details entered: \n{username} \nPassword: {password}\nContinue to save?')
        if answer:
            # Writes into data with append
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")

            # Clears the text from the typebox
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

password_entry = Entry(width=21)
password_entry.insert(END, string="")
password_entry.grid(column=1, row=3)

# `````````````````````````````` Buttons  ```````````````````````````````````` #

generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=3, row=3)

add = Button(text="Add", width=36, command=add_password)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
