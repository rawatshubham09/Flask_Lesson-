from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("learn Frame")

frame = LabelFrame(root, padx = 100, pady = 65)
frame.pack(padx = 10, pady = 10)

b = Button(frame, text="Dont click here", padx = 10, pady = 8)
b.grid(row = 0, column = 0)

#this button will distroy the frame dont press
b2 = Button(frame, text="click here", padx = 10, pady = 8,command = frame.destroy)
b2.grid(row = 1, column = 1)


root.mainloop()
