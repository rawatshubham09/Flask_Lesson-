from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("New window screen")
root.iconbitmap('icons/light_icon.ico')

def click():
    global  screen_image
    top = Toplevel()
    top.title("Second Window")
    top.iconbitmap("icons/light_icon.ico")
    screen_image = ImageTk.PhotoImage(Image.open("images/img1.png"))
    screen_label = Label(top, image = screen_image).pack()


scr_image = ImageTk.PhotoImage(Image.open("images/img2.png"))

# creat canvas

canvas = Canvas(root).pack(fill ="both", expand = True)
canvas.create_image(0, 0, image = scr_image, anchor = True)


#label1 = Label(root, image = scr_image)
button = Button(label1, text = "Click_2nd_ window", command = click).pack()

Button_canvas = casvas.create_window(100, 10, anchor = 'nw', window = button)

mainloop()
