from tkinter import *
import sqlite3
import tkinter.messagebox


conn = sqlite3.connect("E:\Store Management System\Database\store.db")
cursor = conn.cursor()

result = cursor.execute("SELECT Max(id) from inventory")
for r in result:
    id = r[0]

class Database:
    def __init__(self,master,*args,**kwargs):
        self.master = master
        self.heading = Label(master,text = "Update the records of Product items",font=('arial 32 bold'),fg='steelblue')
        self.heading.place(x=320,y=0)

        #labels and entry for id
        self.id_le = Label(master,text= "Enter Product's Id",font=('arial 18 bold'))
        self.id_le.place(x=10,y=70)

        self.id_e = Entry(master, width=10, font='arial 17 bold')
        self.id_e.place(x=400, y=70)

        #search button
        self.btn_search = Button(master,text="Search",command=self.search,width=15,height=2,bg='orange')
        self.btn_search.place(x=570,y=65)

        # labels and entries for windows
        self.name_l = Label(master,text="Enter Product Name",font = ('arial 18 bold'))
        self.name_l.place(x=10,y=120)

        self.stock_l = Label(master, text="Enter Stocks", font=('arial 18 bold'))
        self.stock_l.place(x=10, y=170)

        self.cp_l = Label(master, text="Enter Cost Price", font=('arial 18 bold'))
        self.cp_l.place(x=10, y=220)

        self.sp_l = Label(master, text="Enter Selling Price", font=('arial 18 bold'))
        self.sp_l.place(x=10, y=270)

        self.totalcp_l = Label(master, text="Enter Total Cost Price", font=('arial 18 bold'))
        self.totalcp_l.place(x=10, y=320)

        self.totalsp_l = Label(master, text="Enter Total Selling Price", font=('arial 18 bold'))
        self.totalsp_l.place(x=10, y=370)

        self.vendor_l = Label(master, text="Enter Vendor Name", font=('arial 18 bold'))
        self.vendor_l.place(x=10, y=420)


        #entries for the labels
        self.name_e = Entry(master,width=25,font='arial 18 bold')
        self.name_e.place(x=300,y=120)

        self.stock_e = Entry(master, width=25, font='arial 18 bold')
        self.stock_e.place(x=300, y=170)

        self.cp_e = Entry(master, width=25, font='arial 18 bold')
        self.cp_e.place(x=300, y=220)

        self.sp_e = Entry(master, width=25, font='arial 18 bold')
        self.sp_e.place(x=300, y=270)

        self.totalcp_e = Entry(master, width=25, font='arial 18 bold')
        self.totalcp_e.place(x=300, y=320)

        self.totalsp_e = Entry(master, width=25, font='arial 18 bold')
        self.totalsp_e.place(x=300, y=370)

        self.vendor_e = Entry(master, width=25, font='arial 18 bold')
        self.vendor_e.place(x=300, y=420)

        #button to add to the database
        self.btn_add = Button(master,text="Update Database",command=self.update,font=("arial 12 bold"),width=18,height=2,bg='steelblue',fg='white')
        self.btn_add.place(x=350,y=520)

        #button to clear all the labels
        self.btn_clear = Button(master,text="Clear all the fields",width=18,command=self.clear,height=2,font=("arial 12 bold"),bg='red',fg='white')
        self.btn_clear.place(x=100,y=520)

        #text box for the logs
        self.tBox = Text(master,width=50,height=16)
        self.tBox.place(x=750,y=67)
        self.tBox.insert(END,"Id has reached upto: "+ str(id))

    def search(self,*args,**kwargs):
        sql = "SELECT * FROM inventory WHERE id=?"
        result = cursor.execute(sql,(self.id_e.get(), ))

        for r in result:
            self.n1 = r[1]  # name
            self.n2 = r[2]  # stock
            self.n3 = r[3]  # cp
            self.n4 = r[4]  # sp
            self.n5 = r[5]  # totalcp
            self.n6 = r[6]  # totalsp
            self.n7 = r[7]  # profit
            self.n8 = r[8]  # vendor
        conn.commit()


        #insert into the entries to update
        self.name_e.delete(0,END)
        self.name_e.insert(0,str(self.n1))

        self.stock_e.delete(0, END)
        self.stock_e.insert(0, str(self.n2))

        self.cp_e.delete(0, END)
        self.cp_e.insert(0, str(self.n3))

        self.sp_e.delete(0, END)
        self.sp_e.insert(0, str(self.n4))

        self.totalcp_e.delete(0, END)
        self.totalcp_e.insert(0, str(self.n5))

        self.totalsp_e.delete(0, END)
        self.totalsp_e.insert(0, str(self.n6))

        self.vendor_e.delete(0, END)
        self.vendor_e.insert(0, str(self.n8))

    def update(self,*args,**kwargs):
        #get all the updated values

        self.u1 = self.name_e.get()
        self.u2 = self.stock_e.get()
        self.u3 = self.cp_e.get()
        self.u4 = self.sp_e.get()
        self.u5 = self.totalcp_e.get()
        self.u6 = self.totalsp_e.get()
        self.u7 = self.vendor_e.get()

        query = "UPDATE inventory SET name=?, stock=?, cp=?, sp=?, totalcp=?, totalsp=?, vendor=? WHERE id=?"
        cursor.execute(query,(self.u1,self.u2,self.u3,self.u4,self.u5,self.u6,self.u7,self.id_e.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success","Updated the Product's information")

    def clear(self, *args, **kwargs):
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.totalcp_e.delete(0,END)
        self.totalsp_e.delete(0,END)




root = Tk()
b = Database(root)

root.geometry("1366x768+0+0")
root.title("Update the records of Product items")
root.mainloop()


import add_to_db

