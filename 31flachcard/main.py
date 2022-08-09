from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"

# ------- import the word ------
path = "data/words_to_learn.csv"
isExist = False
isExist = os.path.exists(path)
if isExist: 
    import_words = pd.read_csv("data/words_to_learn.csv")
else:
    import_words = pd.read_csv("data/french_words.csv")

words = import_words.to_dict(orient="record")
current_card = {} # this is dict that assigned a global dict of the current card

random_dic = random.choice(words)

START_LANGUAGE = list(random_dic.keys())[0]
TRANSLATED_LANGUAGE = list(random_dic.keys())[1]

#print(words)
#print('break')
#print(list(words))

# def get_word():
#     random_dic = random.choice(words)
#     start_language = list(random_dic.keys())[0] # start language
#     start_word = list(random_dic.values())[0] # start word
#     translated_lan = list(random_dic.keys())[1]
#     translated_word = list(random_dic.values())[1]
#     return (start_language, start_word, translated_lan, translated_word)

def next_card():
    global current_card
    current_card = random.choice(words)
    canvas.itemconfig(card_title, text=START_LANGUAGE, fill="black")
    canvas.itemconfig(card_word, text=current_card[START_LANGUAGE], fill="black")

    canvas.itemconfig(card_background, image=card_front_img)
    window.after(3000, func=flip_card)

def flip_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text=TRANSLATED_LANGUAGE, fill="white")
    canvas.itemconfig(card_word, text=current_card[TRANSLATED_LANGUAGE], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    flip_timer = window.after(3000, func=flip_card)

def remove_word():
    words.remove(current_card)
    data = pd.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#-----UI setup--------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=1)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
known_button = Button(image=right_img, highlightthickness=0, command=remove_word)
known_button.grid(row=1, column=1)

next_card()










window.mainloop()