from tkinter import *
root = Tk()

# take input and make a box
e = Entry(root, width = 50)
e.pack()
# it will write these line in backscreen
e.insert(0, "Enter ur Name")
#This function will get call for every click

def myClick():
    t = "hellow "+e.get()
    label1 = Label(root, text = t)
    label1.pack()


# inserting button:

button1 = Button(root, text = "Click Me !", command = myClick ,fg = 'black', bg = "red")
button1.pack()

root.mainloop()
