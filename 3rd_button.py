from tkinter import *
root = Tk(screenName = "First")

#This function will get call for every click

def myClick():
    label1 = Label(root, text = 'Hellow this is my first Prototype')
    label1.pack()


# inserting button:

button1 = Button(root, text = "Click Me !", command = myClick ,fg = 'black', bg = "red")
button1.pack()

root.mainloop()
