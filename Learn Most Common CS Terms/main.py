from tkinter import *
import pandas
import random
flip_timer = None
data_dict = {}

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

try:
    data_file = pandas.read_csv("data/ords_to_learn.csv")
except FileNotFoundError:
    data_file = pandas.read_csv("data/most_cs_common_words.csv")
finally:
    data_dict_list = data_file.to_dict(orient="records")


def save_progress():
    data_dict_list.remove(data_dict)
    df = pandas.DataFrame(data_dict_list)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    window.after_cancel(flip_timer)
    canvas.itemconfig(front_card_canvas, image=back_card_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=data_dict["English"], fill="white")
    canvas.itemconfig(word_definition, text="")


def next_card():
    global data_dict, flip_timer
    data_dict = random.choice(data_dict_list)
    random_french_word = data_dict["Arabic"]
    canvas.itemconfig(front_card_canvas, image=front_card_image)
    canvas.itemconfig(word_text, text=random_french_word, fill="black")
    canvas.itemconfig(title_text, text="Arabic", fill="black")
    canvas.itemconfig(word_definition, text="(للمصطلح مختصر تعريف)")
    flip_timer = window.after(3000, flip_card)


window = Tk()
window.title("Learn Most Common CS Terms")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

back_card_image = PhotoImage(file="images/card_back.png")
front_card_image = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_canvas = canvas.create_image(400, 263, image=front_card_image)
title_text = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
word_text = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
word_definition = canvas.create_text(400, 360, text="تعريف مختصر للمصطلح", font=("Ariel", 50))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=save_progress)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
