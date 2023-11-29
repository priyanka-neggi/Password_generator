from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = input.get()
    try:
        with open("passwords.json","r") as file:
            name = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="no file saved")

    else:
        if website in name:
            email = name[website]["email"]
            password = name[website]["password"]
            messagebox.showinfo(title=website, message=f"email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="oppps",message="no data is saved with this name")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_char = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_number+password_char+password_symbol
    shuffle(password_list)
    password = "".join(password_list)

    input3.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website= input.get()
    email= input2.get()
    password=input3.get()
    new_data = {website:{
        "email": email,
        "password":password
    }}
    if len(website)>0 and len(password) >0:
        is_ok = messagebox.askokcancel(website,
                                       f"these are the details \n email: {email}\n password: "
                                       f"{password}\n do you want to save it?")
        if is_ok:
            try:
                with open("passwords.json", "r") as file:
                # json.dump(new_data, file, indent=4) -->write
                # data=json.load(file)print(data) ---> read
                # update :
                    data = json.load(file)
            except FileNotFoundError:
                with open("passwords.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                input.delete(0, END)
                input3.delete(0, END)
    else:
        messagebox.showinfo("empty column","password or/and website name is empty")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password generator")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)
website = Label(text="Website : ")

website.grid(row=1, column=0)
input = Entry(width=25)
input.focus()
input.grid(row=1, column=1)
search= Button(text="Search", fg="blue",width=14, command=find_password)
search.grid(row=1, column=2)
email = Label(text="Email/ Username: ")
email.grid(row=2, column=0)
input2 = Entry(width=43)
input2.insert(0, "negip105@gmail.com")
input2.grid(row=2, column=1, columnspan=2)
password = Label(text="Password: ")
password.grid(row=3, column=0)
input3 = Entry(width=25)
input3.grid(row=3, column=1)
generator = Button(text="Password Generator", command=password_generator)
generator.grid(row=3, column=2)
add = Button(text="Add", width=30, command=save)
add.grid(row=4, column=1, columnspan=2)
window.mainloop()


