from tkinter import *
# importing the module
import json

import pyodbc
def Deserrr():
    # creating the JSON data as a string
    #data = '{"Name" : "Romy", "Gender" : "Female"}'
    xfile = open('2021semA.json', encoding="utf8")
    s = xfile.read().encode('utf-8')
    data = json.loads(s)
    #print(data)
    output.insert()
    for k in data:
        output.insert(END, '{} = {}\n'.format(k,data[k]))
    output.config(state = DISABLED)

def Read():
    print("Read")
    output.delete(0.0, END)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Nathalie_Library.dbo.authors')
    for row in cursor:
        print(f'row = {row}')
        output.insert(END, row)
    output.insert(END, "\n")

    # print()


def close_window():
    window.destroy()
    exit()


# create a Form
window = Tk()
window.title("Comunication LTD")
window.configure(background="black")

# create a text box
output = Text(window, width=90, height=6, wrap=WORD, background="white")
output.grid(row=3, column=0, columnspan=2, sticky=W)

# add a submit button
Button(window, text="SUBMIT", width=6, command=Read).grid(row=5, column=0, sticky=W)
Button(window, text="JsonLoad", width=6, command=Deserrr).grid(row=6, column=0, sticky=W)

# create a button
Button(window, text="EXIT", width=6, command=close_window).grid(row=7, column=0, sticky=W)

# create a button
Button(window, text="Add customer", width=6, command=close_window).grid(row=8, column=0, sticky=W)
# SQLEXPRESS;

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=TWS\SQLEXPRESS;'
    'Database=Nathalie_Library;'
    'Trusted_Connection=yes;')

window.mainloop()
