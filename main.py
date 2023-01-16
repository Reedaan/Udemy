from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(width=200, height=200, padx=20, pady=20)

canvas = Canvas(width=200, height=189)
logo_png = PhotoImage(file=r"D:\Python\Python Bootcamp\Day 29\logo.png")

canvas.create_image(100, 95, image=logo_png)
canvas.grid(column=0, row=0)




window.mainloop()

