from tkinter import *

root = Tk()
root.config(background="lavender")
root.geometry("300x300")

label1 = Label(root, text="Chocolates and IceCreams", font="50")
label1.pack(pady=20)

topframe = Frame(root)
topframe.pack()

button1= Button(topframe, text= "Choco", fg = "red", bg="pink")
button1.pack(side=LEFT)

button2 = Button(topframe, text = "Dark Choco", fg="brown", bg="pink")
button2.pack(side=LEFT)

button3 = Button(topframe, text = "White Choco", fg="blue", bg="pink")
button3.pack(side=LEFT)

bottomframe = Frame(root)
bottomframe.pack(pady=10)

button4 = Button(bottomframe, text="Tirimisu", fg = "green", bg = "blue")
button4.pack(side=TOP)

button5 = Button(bottomframe, text="Cake", fg = "green", bg = "cyan")   
button5.pack(side=TOP)

button6 = Button(bottomframe, text="Pastry", fg = "green", bg = "lime")
button6.pack(side=TOP)




root.mainloop()