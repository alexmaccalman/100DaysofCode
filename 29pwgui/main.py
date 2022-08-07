import atexit
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # new_list = [new_item for item in list]

    pw_letters = [choice(letters) for _ in range(randint(8,10))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pw_list = pw_letters + pw_numbers + pw_symbols
    shuffle(pw_list)
    pw = "".join(pw_list)
    pw_entry.insert(0, pw)
    pyperclip.copy(pw)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    email =  email_entry.get() 
    pw =  pw_entry.get()

    if len(web) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email} "
                                                f"\nPassword: {pw} \nIs ot ok to save?")
        if is_ok:
            with open("./data.txt", mode="a") as file:
                entry = str(web) + " | " + str(email) + " | " + str(pw)
                file.write(f"{web} | {email} | {pw}\n")
                website_entry.delete(0, END)
                pw_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=1)
pw_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pw_img)
canvas.grid(row=0, column=1)
#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)
#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
pw_entry = Entry(width=21)
pw_entry.grid(row=3, column=1)
# Buttons
gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()