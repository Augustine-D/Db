import tkinter as tk
import sqlite3

from matplotlib.pyplot import get

root = tk.Tk()
root.title('Database App')
root.geometry('400x400')

myLabel = tk.Label(root, text='Hello Welcome, Login').grid(
    column=1, row=0)
# database

# create a db or connect to one
conn = sqlite3.connect('addressbook.db')

# create a curseor to send it off into the db
c = conn.cursor()


'''
# create table
c.execute(""" CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)""")
'''


# create submit function


def submit():
    # create a db or connect to one
    conn = sqlite3.connect('addressbook.db')

    # create a curseor to send it off into the db
    c = conn.cursor()

   # insert into table
    c.execute("INSERT INTO addresses VALUES ( :f_name, :l_name, :address, :city, :state, : zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              }
              )

    # commit to db
    conn.commit()

    # close connection
    conn.close()

    # clear textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# create query function
def query():
    return


# Create fields
f_name = tk.Entry(root)
f_name.grid(column=1, row=1, pady=10, padx=10)

l_name = tk.Entry(root)
l_name.grid(column=1, row=3, pady=10, padx=10)

address = tk.Entry(root)
address.grid(column=1, row=5, pady=10, padx=10)

city = tk.Entry(root)
city.grid(column=1, row=7, pady=10, padx=10)

state = tk.Entry(root)
state.grid(column=1, row=9, pady=10, padx=10)

zipcode = tk.Entry(root)
zipcode.grid(column=1, row=11, pady=10, padx=10)

# Text box labels
fname_label = tk.Label(root, text='First Name')
fname_label.grid(column=1, row=2)

lname_label = tk.Label(root, text='Last Name')
lname_label.grid(column=1, row=4)

address_label = tk.Label(root, text='Address')
address_label.grid(column=1, row=6)

city_label = tk.Label(root, text='City')
city_label.grid(column=1, row=8)

state_label = tk.Label(root, text='State')
state_label.grid(column=1, row=10)

zipcode_label = tk.Label(root, text='Zipcode')
zipcode_label.grid(column=1, row=12)


# submit button
submit_btn = tk.Button(root, text='Add Record to Db',
                       command=submit).grid(column=1, row=15, pady=10, padx=10)


# query button
query_btn = tk.Button(root, text='Show Records', command=query).grid(
    column=1, row=13, ipadx=137)
# commit to db
conn.commit()

# close connection
conn.close()

root.mainloop()
