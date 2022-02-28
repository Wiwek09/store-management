from tkinter import *
import sys
import tkinter.messagebox
import module
from add_to_db import add

class Database:
  def __init__(self, master, *args, **kwargs):
    self.master = master
    self.heading1 = Label(master, text="Home", font=('arial 34 bold'), fg='steelblue')
    self.heading1.place(x=575,y=10)
    self.heading2 = Label(master, text="Select Option", font=('arial 20 bold'), fg='Black')
    self.heading2.place(x=100, y=100)
    self.myButton1 = Button(master,text="Add new Product to information",command=self.click,font='arial 12 bold',width=30,height=2,bg='grey',fg='white')
    self.myButton1.place(x=200,y=175)
    self.myButton2 = Button(master,text="Updation of Product information",command=self.touch,font='arial 12 bold',width=30,height=2,bg='grey',fg='white')
    self.myButton2.place(x=200,y=250)
    self.myButton3 = Button(master,text = "See product information",command=self.seeinfo,font='arial 12 bold',width=30,height=2,bg='grey',fg='white')
    self.myButton3.place(x=200,y=325)
    self.myButton3 = Button(master, text="Billing", command=self.bill, font='arial 12 bold',width=30, height=2, bg='grey', fg='white')
    self.myButton3.place(x=200, y=400)



  def click(self):
    add()

  def touch(self):
    import update_db

  def seeinfo(self):
    return True

  def bill(self):
    import main




root = Tk()
b = Database(root)
root.geometry("1366x768+0+0")
root.title("Stock Center")
root.mainloop()