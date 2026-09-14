from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
flip_timer = None
# ---------------------------- NEXT CARD ------------------------------- #
def next_card():
    global flip_timer
    global current_card
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    flip_timer = window.after(3000, flip_card)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# ---------------------------- BUTTONS ------------------------------- #
unknown_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, bd=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, highlightthickness=0, bd=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
