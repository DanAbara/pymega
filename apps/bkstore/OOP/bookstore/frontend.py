"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:

View all records
Search an entry
Add entry
Update entr
Delete
Close program

"""
import tkinter as tk
from backend import Database # importing the Database class from the backend.py script

database=Database() # create an object called database from the Database class

class Commands():

    def __init__(self):
        pass

    def get_selected_row(self,event): # the event parameter is a flag to highlight that this function is binded to an event and is necessary.
        #global selected_tuple
        index=list1.curselection()[0] # get the index of the selected row in the listbox which is a tuple. The [0] extracts just the number which is the first item in the tuple.
        self.selected_tuple=list1.get(index) # from the listbox, retrieve the row which corresponds to the obtained index from the event of clicking.
        e1.delete(0,tk.END) # clear e1
        e1.insert(tk.END,self.selected_tuple[1]) # insert title when the row is selected
        e2.delete(0,tk.END) # clear e2
        e2.insert(tk.END,self.selected_tuple[2]) # insert author in author entry widget when row is selected
        e3.delete(0,tk.END) # clear e3
        e3.insert(tk.END,self.selected_tuple[3]) # insert year in year entry widget when row is selected
        e4.delete(0,tk.END) # clear e4
        e4.insert(tk.END,self.selected_tuple[4]) # insert isbn in isbn entry widget when rows is selected


    def view_command(self): # func to iterate on each tuple inside obtained list from backend
        list1.delete(0,tk.END) # delete from row 0 to the END each time to make sure when the button is pressed it first clears the current values in the listbox
        for row in database.view():
            list1.insert(tk.END,row) # put each tuple in the list as a row at the end of the listbox

    def search_command(self):
        list1.delete(0,tk.END)
        for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
            list1.insert(tk.END,row)

    def add_command(self):
        database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        list1.delete(0,tk.END)
        list1.insert(tk.END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())) # so that the values can show in the listbox for the user to know thd add was successful

    def delete_command(self):
        database.delete(self.selected_tuple[0]) # pass the first index (id) of the obtained tuple from get_selected_row()

    def update_command(self):
        database.update(self.selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

window=tk.Tk()
window.wm_title("BookStore") # set title
comm=Commands() # create an object of the Commands class

# define labels title, author, year, ISBN
l1=tk.Label(window,text="Title")
l1.grid(row=0,column=0)

l2=tk.Label(window,text="Author")
l2.grid(row=0,column=2)

l3=tk.Label(window,text="Year")
l3.grid(row=1,column=0)

l4=tk.Label(window,text="ISBN")
l4.grid(row=1,column=2)

# define entry using entry widgets
title_text=tk.StringVar() # specify data type for title entry
e1=tk.Entry(window, textvariable=title_text)
e1.grid(row=0,column=1)

author_text=tk.StringVar() # specify data type for title entry
e2=tk.Entry(window, textvariable=author_text)
e2.grid(row=0,column=3)

year_text=tk.StringVar() # specify data type for title entry
e3=tk.Entry(window, textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=tk.StringVar() # specify data type for title entry
e4=tk.Entry(window, textvariable=isbn_text)
e4.grid(row=1,column=3)

# define the list box
list1=tk.Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=7,columnspan=2)
list1.bind("<<ListboxSelect>>",comm.get_selected_row) # bind the listbox to an condition/action (a selection of an item on the listbox), and select an effect to be performed when the action is met.

# make a scrollbar for the listbox
sb1=tk.Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=7)

list1.configure(yscrollcommand=sb1.set) # set list1 to use scrollbar sb1 along y axis
sb1.configure(command=list1.yview) # set scrollbar command to be for vertical (y-axis) viewing of list1

# define the buttons
b1=tk.Button(window,text="View all",width=12,command=comm.view_command)
b1.grid(row=2,column=3)

b2=tk.Button(window,text="Search entry",width=12,command=comm.search_command)
b2.grid(row=3,column=3)

b3=tk.Button(window,text="Add entry",width=12,command=comm.add_command)
b3.grid(row=4,column=3)

b4=tk.Button(window,text="Update",width=12,command=comm.update_command)
b4.grid(row=5,column=3)

b5=tk.Button(window,text="Delete",width=12,command=comm.delete_command)
b5.grid(row=6,column=3)

b6=tk.Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
