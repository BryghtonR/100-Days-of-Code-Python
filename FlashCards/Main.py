from tkinter import *
import random
import json

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50)

flash_dict = {}
start_count = 0
flash_front = " "
flash_back = " "
default_state = "Front"
flipped_state = "Front"

# builds dictionary from JSON file
def fill_flashcards():
    global start_count
    global flash_dict
    with open("english_korean.json", "r") as data_file:
        flash_dict = json.load(data_file)
    start_count = len(flash_dict)
    show_count()

def show_count():
    flash_count.config(text=f"{len(flash_dict)}/{start_count}")

# picks new flash card from remaining list
def fill_current_flash():
    global flash_front
    global flash_back
    if len(flash_dict) == 0: #makes sure list card list isn't empty
        flash_card.config(text="Complete", bg="white")
    else:
        flash_front = random.choice(list(flash_dict.keys())) # pick new flashcard and fills in front variable
        flash_back = flash_dict[flash_front] #fills in back variable
        if default_state == "Front": # auto shows default side of card
            show_front()
        elif default_state == "Back":
            show_back()
    show_count()

# card flipping functions
def show_front():
    global flipped_state
    flash_card.config(text=flash_front, bg="orange")
    flipped_state = "Front"

def show_back():
    global flipped_state
    flash_card.config(text=flash_back, bg="yellow")
    flipped_state = "Back"

def flip_flash():
    if flipped_state == "Front":
        show_back()
    elif flipped_state == "Back":
        show_front()

# correct guess removes card from the dictionary and displays new card
def correct_guess():
    if len(flash_dict) > 0:
        del flash_dict[flash_front]
    fill_current_flash()

# defaut front/back for all new cards
def set_def_state(var):
    global default_state
    default_state = var

def save_list():
    with open("data.json", "w") as data_file:
            json.dump(flash_dict, data_file, indent=4)

def load_list():
    global flash_dict
    with open("data.json", "r") as data_file:
        flash_dict = json.load(data_file)
    show_count()

# Main Flash Card Display
flash_card = Label(text=" ", font=("Arial", 50, "bold"), padx=50, pady=50)
flash_card.grid(row=0, column=0, columnspan=3)

flash_count = Label(text= "  /  ", font=("Arial", 10, "bold"))
flash_count.grid(row=2, column=2)

# Buttons
flip_button = Button(text="Flip", width=20, height=2, command=flip_flash)
flip_button.grid(row=1, column=1)

correct_button = Button(text="Correct", width=20, height=2, command=correct_guess)
correct_button.grid(row=1, column=2)

redo_button = Button(text="Redo", width=20, height=2, command=fill_current_flash)
redo_button.grid(row=1, column=0)

reset_button = Button(text="Start/Reset", width=20, height=2, command=lambda: [fill_flashcards(), fill_current_flash()])
reset_button.grid(row=3, column=0)

save_button = Button(text="Save", width=20, height=2, command=save_list)
save_button.grid(row=3, column=1)

load_button = Button(text="Load Save", width=20, height=2, command=load_list)
load_button.grid(row=3, column=2)

# Front/Back Menu
varList = StringVar(window)
varList.set("Front")
default_picker = OptionMenu(window, varList, "Front", "Back", command=set_def_state)
default_picker.grid(row=2, column=1)

#wrapup
window.mainloop()