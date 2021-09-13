from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("File DIlog")
root.iconbitmap(r'icons/light_icon.ico')

def open():
    global img
    root.filename = filedialog.askopenfilename(initialdir = "/Images", title = "Select A File", filetypes = (("png files", "*.png"),("all files", "*.*")))
    img = ImageTk.PhotoImage(Image.open(root.filename))
    img_label = Label(image = img).pack()


btn = Button(root, text = "Open Files", command = open).pack()

root.mainloop()
