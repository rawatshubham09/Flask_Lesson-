from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Slider")
root.iconbitmap(r'icons/light_icon.ico')
root.geometry("600x450")

def show():
    my_la = Label(root, text = var.get()).pack()

var = StringVar()


#Check Box

c = Checkbutton(root, text = "Check this box!", variable = var, onvalue = "On", offvalue = "Off")
c.deselect()
c.pack()

btn = Button(root, text = "Show Selection", command = show).pack()

root.mainloop()
