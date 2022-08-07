from cgi import test
from cgitb import text
from tkinter import *

def button_clicked():
    new_text = input_miles.get()
    miles = float(new_text)
    km = str(convert_miles_to_km(miles))
    output_km.config(text=km)

def convert_miles_to_km(miles):
    km = 1.609344 * miles
    return km

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) #adds padding around GUI

# Label
my_label = Label(font=("Arial", 18, "bold"))
my_label["text"] = "is equal to" # reassign kwargs "text"
my_label.config(text="is equal to") # another way to reassign
#my_label.pack() # places label on the screen
#my_label.place(x=100, y=200)
my_label.grid(column=0, row=1) # grid system is relative to other components. 
#my_label.config(padx=50, pady=50)

label2 = Label(font=("Arial", 18, "bold"))
label2.config(text="Miles")
label2.grid(column=2, row=0)

label3 = Label(font=("Arial", 18, "bold"))
label3.config(text="Km")
label3.grid(column=2, row=1)

output_km = Label(font=("Arial", 10))
output_km.grid(column=1, row=1) 

# Entry
input_miles = Entry(width=10)
input_miles.grid(column=1, row=0) # cannot mix up grid and pack methods

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
