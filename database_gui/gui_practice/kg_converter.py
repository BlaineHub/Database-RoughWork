from tkinter import *

window=Tk()

def conv_kg():
    lbs = int(v1_value.get())*2.2222
    t1.delete("1.0", END)
    t1.insert(END,lbs)
    ounces = int(v1_value.get())*35.2222
    t2.delete("1.0", END)
    t2.insert(END,ounces)
    grams = int(v1_value.get())*1000.0000
    t3.delete("1.0", END)
    t3.insert(END,grams)


b1=Button(window,text='convert',command=conv_kg)
b1.grid(row=0,column=2)

v1_value=StringVar()

e1 = Label(window,text='Kg')
e1.grid(row=0,column=0)
e2 = Entry(window,textvariable=v1_value)
e2.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=2)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=3)

window.mainloop()