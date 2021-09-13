from tkinter import *
root = Tk()
root.title("Simple Calculator")


# take input and make a box
e = Entry(root, width = 35, borderwidth = 5)
e.grid(row=0,column=0, columnspan=3, padx=10, pady=10)

# it will write these line in backscreen
#e.insert(0, "Enter ur Name")
#This function will get call for every click

def button_click(num):
    current = str(e.get())#here we are converting current no. on screen to string
    e.delete(0,END)
    e.insert(0,current + str(num) ) #we contanated the screen no. in string to
                                    #new no in string
def clear_button():
    e.delete(0,END)#clearing the screen

#function button it perform all function:

def funct(token):
    num1 = int(e.get()) #getting first no.
    global f_num
    f_num = num1
    global math #creating a global vairablee math which will take operator
    math = token
    clear_button()
    
def button_sqr():
    global math
    math = "sqr"
    
def button_cube():
    global math
    math = "cube" 
    

'''def button_add():
    num1 = int(e.get()) #getting first no.
    global f_num
    f_num = num1
    global math #creating a global vairablee math which will take operator
    math = "add"
    clear_button() #clearing screen for second no.
    
def button_sub():
    num1 = int(e.get()) #getting first no.
    global f_num
    f_num = num1
    global math #creating a global vairablee math which will take operator
    math = "sub"
    clear_button() #clearing screen for second no.
    
def button_mul():
    num1 = int(e.get()) #getting first no.
    global f_num
    f_num = num1
    global math #creating a global vairablee math which will take operator
    math = "mul"
    clear_button() #clearing screen for second no.
    
def button_div():
    num1 = int(e.get()) #getting first no.
    global f_num
    f_num = num1
    global math #creating a global vairablee math which will take operator
    math = "div"
    clear_button() clearing screen for second no. '''


def button_equal():
    num2 = int(e.get()) #taking second no. on screen
    clear_button()
    if math =='add':    # accorning to math 'token' it will perform function
        ans = num2+f_num
    if math =='sub':
        ans = f_num-num2
    if math =='mul':
        ans = num2*f_num
    if math =='div':
        ans =int(f_num/num2)
    if math =='sqr':
        ans = num2*num2
    if math =='cube':
        ans = num2*num2*num2
    e.insert(0, str(ans))

# inserting button:
button_1 = Button(root, text = '1', padx=40, pady=20, bg = '#ffe4c4', command= lambda: button_click(1))
button_2 = Button(root, text = '2', padx=40, pady=20, bg = '#ffe4c4',command= lambda: button_click(2))
button_3 = Button(root, text = '3', padx=40, pady=20, bg = '#ffe4c4',command= lambda: button_click(3))

button_4 = Button(root, text = '4', padx=40, pady=20, bg = '#ffe4c4',command= lambda: button_click(4))
button_5 = Button(root, text = '5', padx=40, pady=20, bg = '#ffe4c4',command= lambda: button_click(5))
button_6 = Button(root, text = '6', padx=40, pady=20, bg = '#ffe4c4',command= lambda: button_click(6))

button_7 = Button(root, text = '7', padx=40, pady=20, bg = '#ffe4c4',command= lambda: button_click(7))
button_8 = Button(root, text = '8', padx=40, pady=20, bg = '#ffe4c4',command= lambda: button_click(8))
button_9 = Button(root, text = '9', padx=40, pady=20, bg = '#ffe4c4',command= lambda: button_click(9))

button_0 = Button(root, text = '0', padx=39, pady=20, bg = '#ffe4c4',command= lambda: button_click(0))
button_equal = Button(root, text = '=', padx=91, pady=20, bg = '#00FFFF',command= button_equal)
button_clear = Button(root, text = 'Clear', padx=60, pady=20,bg = '#ffe4c4', command= lambda: clear_button())

button_add = Button(root, text = '+', padx=40, pady=20, bg = '#ffe4c4', command= lambda : funct('add'))
button_multiply = Button(root, text = 'x', padx=40, pady=20, bg = '#ffe4c4', command= lambda : funct('mul'))
button_divide = Button(root, text = '/', padx=39, pady=20, bg = '#ffe4c4', command= lambda : funct('div'))
button_subtract = Button(root, text = '-', padx=40, pady=20, bg = '#ffe4c4', command= lambda : funct('sub'))

button_sqr = Button(root, text = 'x^2', padx=38, pady=20, bg = '#ffe4c4', command= button_sqr)
button_cube = Button(root, text = 'x^3', padx=38, pady=20,bg = '#ffe4c4', command= button_cube)




#-------------------------------This will place the button on the screen......................
button_clear.grid(row=1,column=1, columnspan = 2 ) #row = 1

button_7.grid(row=2,column=0 ) #row 2
button_8.grid(row=2,column=1 )
button_9.grid(row=2,column=2 )

button_4.grid(row=3,column=0 ) #row 3
button_5.grid(row=3,column=1 )
button_6.grid(row=3,column=2 )

button_1.grid(row=4,column=0 ) #row 4
button_2.grid(row=4,column=1 )
button_3.grid(row=4,column=2 )

button_0.grid(row=5,column=0 ) #row 5
button_sqr.grid(row=5,column=1 )
button_cube.grid(row=5,column=2 )

button_add.grid(row=6,column=0 ) #row 6
button_multiply.grid(row=6,column=1 )
button_subtract.grid(row=6,column=2 )

button_divide.grid(row=7,column=0 ) # row 7
button_equal.grid(row=7,column=1, columnspan = 2 )

root.mainloop()
