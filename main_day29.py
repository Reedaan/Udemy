from tkinter import *
from tkinter import messagebox
import pyperclip
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    a = [password_list.append(random.choice(letters)) for a in range(nr_letters)]
    b = [password_list.append(random.choice(symbols)) for b in range(nr_symbols)]
    c = [password_list.append(random.choice(numbers)) for c in range(nr_numbers)]

    random.shuffle(password_list)

    password_entry.delete(0, END)
    password = "".join(password_list)
    pyperclip.copy(password)    
    password_entry.insert(0, string=f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
     
    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Information", message="You cannot leave empty boxes!")
    else: 
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("passwords.txt", "a") as save_passwords:
                save_password_string = f"{website} | {email} | {password}\n"
                save_passwords.write(save_password_string)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(width=200, height=200, padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file=r"D:\Python\Python Bootcamp\Day 29\logo.png")

#Logo
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0, "angela@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=1)

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

