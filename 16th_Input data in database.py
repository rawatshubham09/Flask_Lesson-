# There are 5 data type in sql:-
# text, int, real, null, blob(img file/video type)


# we only needed to run this file for one time after it we get our
# database name -> address_book.db

from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Option Menu")
root.iconbitmap(r'icons/light_icon.ico')
#root.geometry("600x450")
'''
# 3) Creat Table :-

c.execute(""" CREATE TABLE addresses(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer)
    """)
'''
# Creat Submit Function:

def submit():
    #connecting database
    conn = sqlite3.connect("database/address_book.db")

    # 2) Creat cursor :-
    c = conn.cursor()

    # 3) Adding Data in Data base
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  "f_name" : f_name.get(),
                  "l_name" : l_name.get(),
                  "address" : address.get(),
                  "city" : city.get(),
                  "state" : state.get(),
                  "zipcode" : zipcode.get()
                  
                })


    #Commit changes
    conn.commit()

    #closing connection
    conn.close()
    
    #Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0,END)
    address.delete(0,END)
    state.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0,END)

#creating quering data base:

def query():
    # connect database:
    conn = sqlite3.connect("database/address_book.db")
    # creating Cursor:
    c = conn.cursor()
    #Query the database
    c.execute("SELECT oid,* FROM addresses") #oid give special id to each data fetch
    records = c.fetchall() # fetchone - give 1, fetchmany(50) -> 50 no.
    print_record = ''
    for record in records:
        print_record += str(record) + "\n"

    query_label = Label(root, text = print_record)
    query_label.grid(row = 8, column = 0, columnspan = 2)
    
                        
#Creating Entry place : for GUI

f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20, pady = 3)

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1, pady = 3)

address = Entry(root, width = 30)
address.grid(row = 2, column = 1, pady = 3)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1, pady = 3)

state = Entry(root, width = 30)
state.grid(row = 4, column = 1, pady = 3)

zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1, pady = 3)

# Creating Text Box :

f_name_label = Label(root, text = " First Name").grid(row = 0, column = 0)
l_name_label = Label(root, text = " Last Name").grid(row = 1, column = 0)
address_label = Label(root, text ="Address").grid(row = 2, column = 0)
city_label = Label(root, text = "City").grid(row = 3, column = 0)
state_label = Label(root, text = "State").grid(row = 4, column = 0)
zipcode_label = Label(root,text = "Zipcode").grid(row = 5, column = 0)

# creating Submit Button:
sub_btn = Button(root, text = "Submit", command = submit)
sub_btn.grid(row = 6, column = 0, columnspan = 2, pady = 20, padx = 10, ipadx = 100) 

query_btn = Button(root, text = "Query", command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 20, padx = 10, ipadx = 100) 

root.mainloop()
