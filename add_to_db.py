import sqlite3
import tkinter.messagebox
from tkinter import *



conn = sqlite3.connect('E:\Store Management System\Database\store.db')
cursor = conn.cursor()

result = cursor.execute("SELECT Max(id) from inventory")
for r in result:
    id = r[0]

class Database:
    def __init__(self,master,*args,**kwargs):
        self.master = master
        self.heading = Label(master,text = "Add to the database",font=('arial 35 bold'),fg='steelblue')
        self.heading.place(x=400,y=0)

        # labels and entries for windows
        self.name_l = Label(master,text="Enter Product Name",font = ('arial 18 bold'))
        self.name_l.place(x=10,y=70)

        self.stock_l = Label(master, text="Enter Stocks", font=('arial 18 bold'))
        self.stock_l.place(x=10, y=120)

        self.cp_l = Label(master, text="Enter Cost Price", font=('arial 18 bold'))
        self.cp_l.place(x=10, y=170)

        self.sp_l = Label(master, text="Enter Selling Price", font=('arial 18 bold'))
        self.sp_l.place(x=10, y=220)

        self.vendor_l = Label(master, text="Enter Vendor Name", font=('arial 18 bold'))
        self.vendor_l.place(x=10, y=270)

        self.id_l = Label(master, text="Enter Product Id", font=('arial 18 bold'))
        self.id_l.place(x=10, y=320)

        #entries for the labels
        self.name_e = Entry(master,width=25,font='arial 18 bold')
        self.name_e.place(x=300,y=70)

        self.stock_e = Entry(master, width=25, font='arial 18 bold')
        self.stock_e.place(x=300, y=120)


        self.cp_e = Entry(master, width=25, font='arial 18 bold')
        self.cp_e.place(x=300, y=170)

        self.sp_e = Entry(master, width=25, font='arial 18 bold')
        self.sp_e.place(x=300, y=220)

        self.vendor_e = Entry(master, width=25, font='arial 18 bold')
        self.vendor_e.place(x=300, y=270)

        self.id_e = Entry(master, width=25, font='arial 18 bold')
        self.id_e.place(x=300, y=320)

        #button to add to the database
        self.btn_add = Button(master,text="Add To Database",command = self.clicked,font=("arial 12 bold"),width=18,height=2,bg='steelblue',fg='white')
        self.btn_add.place(x=350,y=420)

        #button to clear all the labels
        self.btn_clear = Button(master,text="Clear all the fields",command=self.clear,width=18,height=2,font=("arial 12 bold"),bg='red',fg='white')
        self.btn_clear.place(x=100,y=420)

        self.btn_home = Button(master,text="Home",command=self.home,width=20,height=2,font=("arial 12 bold"),bg='steelblue',fg='white')
        self.btn_home.place(x=175,y=550)


        #text box for the logs
        self.tBox = Text(master,width=50,height=16)
        self.tBox.place(x=750,y=67)
        self.tBox.insert(END,"Id has reached upto: "+ str(id))




    def clicked(self,*args,**kwargs):
        #get from entries
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()

        if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '':
            tkinter.messagebox.showinfo("Error","Please Fill all the entries.")
        else:
            self.totalcp = float(self.cp) * float(self.stock)
            self.totalsp = float(self.sp) * float(self.stock)
            self.profit = float(self.totalsp - self.totalcp)
            sql = "INSERT INTO inventory (name,stock,cp,sp,totalcp,totalsp,profit,vendor)VALUES(?,?,?,?,?,?,?,?)"
            cursor.execute(sql,(self.name,self.stock,self.cp,self.sp,self.totalcp,self.totalsp,self.profit,self.vendor))
            conn.commit()
            conn.close()
            #textbox insert
            self.tBox.insert(END,"\n\n"+str(self.name) + " is inserted into the database with code "+str(self.id_e.get()))

            tkinter.messagebox.showinfo("Success","Data recorded successfully")


    def clear(self,*args,**kwargs):
        self.name_e.delete(0,END)
        self.stock_e.delete(0,END)
        self.cp_e.delete(0,END)
        self.sp_e.delete(0,END)
        self.vendor_e.delete(0,END)
        self.id_e.delete(0,END)


    #def home(self,*args,**kwargs):
        #import combined

def add():
    root = Tk()
    b = Database(root)
    root.geometry("1366x768+0+0")
    root.title("Add to the database")
    root.mainloop()




