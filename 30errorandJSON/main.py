from re import T
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from turtle import title
import pyperclip
import json

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
    website = website_entry.get()
    email =  email_entry.get() 
    password =  pw_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave fields empty!")
    else:
        try: # try to see if works
            with open("data.json", mode="r") as data_file:
                #Reading Old Data
                data = json.load(data_file)
                #Updating old data with new data
                data.update(new_data)
        except FileNotFoundError: # if it does NOT work then do this
            with open("data.json", "w") as data_file:
                #saving entries
                json.dump(new_data, data_file, indent=4)
        else: # otherwise do this
            #Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #saving entries
                json.dump(data, data_file, indent=4)
        finally:   # and always do this at the end
            website_entry.delete(0, END)
            pw_entry.delete(0, END)

# ----------------------------- find pw --------------------------------#
def find_password():
    website = website_entry.get()
    try: # try to see if works
        with open("data.json", mode="r") as data_file:
            #Reading Old Data
            data = json.load(data_file)
            
    except FileNotFoundError: # if it does NOT work then do this
        messagebox.showinfo(title="Error", message="No Data File Found")
    else: # otherwise do this
        try:
            email = data[website]['email']
            pw = data[website]['password']
            messagebox.showinfo(title=website, message=f"The Email is: {email}\nThe password is: {pw}")
        except KeyError:
            messagebox.showinfo(title="None Found", message="No Details for the website")



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
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
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
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()