from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Align", 14, "bold"))
# my_label.pack(side='left')
my_label.grid(column=0, row=0)
my_label.config(padx=100, pady=200)

my_label["text"] = "New Text"   # These things do the same thing
my_label.config(text="New Text")    # These things do the same thing

# Button
def button_clicked():
    # my_label['text'] = input.get()
    my_label.config(text=input.get())


button = Button(text="Click me")
button.grid(column=1, row=1)

button2 = Button(text="New Button")
button2.grid(column=2, row=0)

# Entry
input = Entry(width=20)
input.grid(column=3, row=2)
print(input.get())






window.mainloop()