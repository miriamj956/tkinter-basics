from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Login screen")
root.config(background="violet")

user_name = Label(root, text = "Username").place(x = 40, y = 60)
user_name_entry = Entry(root, width=30).place(x = 110, y = 60)

password = Label(root, text = "Password").place(x = 40, y = 100)
password_entry = Entry(root, width = 30, show = "*").place(x = 110, y = 102)

btn = Button(root, text = "Login", bd = 5, background = "pink", command = root.destroy)
btn.place(x = 40, y = 140)

root.mainloop()
