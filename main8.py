from tkinter import *

root = Tk()
root.geometry("300x400")
root.config(background="pink")

label1 = Label(root, text="Scrollbar", font= "50")
label1.pack(pady = 10)

scroll = Scrollbar(root)
scroll.pack(side = RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scroll.set)

for i in range(1,30):
    mylist.insert(END, "Hi"+ str(i))
mylist.pack()
scroll.config(command=mylist.yview)

root.mainloop()