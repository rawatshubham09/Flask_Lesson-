from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Option Menu")
root.iconbitmap(r'icons/light_icon.ico')
root.geometry("600x450")

def show():
    lab = Label(root, text = clicked.get()).pack()

opt = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


clicked = StringVar()
clicked.set(opt[0])

drop = OptionMenu(root, clicked, *opt)
drop.pack()

myButton = Button(root, text = "Show Selection", command = show).pack()

root.mainloop()
