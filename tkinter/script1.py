import tkinter as tk

# create a window
window=tk.Tk()

def km_to_miles():
    print(e1_value.get())
    miles=float(e1_value.get())*1.606 # convert the value to miles
    t1.delete(1.0,tk.END) # to delete the contents before inserting new result
    t1.insert(tk.END,miles) # inserting the value obtained from the entry widget into the t1 widget.

b1=tk.Button(window,text="Execute", command=km_to_miles) # create a button
b1.grid(row=0,column=0) # display the button created in b1. May be b1.grid() or b1.pack()

e1_value=tk.StringVar() # create stringVar object to be pointed to.
e1=tk.Entry(window,textvariable=e1_value) # the input in the entry widget gets saved in a StringVar object in a variable e1_value
e1.grid(row=0,column=1)

t1=tk.Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop() # to make sure the window stays open and an X button appears at the top-right corner. Without this line, the app will close immediately after opening.
