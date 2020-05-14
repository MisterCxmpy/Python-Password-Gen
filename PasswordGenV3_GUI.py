import tkinter as tk
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

HEIGHT = 400
WIDTH = 600

def low(): #The function for creating a random password according to whatever the user picks as their security level.
    entry.delete(0, END)

    length = var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password

    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password

    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")

def generate(): #Function that creates the password and inputs it into the entry box.
    password1 = low()
    entry.insert(10, password1)

def copy1(): #Function that copies the text from the entry box.
    random_password = entry.get()
    pyperclip.copy(random_password)

def save(): #Function that saves the entry box data into a .txt document.
    file = open('passwords.txt','a+')
    file.write(entry.get() + '\n')
    file.close()

root = tk.Tk()
var = IntVar()
var1 = IntVar()

root.title("Random Password Generator")
root.iconbitmap("passwordicon.ico")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

root.resizable(0, 0)

frame = tk.Frame(root, bg="#764ce0")                                        #------\
frame.place(relwidth=1, relheight=1)                                        #------ Code that creates the frame.
entry = tk.Entry(frame, bg="white", bd=5, font=("Arial Rounded MT", 15))    #------ Code that creates the entry box.
entry.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")   #------/

c_label = Label(root, text="Length")
c_label.place()

copy_button = tk.Radiobutton(root, text="Copy", value=5, command=copy1, bg="#4926a3", height=40, width=40, indicatoron=0, selectcolor="#90ee90", font=("Arial Rounded MT", 15))                 #------\ Copy button
copy_button.place(relx=0.525, rely=0.27, relheight=0.1, relwidth=0.3, anchor="w")

generate_button = tk.Radiobutton(root, text="Generate", value=4, command=generate, bg="#4926a3", height=40, width=40, indicatoron=0, selectcolor="#90ee90", font=("Arial Rounded MT", 15))      #-------\ Generate button
generate_button.place(relx=0.525, rely=0.38, relheight=0.1, relwidth=0.3, anchor="w")

weakPass = tk.Radiobutton(root, text="Weak", variable=var, value=1, bg="#4926a3", height=40, width=40, indicatoron=0, selectcolor="#90ee90", font=("Arial Rounded MT", 15))                     #------ Code that creates the buttons - Weak Button
weakPass.place(relx=0.475, rely=0.27, relheight=0.1, relwidth=0.3, anchor="e")

mediumPass = tk.Radiobutton(root, text="Medium", variable=var, value=0, bg="#4926a3", height=40, width=40, indicatoron=0, selectcolor="#90ee90", font=("Arial Rounded MT", 15))                 #------ Code that creates the buttons - Medium Button
mediumPass.place(relx=0.475, rely=0.38, relheight=0.1, relwidth=0.3, anchor="e")

strongPass = tk.Radiobutton(root, text="Strong", variable=var, value=3, bg="#4926a3", height=40, width=40, indicatoron=0, selectcolor="#90ee90", font=("Arial Rounded MT", 15))                 #-------/ Strong Button
strongPass.place(relx=0.475, rely=0.49, relheight=0.1, relwidth=0.3, anchor="e")

savePass = tk.Button(root, text="Save", command=save, bg="#4926a3", height=40, width=40, activebackground="#90ee90", font=("Arial Rounded MT", 15))                                                                         #------/ Save button
savePass.place(relx=0.65, rely=0.60, relheight=0.1, relwidth=0.3, anchor="e")

combo = Combobox(root, textvariable=var1)

combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,        #------\
                   17, 18, 19, 20, 21, 22, 23, 24, 25,      #------ The combo values for the length of the password.
                   26, 27, 28, 29, 30, 31, 32)              #------/

combo.current(0)
combo.configure(font=("Arial Rounded MT", 15))
combo.bind('<<ComboboxSelected>>')
combo.place(relx=0.525, rely=0.49, relheight=0.1, relwidth=0.3, anchor="w")

root.mainloop()