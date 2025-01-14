from tkinter import *

root = Tk()
root.geometry("300x400")
root.config(background="lavender")

label1 = Label(root, text="My favorite foods:", font="40")
label1.pack(pady=10)

listbox = Listbox(root, height=10, width=15, bg="grey", activestyle='underline', font="Helvetica", fg="yellow")
#dotbox, underline, and none are the highlighting styles for selected text
listbox.insert(1,"IceCream")
listbox.insert(2, "Tirimisu")
listbox.insert(3, "Pasta")
listbox.pack()

root.mainloop()