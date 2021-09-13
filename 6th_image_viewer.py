#Importing hedder Filess
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title(" Image viewer ")
root.resizable(0,0)

root.iconbitmap(r'icons/light_icon.ico') #Change icon of GUI

#Creating frame

frame=Frame(root, width=600, height=500, bg='white', relief=GROOVE, bd=2)
frame.pack(padx=10, pady=10)

#Creating thumbnails of all images
img1 = Image.open("Images/img1.jpg")#img 1
img1.thumbnail((500,400))
my_img1 = ImageTk.PhotoImage(img1) 

img2 = Image.open("Images/img2.jpg")#img 2
img2.thumbnail((500,400))
my_img2 = ImageTk.PhotoImage(img2)

img3 = Image.open("Images/img3.jpg")#img 3
img3.thumbnail((500,400))
my_img3 = ImageTk.PhotoImage(img3)

# creating list of image
image_list = [my_img1, my_img2, my_img3]

# configure the image to Label in frame
i=0
my_label = Label(frame,image = image_list[i])
my_label.pack()

# main logic
def previous():
    global i
    i = i - 1
    try:
        my_label.config(image=image_list[i])
    except:
        i = 0
        previous()
def next():
    global i
    i = i + 1
    try:
        my_label.config(image=image_list[i])
    except:
        i = -1
        next()

# create buttons    
btn1 = Button(root, text="Previous", bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=previous)
btn1.pack(side=LEFT, padx=60, pady=5)

btn2 = Button(root, text="Next", width=8, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=next)
btn2.pack(side=LEFT, padx=60, pady=5)

btn3 = Button(root, text="Exit", width=8, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=root.destroy)
btn3.pack(side=LEFT, padx=60, pady=5)

root.mainloop()
