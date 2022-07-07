from asyncio.windows_events import NULL
from errno import ENODATA
from tkinter import *
from backend import Database

database = Database('books.db')

window=Tk()
window.wm_title('Book Store')

######entry and labels#######
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()

l1=Label(window,text='Title')
l1.grid(row=0,column=0)
e1=Entry(window,textvariable=v1)
e1.grid(row=0,column=1)

l2=Label(window,text='Year')
l2.grid(row=1,column=0)
e2=Entry(window,textvariable=v2)
e2.grid(row=1,column=1)

l3=Label(window,text='Author')
l3.grid(row=0,column=2)
e3=Entry(window,textvariable=v3)
e3.grid(row=0,column=3)

l4=Label(window,text='ISBN')
l4.grid(row=1,column=2)
e4=Entry(window,textvariable=v4)
e4.grid(row=1,column=3)

######list box & scrollbar#######

list1 = Listbox(window, height=8,width=40)
list1.grid(row=2,column=0,rowspan=6,columnspan=3)

sb1 = Scrollbar(window)
sb1.grid(row=1,column=3,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

def get_selected_row(event):
 try:
    global selected_tuple
    x=list1.curselection()
    selected_tuple=list1.get(x)
    e1.delete(0,END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END, selected_tuple[4])
 except IndexError:
     pass

list1.bind('<<ListboxSelect>>',get_selected_row)


######button configuration######

def view_command():
    list1.delete(0,END)
    for x in database.view():
        list1.insert(END,x)
b1=Button(window,text='View All',width=12,command=view_command)
b1.grid(row=2,column=4)

def search_command():
    list1.delete(0,END)
    for x in database.search(v1.get(),v2.get(),v3.get(),v4.get()):
        list1.insert(END,x)
b2=Button(window,text='Search Entry',width=12,command=search_command)
b2.grid(row=3,column=4)

def add_command():
    database.insert(v1.get(),v2.get(),v3.get(),v4.get())
    list1.delete(0,END)
    list1.insert(END,(v1.get(), v2.get(), v3.get(), v4.get()))
b3=Button(window,text='Add Entry',width=12,command=add_command)
b3.grid(row=4,column=4)

def update_command():
    database.update(selected_tuple[0],v1.get(), v2.get(), v3.get(), v4.get())
b4=Button(window,text='Update',width=12,command=update_command)
b4.grid(row=5,column=4)

def delete_command():
    database.delete(selected_tuple[0])
b5=Button(window,text='Delete',width=12,command=delete_command)
b5.grid(row=6,column=4)

b6=Button(window,text='Close',width=12,command=window.destroy)
b6.grid(row=7,column=4)


window.mainloop()