from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for letter in range(nr_letters)]
    password_list += [random.choice(symbols) for symbol in range(nr_symbols)]
    password_list += [random.choice(numbers) for number in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    # copies password right away, so by using Ctrl+V we can paste our password wherever we want
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if website == "" or password == "":  # or  if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")

    website_entry.delete(0, "end")  # or    website_entry.delete(0, END)
    password_entry.delete(0, "end")  # or    password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=153, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_lbl = Label(text="Website:")
website_lbl.grid(column=0, row=1)

email_lbl = Label(text="Email/Username:")
email_lbl.grid(column=0, row=2)

password_lbl = Label(text="Password:")
password_lbl.grid(column=0, row=3)

# Entries
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "sultonovjaloliddin07@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", fg="blue", bg='light blue', command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, bg='pink', command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
