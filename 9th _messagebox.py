from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title(" click me for message box")


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

#these are few popup msg box

def popup(val):
    if val == 1:
        responce = messagebox.showinfo("Message", "You Know this") #this will give ok
        #print(responce)
    if val == 2:
        responce = messagebox.showwarning("Warning", "Don't Take it serious") #this will give ok
        #print(responce)
    if val == 3:
        responce = messagebox.showerror("Error", "Just testing")#this will give ok
        #print(responce)
    if val == 4:
        responce = messagebox.askquestion("Question", "how many day in a year ?")#this will give yes
        #print(responce)
    if val == 5:
        responce = messagebox.askokcancel("Asking ", "Are you ok ?")
        #print(responce)
    if val == 6:
        responce = messagebox.askyesno("Tell Truth ", "I am Awsome ?")
        #print(responce)
        
    # Taking value from msg box and answer it:
    if responce =='ok' or 'yes':
        label = Label(root, text = "Yes you nailed it").pack()
    else:
        label = Label(root, text = "NOOOOOOO").pack()

r = IntVar()
r.set('1')

Radiobutton(root, text= "Show Info",variable=r, value = 1, command = lambda : popup(r.get())).pack() 
Radiobutton(root, text= "Showw Warning",variable=r,value = 2, command = lambda : popup(r.get()) ).pack() 
Radiobutton(root, text= "Show Error",variable=r,value = 3, command = lambda : popup(r.get())).pack()
Radiobutton(root, text= "Ask Question",variable=r,value = 4, command = lambda : popup(r.get())).pack()
Radiobutton(root, text = "Ask ok cancel",variable=r,value = 5, command = lambda : popup(r.get())).pack()
Radiobutton(root, text = "ask yes_no",variable=r,value = 6, command = lambda : popup(r.get())).pack()

mainloop()



