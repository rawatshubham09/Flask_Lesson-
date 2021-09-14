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

#update function which update edit data
def update():
    #connecting database
    conn = sqlite3.connect("database/address_book.db")

    # 2) Creat cursor :-
    c = conn.cursor()

    record_id = dele.get()
    #update selected record
    c.execute("""UPDATE addresses SET
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode  WHERE oid = :oid""",
              {
                'first': f_name_ed.get(),
                'last': l_name_ed.get(),
                'address': address_ed.get(),
                'city': city_ed.get(),
                'state': state_ed.get(),
                'zipcode': zipcode_ed.get(),
                'oid': record_id
                  })


    #Commit changes
    conn.commit()

    #closing connection
    conn.close()

    editor.destroy()

def edit():
   
    #creating new window:
    global editor
    editor = Tk()
    editor.title("Edit Data")
    editor.iconbitmap(r'icons/light_icon.ico')
    
    # connect to the database:
    conn = sqlite3.connect("database/address_book.db")
    # creating Cursor--
    c = conn.cursor()

    record_id = dele.get()
    #Query to the database
    c.execute("SELECT oid,* FROM addresses WHERE oid =" + record_id)
    records = c.fetchall()

    
    #creat global vairable--
    global f_name_ed
    global l_name_ed
    global address_ed
    global city_ed
    global state_ed
    global zipcode_ed

    # Creating Text Boxes :

    f_name_label_ed = Label(editor, text = " First Name").grid(row = 0, column = 0)
    
    l_name_label_ed = Label(editor, text = " Last Name").grid(row = 1, column = 0)

    address_label_ed = Label(editor, text ="Address").grid(row = 2, column = 0)

    city_label_ed = Label(editor, text = "City").grid(row = 3, column = 0)

    state_label_ed = Label(editor, text = "State").grid(row = 4, column = 0)

    zipcode_label_ed = Label(editor,text = "Zipcode").grid(row = 5, column = 0)  
    

                            
    #Creating Entry place : for GUI

    f_name_ed = Entry(editor, width = 30)
    f_name_ed.grid(row = 0, column = 1, padx = 20, pady = (5,3))

    l_name_ed = Entry(editor, width = 30)
    l_name_ed.grid(row = 1, column = 1, pady = 3)

    address_ed = Entry(editor, width = 30)
    address_ed.grid(row = 2, column = 1, pady = 3)

    city_ed = Entry(editor, width = 30)
    city_ed.grid(row = 3, column = 1, pady = 3)

    state_ed = Entry(editor, width = 30)
    state_ed.grid(row = 4, column = 1, pady = 3)

    zipcode_ed = Entry(editor, width = 30)
    zipcode_ed.grid(row = 5, column = 1, pady = 3)

    #loop for results--
    for record in records:
        f_name_ed.insert(0, record[1])
        l_name_ed.insert(0, record[2])
        address_ed.insert(0, record[3])
        city_ed.insert(0, record[4])
        state_ed.insert(0, record[5])
        zipcode_ed.insert(0, record[6])

    # creating Submit Button:
    sub_btn = Button(editor, text = "Submit", command = update)
    sub_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100) 

    

# Delete a record:

def delete():
    #connecting database
    conn = sqlite3.connect("database/address_book.db")

    # 2) Creat cursor :-
    c = conn.cursor()

    place = dele.get()

    #delete a record
    c.execute("DELETE FROM addresses WHERE oid =" + place)

    #commit
    conn.commit()

    #close connection
    conn.close()

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
    for record in records :
        print_record += str(record[0]) + "\t " + str(record[1]) + " " + str(record[2])+ "\n"

    query_label = Label(root, text = print_record)
    query_label.grid(row = 11, column = 0, columnspan = 2)


    
                        
#Creating Entry place : for GUI

f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20, pady = (5,3))

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

dele = Entry(root, width = 30)
dele.grid(row = 8, column = 1, pady = 6)

# Creating Text Box :

f_name_label = Label(root, text = " First Name").grid(row = 0, column = 0)
l_name_label = Label(root, text = " Last Name").grid(row = 1, column = 0)
address_label = Label(root, text ="Address").grid(row = 2, column = 0)
city_label = Label(root, text = "City").grid(row = 3, column = 0)
state_label = Label(root, text = "State").grid(row = 4, column = 0)
zipcode_label = Label(root,text = "Zipcode").grid(row = 5, column = 0)
dele_label = Label(root, text = "Select ID").grid(row = 8, column = 0, pady = 6)

# creating Submit Button:
sub_btn = Button(root, text = "Submit", command = submit)
sub_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100) 

query_btn = Button(root, text = "Record", command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100) 

#create delete button
delete_btn = Button(root, text = "Delete", command = delete)
delete_btn.grid(row = 9, column = 0, columnspan = 2, pady = 20, padx = 10, ipadx = 100)

#create an update button:
edit_btn = Button(root, text = "EDIT Data", command = edit)
edit_btn.grid(row = 10, column = 0, columnspan = 2, pady = 20, padx = 10, ipadx = 100)

root.mainloop()
