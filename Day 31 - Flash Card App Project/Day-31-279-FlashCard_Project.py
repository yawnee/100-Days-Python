from tkinter import *
import pandas as p
import random
import time
from tkinter import messagebox
from random import choice, randint, shuffle



# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
current_card = {}
word_dict = {}

try:
    data = p.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = p.read_csv('data/french_words.csv')
    word_dict = original_data.to_dict(orient='records')
else:
    word_dict = data.to_dict(orient='records')

current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    current_word = current_card['French']
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_word, fill='black')
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    current_eng_word = current_card['English']
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_eng_word, fill='white')
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    word_dict.remove(current_card)
    print(len(word_dict))
    data = p.DataFrame(word_dict)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file='images/card_back.png')  # must always be outside of function
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, 'italic'))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# ``````````````````````````````Labels ```````````````````````````````````` #

# title_label = Label(text="Title", font=("Ariel", 40, 'italic'))
# title_label.grid(column=0, row=0)
#
# word_label = Label(text="Word", font=("Ariel", 60, 'bold'))
# word_label.grid(column=0, row=0)

# `````````````````````````````` Buttons  ```````````````````````````````````` #

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

correct_button_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_button_img, highlightthickness=0, command=is_known)
correct_button.grid(column=1, row=1)

next_card()

window.mainloop()
