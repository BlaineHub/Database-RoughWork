'''
A Program that stores book information:
Title, Author, 
Year, ISBN

User Can:
View all records
search all entrys
add entry
update entry
delete
close
'''

from asyncio.windows_events import NULL
from errno import ENODATA
from tkinter import *
from backend import Database

database = Database('main_project/oop/books.db')

class Window(object):

    def __init__(self,window):

        self.window=window
        self.window.wm_title('Book Store')

        self.v1=StringVar()
        self.v2=StringVar()
        self.v3=StringVar()
        self.v4=StringVar()

        l1=Label(window,text='Title')
        l1.grid(row=0,column=0)
        self.e1=Entry(window,textvariable=self.v1)
        self.e1.grid(row=0,column=1)

        l2=Label(window,text='Year')
        l2.grid(row=1,column=0)
        self.e2=Entry(window,textvariable=self.v2)
        self.e2.grid(row=1,column=1)

        l3=Label(window,text='Author')
        l3.grid(row=0,column=2)
        self.e3=Entry(window,textvariable=self.v3)
        self.e3.grid(row=0,column=3)

        l4=Label(window,text='ISBN')
        l4.grid(row=1,column=2)
        self.e4=Entry(window,textvariable=self.v4)
        self.e4.grid(row=1,column=3)

        self.list1 = Listbox(window, height=8,width=40)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=3)

        sb1 = Scrollbar(window)
        sb1.grid(row=1,column=3,rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

        b1=Button(window,text='View All',width=12,command=self.view_command)
        b1.grid(row=2,column=4)

        b2=Button(window,text='Search Entry',width=12,command=self.search_command)
        b2.grid(row=3,column=4)

        b3=Button(window,text='Add Entry',width=12,command=self.add_command)
        b3.grid(row=4,column=4)

        b4=Button(window,text='Update',width=12,command=self.update_command)
        b4.grid(row=5,column=4)

        b5=Button(window,text='Delete',width=12,command=self.delete_command)
        b5.grid(row=6,column=4)

        b6=Button(window,text='Close',width=12,command=window.destroy)
        b6.grid(row=7,column=4)



    def get_selected_row(self,event):
        try:
            x=self.list1.curselection()
            self.selected_tuple=self.list1.get(x)
            self.e1.delete(0,END)
            self.e1.insert(END, self.selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END, self.selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END, self.selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END, self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0,END)
        for x in database.view():
            self.list1.insert(END,x)
    

    def search_command(self):
        self.list1.delete(0,END)
        for x in database.search(self.v1.get(),self.v2.get(),self.v3.get(),self.v4.get()):
            self.list1.insert(END,x)


    def add_command(self):
        database.insert(self.v1.get(),self.v2.get(),self.v3.get(),self.v4.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.v1.get(), self.v2.get(), self.v3.get(), self.v4.get()))


    def update_command(self):
        database.update(self.selected_tuple[0],self.v1.get(), self.v2.get(), self.v3.get(), self.v4.get())
 

    def delete_command(self):
        database.delete(self.selected_tuple[0])


window=Tk()
Window(window)
window.mainloop()

