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
root.geometry("600x450")


# DataBase

# 1) creat darabase :-

conn = sqlite3.connect("address_book.db")

# 2) Creat cursor :-
c = conn.cursor()

# 3) Creat Table :-

c.execute(""" CREATE TABLE addresses(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer)
    """)

#Commit changes
conn.commit()

#closing connection
conn.close()



root.mainloop()
