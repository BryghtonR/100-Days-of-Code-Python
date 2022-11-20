from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import json

default_email = "YourEmail@email.com"
astrics = "*"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+']
def gen():
    password = []
    password = [choice(letters) for _ in range(randint(12,16))]
    shuffle(password)
    password = "".join(password)
    entry_password.delete(0, END)
    entry_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    if len(entry_email.get()) == 0 or len(entry_website.get()) == 0 or len(entry_password.get()) == 0:
        messagebox.showinfo(title="", message="Please fill all boxes!")
    else:
        with open(file="SavedPasswords.json", mode="w") as new_file:
            new_file.write(entry_website.get() + " | " + entry_email.get() + " | " + entry_password.get() + "\n")
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")

#Canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
myPass_Image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=myPass_Image)
canvas.grid(row=0, column=1)
window.config(padx=50, pady=50, bg="white")

#Labels for Entries
label_website = Label(text="Website")
label_website.grid(row=1, column=0)

label_email = Label(text="Email")
label_email.grid(row=2, column=0)

label_password = Label(text="Password")
label_password.grid(row=3, column=0)

# Entry boxes
entry_website = Entry(width=50)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

entry_email = Entry(width=50)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, default_email)

entry_password = Entry(width=32, show="*")
entry_password.grid(row=3, column=1)

#Buttons
Generate_Button= Button(text="Generate Password", command=gen)
Generate_Button.grid(row=3, column=2)

add_button = Button(text="Add", command=add, width=40)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()