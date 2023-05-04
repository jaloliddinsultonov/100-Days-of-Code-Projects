from tkinter import *

# converting from miles to km
def calculate():
    a = float(input_number.get())
    km = a * 1.6
    label_answer.config(text=f"{km}")

# Window
window = Tk()
window.minsize(width=300, height=200)
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

# Label
label_nothing = Label(text="")
label_nothing.grid(column=0, row=0)

label_miles = Label(text="Miles", font=("Align", 10, "bold"))
label_miles.grid(column=2, row=0)
label_miles.config(padx=20, pady=20)

label_is_equal_to = Label(text="is equal to", font=("Align", 10, "bold"))
label_is_equal_to.grid(column=0, row=1)

label_km = Label(text="Km", font=("Align", 10, "bold"))
label_km.grid(column=2, row=1)

label_answer = Label(text="0")
label_answer.grid(column=1, row=1)

# Entry
input_number = Entry(width=10)
input_number.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()

