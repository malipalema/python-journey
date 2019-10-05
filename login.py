# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 13:41:03 2019

@author: Pale
"""
from tkinter import*
import tkinter.messagebox as tk
from tkinter import ttk
import sys,random
import time
import datetime
root=None
def main():
    global root
    root=Tk()
    app=Login(root)
   
class Login:
    def __init__(self,master):
        self.master=master
        self.master.title("Campus Goods Trading Platform")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg='cadet blue')
        self.frame= Frame(self.master,bg='cadet blue')
        self.frame.pack()
        
        self.Username=StringVar()
        self.Password=StringVar()
        
        self.lblTitle=Label(self.frame, text='Campus Goods Trading Platform', font=('arial',60,'bold'),
                            bg='cadet blue', fg='Cornsilk')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=20)
        #======================================================================================================
        self.LoginFrame1=LabelFrame(self.frame,width=1350,height=200
                                   ,text="Login",font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=40)
        self.LoginFrame1.grid(row=1,column=0)
        self.LoginFrame2=LabelFrame(self.frame,width=1000,height=200
                                   ,text="Log",font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=40)
        self.LoginFrame2.grid(row=2,column=0)
        #======================================================================================================
        self.lblUsername=Label(self.LoginFrame1,text="Username",font=('arial',30,'bold'),bd=22,
                               bg='cadet blue',fg='cornsilk')
        self.lblUsername.grid(row=0,column=0)
        
        self.txtUsername=Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=7,textvariable=self.Username,
                               width=33)
        self.txtUsername.grid(row=0,column=1,padx=88)
        
        self.lblPassword=Label(self.LoginFrame1,text="Password",font=('arial',30,'bold'),bd=22,
                               bg='cadet blue',fg='cornsilk')
        self.lblPassword.grid(row=1,column=0)
        
        self.txtPassword=Entry(self.LoginFrame1,font=('arial',30,'bold'),show='*',bd=7,textvariable=self.Password,
                               width=33)
        self.txtPassword.grid(row=1,column=1,columnspan=2,pady=30)
        #======================================================================================================        
        self.btnLogin=Button(self.LoginFrame2,text='Login',width=15,font=('arial',30,'bold'),
                             bg='cadet blue',fg='cornsilk',command=self.LoginSystem)
        self.btnLogin.grid(row=3,column=2,pady=20,padx=8)
        self.btnCancel=Button(self.LoginFrame2,text='Cancel',width=15,font=('arial',30,'bold'),
                             bg='cadet blue',fg='cornsilk',command=self.SystemCancel)
        self.btnCancel.grid(row=3,column=0,pady=20,padx=8)
        
        #======================================================================================================
    def LoginSystem(self):
        user=(self.Username.get())
        pas=(self.Password.get())
        if(user==str(1234) and pas==str(1234)):
            self.Loginwindow()
        else:
            tkinter.messagebox.askyesno("Campus Goods System","Invalid Login details")
            self.Username=set("")
            self.Password=set("")
            
    def SystemCancel(self):
        self.SystemCancel=tkinter.messagebox.askyesno("Campus Goods Trading System","Confirm if you want to exit")
        if self.SystemCancel>0:
            self.master.destroy()
            return
        
    def Loginwindow(self):
        self.goodswindow=Toplevel(self.master)
        self.app=Goodsmanagment(self.goodswindow)
        
        
class Goodsmanagment:
    def __init__(self,master):
        self.master=master
        self.master.title("Campus Goods Billing System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg='cadet blue')
        self.frame= Frame(self.master,bg='cadet blue')
        self.frame.pack()
        #=====================frame===================================================================================
        ABC=Frame(root,bg="powder blue",bd=20,relief=RIDGE)
        ABC.grid()
        
        ABC1=Frame(root,bg="powder blue",bd=10,relief=RIDGE)
        ABC1.grid(row=0,column=0,columnspan=4,sticky=W)
        
        ABC2=Frame(root,bg="powder blue",bd=10,relief=RIDGE)
        ABC2.grid(row=1,column=0,sticky=W)
        
        ABC3=Frame(root,bg="powder blue",bd=10,relief=RIDGE)
        ABC3.grid(row=1,column=1,sticky=W)
        
        ABC4=Frame(root,bg="powder blue",bd=10,relief=RIDGE)
        ABC4.grid(row=1,column=2,sticky=W)
        
        ABC5=Frame(root,bg="powder blue",bd=10,relief=RIDGE)
        ABC5.grid(row=0,column=0,sticky=W)
        
        ABC6=Frame(root,bg="powder blue",bd=10,relief=RIDGE)
        ABC6.grid(row=1,column=0,columnspan=4,sticky=W)
        
       ## self.LoginFrameA=LabelFrame(self.frame,width=1350,height=200
       ##                            ,text="Login",font=('arial',20,'bold'),relief='ridge',bg='powder blue',bd=40)
      ##  self.LoginFrameB.grid(row=1,column=0)
       ## self.LoginFrame2=LabelFrame(self.frame,width=1000,height=200
                          ##         ,text="Log",font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=40)
     ##   self.LoginFrame2.grid(row=2,column=0)
        lblDate=Label(ABC1,text="/tDate/t",font=('arial',30,'bold'),padx=9,pady=9,
                      bd=5,bg="cadet blue",fg="cornsilk",justify=CENTER).grid(row=0,column=0)
        
        
        lblDate=Label(ABC1,text="/tCampus Goods Billing System/t",font=('arial',30,'bold'),padx=9,pady=9,
                      bd=14,bg="cadet blue",fg="cornsilk",justify=CENTER).grid(row=0,column=1)
        
        
        lblDate=Label(ABC1,text="/tTime/t",font=('arial',30,'bold'),padx=9,pady=9,
                      bd=5,bg="cadet blue",fg="cornsilk",justify=CENTER).grid(row=0,column=2)
        root.mainloop()
        
        #==============================================================================================================
        
        
if __name__ =="__main__":
    main()
