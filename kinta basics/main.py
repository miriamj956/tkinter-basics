from tkinter import *

#create output screen
root = Tk()

#output display size
root.geometry("500x500")

#create widget - button, text, entry....
btn = Button(root, text = "Click Me!", bd = 5, background = "pink", command = root.destroy)

#place widget on screen (if you dont set a side it will go center)
btn.pack(side = "top")

btn1 = Button(root, text="Hi", bd = 5, background="purple", command=root.destroy)
btn1.pack(side="bottom")

btn2 = Button(root, text="hello", bd=5, background="green", command=root.destroy)
btn2.pack(side= "left")

btn3 = Button(root, text="DO NOT CLICK", bd = 4, background="red", command=root.destroy)
btn3.pack(side="right")

root.mainloop()




