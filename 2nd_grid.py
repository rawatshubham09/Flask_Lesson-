from tkinter import *
root = Tk(screenName = "First")

''' this Label creat text file and root is thinkter Tk()
'''
label1 = Label(root, text = 'Hellow this is my first Prototype')
label2 = Label(root, text = 'using grid system')

#appling Grid in lable:

label1.grid(row = 1, column = 5)
label2.grid(row = 2, column = 5)


root.mainloop()
