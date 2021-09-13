from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Slider")
root.iconbitmap(r'icons/light_icon.ico')
root.geometry("600x450")

def slide():# defining a FUnction Slider
    global hor, ver
    
    H = hor.get()
    if H < 200:
        H = 200
    
    V = ver.get()
    if V < 150:
        V = 150
    
    my_label = Label(root, text = str(H) +"x" + str(V)).pack()
    root.gemetory(str(H) +"x" + str(V))
#ver = IntVar()
ver= Scale(root, from_ = 0, to = 600).pack()
#hor = IntVar()
hor = Scale(root,orient = HORIZONTAL, from_= 0, to = 450).pack()
print(hor, ver)

my_btn = Button(root, text = "Click me!", command = slide).pack()

root.mainloop()
