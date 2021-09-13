from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Radio button and message box")


# There are various way to do it so :
#1st way to define radio button:

frame1 = LabelFrame(root, padx = 100, pady = 100) # first frame for better visual
frame1.grid(row =0, column = 0)


r1 = IntVar()  #tkinter intiger variable
r1.set('1')


def display(val):
    myLabel1 = Label(frame1, text=val).pack() #it will display at 3rd frame




Radiobutton(frame1, text= "Option 1", variable=r1, value = 1).pack() #here value is int so we put 1(as intiger) if it was string then we use '1'
Radiobutton(frame1, text= "Option 2", variable=r1, value = 2).pack() #both are connected so we have same variable name
Radiobutton(frame1, text= "Option 3", variable=r1, value = 3).pack()
Radiobutton(frame1, text= "Option 4", variable=r1, value = 4).pack()

#output:
mybutton1 = Button(frame1, text ="click me", command = lambda : display(r1.get())).pack()

#This is second way:

frame2 = LabelFrame(root, padx = 100, pady = 100) # second frame for better visual
frame2.grid(row =0, column = 1)

Modes = [
            ("peper","peper"),
            ("cheese","cheese"),
            ("onion","onion"),
            ("mushrom","mushrom")
            ]

pizza = StringVar()
pizza.set("peper")

for text, mode in Modes:
    Radiobutton(frame2, text = text, variable = pizza, value = mode).pack(anchor = W)


def clicked(val):
    myLable2 = Label(frame2, text = val).pack() # it will display in 3rd frame

mybutton = Button(frame2, text = "click me", command = lambda : clicked(pizza.get())).pack()


root.mainloop()
