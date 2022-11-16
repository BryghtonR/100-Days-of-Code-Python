from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

def button_clicked():
    input = new_input.get()
    final_output = round(float(input) * 1.6)
    output.config(text=f"{final_output}")


new_input = Entry(width=10)
new_input.grid(row=1, column=2)

input_label = Label(text="Miles", font=("Arial", 12, "normal"))
input_label.grid(row=1, column=3)

equal_to = Label(text="is equal to", font=("Arial", 12, "normal"))
equal_to.grid(row=2, column=1)

output = Label(text="0", font=("Arial", 12, "normal"))
output.grid(row=2, column=2)

output_label = Label(text="KM", font=("Arial", 12, "normal"))
output_label.grid(row=2, column=3)

button = Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=2)





window.mainloop()