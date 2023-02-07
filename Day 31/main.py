from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# ---------------------------- Data ------------------------------- #
try:
    data = pandas.read_csv(
        r"D:\Python\Python Bootcamp\Day 31\data\words_to_learn.csv")
    data_dict = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv(
        r"D:\Python\Python Bootcamp\Day 31\data\french_words.csv")
    data_dict = data.to_dict(orient="records")

current_card = {}

def generate_new():

    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(create_title, text="French", fill="black")
    canvas.itemconfig(create_description,
                      text=current_card["French"], fill="black")
    canvas.itemconfig(main_photo, image=card_front_png)
    flip_timer = window.after(3000, func=flip_card)


def add_to_known():
    if current_card in data_dict:
        data_dict.remove(current_card)

    df = pandas.DataFrame(data_dict)
    df.to_csv(
        r"D:\Python\Python Bootcamp\Day 31\data\words_to_learn.csv", index=False)

    generate_new()


# ---------------------------- GUI ------------------------------- #
# Window config

def flip_card():
    canvas.itemconfig(main_photo, image=card_back_png)
    canvas.itemconfig(create_title, text="English", fill="white")
    canvas.itemconfig(create_description,
                      text=current_card["English"], fill="white")


window = Tk()
window.title("Flash card Project")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Addressing photos
card_front_png = PhotoImage(
    file=r"D:\Python\Python Bootcamp\Day 31\images\card_front.png")

card_back_png = PhotoImage(
    file=r"D:\Python\Python Bootcamp\Day 31\images\card_back.png")

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
main_photo = canvas.create_image(400, 263, image=card_front_png)
create_title = canvas.create_text(
    400, 150, text="French", font=(FONT_NAME, 40, "italic"))
create_description = canvas.create_text(
    400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
x_image = PhotoImage(file=r"D:\Python\Python Bootcamp\Day 31\images\wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=generate_new)
x_button.grid(row=1, column=0)

y_image = PhotoImage(file=r"D:\Python\Python Bootcamp\Day 31\images\right.png")
y_button = Button(image=y_image, highlightthickness=0, command=add_to_known)
y_button.grid(row=1, column=1)


window.mainloop()
