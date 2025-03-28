# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_list = []
    for _ in range(0, nr_letters):
        password_list.append(random.choice(letters))

    for _ in range(0, nr_symbols):
        password_list.append(random.choice(symbols))

    for _ in range(0, nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)  #END represent the very last character in entry
    pyperclip.copy(password)  #this will copy the password the moment it is generated
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    if len(website_input) == 0 or len(password_input) == 0:
        messagebox.showinfo(title = "oops", message = "please don't leave any field empty!")
    else:
        yes = messagebox.askyesno(title = website_input, message = f"These are the details entered: \nWebsite: {website_input} "
                                                             f"\nEmail: {email_input} \nPassword: {password_input} \n Do you want to save it?")
        if yes:
            with open("data.txt", mode = "a") as file:
                file.write(f"\n{website_input} | {email_input} | {password_input}")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *  #astik only give all the classes but not the module like massagebox
from tkinter import messagebox
import random
import pyperclip #pyperclip is a cross platform python module for copy and paste clipboard functions.
window = Tk()
window.title("Password Generator")
window.config(padx = 50, pady = 50, bg = "white")

canvas = Canvas(height = 200, width = 200, bg = "white", highlightthickness= 0)
canvas.grid(row = 0, column = 1)
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = lock_img)

website_label = Label(text = "Website: ")
website_label.grid(row = 1, column = 0)
website_entry = Entry(width = 35)
website_entry.focus() #focus will put a cursor by default in the entry

website_entry.grid(row = 1, column = 1, columnspan = 2)
email_label = Label(text = "Email/Username: ")
email_label.grid(row = 2, column = 0)
email_entry = Entry(width = 35)
email_entry.insert(END, "fm@gmail.com")   # END represent the very last character in entry


email_entry.grid(row = 2, column = 1, columnspan = 2)
password_label = Label(text = "Password: ")
password_label.grid(row = 3, column = 0)
password_entry = Entry(width = 21)
password_entry.grid(row = 3, column = 1)

#button
button = Button(text = "Generate Password", command= generate)
button.grid(row = 3, column = 2)

button = Button(text = "ADD", width= 36, command= save)
button.grid(row = 4, column = 1, columnspan = 2)







window.mainloop()
