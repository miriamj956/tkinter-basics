from tkinter import *
from tkinter.ttk import *
import time

root = Tk()

progress = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
progress.pack()

def Bar():
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
    root.update_idletasks()
    time.sleep(1)


startbutton = Button(root,text= "Start", command=Bar)
startbutton.pack()



root.mainloop()