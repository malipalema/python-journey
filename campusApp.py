# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:47:23 2019

@author: Pale
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 13:41:03 2019

@author: Pale
"""
from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import sys,random
import time
import datetime
import campusdatabase

def main():
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
        self.app=Goodsmanagement(self.goodswindow)
        
        
class Goodsmanagement:
    def __init__(self,master):
        self.master=master
        self.master.title("Campus Goods Billing System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg='cadet blue')
        self.frame= Frame(self.master,bg='cadet blue')
        self.frame.pack()
        #=====================frame===================================================================================        
        self.ABC=LabelFrame(self.frame,bg="powder blue",bd=20,relief=RIDGE)
        self.ABC.grid()
        
        self.ABC1=LabelFrame(self.frame,bg="powder blue",bd=10,relief=RIDGE)
        self.ABC1.grid(row=0,column=0,columnspan=4,sticky=W)
        
        self.ABC2=LabelFrame(self.frame,bg="powder blue",bd=10,relief=RIDGE)
        self.ABC2.grid(row=1,column=0,sticky=W)
        
        self.ABC3=LabelFrame(self.frame,bg="powder blue",bd=10,relief=RIDGE)
        self.ABC3.grid(row=1,column=1,sticky=W)
        
        self.ABC4=LabelFrame(self.frame,bg="powder blue",bd=10,relief=RIDGE)
        self.ABC4.grid(row=1,column=2,sticky=W)
        
        self.ABC5=LabelFrame(self.frame,bg="powder blue",bd=10,relief=RIDGE)
        self.ABC5.grid(row=1,column=3,sticky=W)
        
        self.ABC6=LabelFrame(self.frame,bg="powder blue",bd=10,relief=RIDGE)
        self.ABC6.grid(row=2,column=3,columnspan=4,sticky=W)
        #=================variables=======================================================================================
        self.Date1=StringVar()
        self.Time1=StringVar()
        self.Receipt_ref=StringVar()
        self.Tax=StringVar()
        self.Total=StringVar()
        
        customerid=StringVar()
        firstname=StringVar()
        surname=StringVar()
        dob=StringVar()
        age=StringVar()
        gender=StringVar()
        mobilephone=StringVar()
        address=StringVar()
        
        orderid=StringVar()
        ordername=StringVar()
        quantity=StringVar()
        ordertype=StringVar()
        employeeid=StringVar()
        shippingid=StringVar()
        shipaddress=StringVar()
        ddate=StringVar()
        
        
        #=================date and time=======================================================================================
        self.Date1.set(time.strftime("%d/%m/%Y"))
        self.Time1.set(time.strftime("%H:%M:%S"))
        #======================================================================================================================
        def iExit():
            self.iExit=tkinter.messagebox.askyesno("Campus goods billing system","Confirm if you want to exit")
            if self.iExit>0:
                self.destroy()
                return
            
        def Displayx():
            #txtReceipt.delete(0,END)
            for row in campusdatabase.displayData():
            
                txtReceipt.insert(END,row,str(""))
            
        def AddData():
            if(len(customerid.get())!=0):
                campusdatabase.addData(customerid.get(),firstname.get(),surname.get(),dob.get(),age.get(),\
                                       gender.get(),mobilephone.get(),address.get(),orderid.get(),ordername.get(),\
                                       quantity.get(),ordertype.get(),employeeid.get(),shippingid.get(),\
                                       shipaddress.get(),ddate.get())
                txtReceipt.delete(0,END)
                txtReceipt.insert(END,(customerid.get(),firstname.get(),surname.get(),dob.get(),age.get(),\
                                       gender.get(),mobilephone.get(),address.get(),orderid.get(),ordername.get(),\
                                       quantity.get(),ordertype.get(),employeeid.get(),shippingid.get(),\
                                       shipaddress.get(),ddate.get()))
   
        
        #======================================================================================================================
        self.lblDate=Label(self.ABC1,textvariable=self.Date1,font=('arial',30,'bold'),padx=22,pady=9,
                      bg="cadet blue",fg="cornsilk",justify=CENTER).grid(row=0,column=0)
        
        
        self.lblTitle=Label(self.ABC1,text="\tCustomer Trading Information\t",font=('arial',30,'bold'),padx=9,pady=9,
                      bg="cadet blue",fg="cornsilk").grid(row=0,column=1)
        
        
        self.lblTime=Label(self.ABC1,textvariable=self.Time1,font=('arial',30,'bold'),padx=9,pady=9,
                      bg="cadet blue",fg="cornsilk",justify=CENTER).grid(row=0,column=2)
        #======================================================================================================================
        self.lblcustomer=Label(self.ABC2,text="Customer details",font=('arial',20,'bold'),pady=1,bd=8,bg="cadet blue",
                           fg="Cornsilk",width=25,justify=CENTER).grid(row=0,column=0,columnspan=4)
        self.lblcustomerid=Label(self.ABC2,text="Customer ID",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=1,column=0,sticky=W)
        self.lblfirtstname=Label(self.ABC2,text="First name",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=2,column=0,sticky=W)
        self.lblsurname=Label(self.ABC2,text="Last name",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=3,column=0,sticky=W)
        self.lbldob=Label(self.ABC2,text="Date of birth",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=4,column=0,sticky=W)
        self.lblage=Label(self.ABC2,text="Age",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=6,column=0,sticky=W)
        self.lblgender=Label(self.ABC2,text="Gender",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=7,column=0,sticky=W)
        self.lblmobilephone=Label(self.ABC2,text="Mobile Phone",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=8,column=0,sticky=W)
        self.lbladdress=Label(self.ABC2,text="Address",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=9,column=0,sticky=W)
        #======================================================================================================================
        self.txtcustomerid=Entry(self.ABC2,textvariable=customerid,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=1,column=1,pady=1)
        self.txtfirstname=Entry(self.ABC2,textvariable=firstname,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=2,column=1,pady=1)
        self.txtsurname=Entry(self.ABC2,textvariable=surname,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=3,column=1,pady=1)
        self.txtdob=Entry(self.ABC2,textvariable=dob,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=4,column=1,pady=1)
        self.lblcustomerd=Label(self.ABC2,text="Customer details",font=('arial',20,'bold'),pady=1,bd=8,bg="cadet blue",
                           fg="Cornsilk",width=25,justify=CENTER).grid(row=5,column=0,columnspan=4)
        self.txtage=Entry(self.ABC2,textvariable=age,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=6,column=1,pady=1)
        self.txtPgender=Entry(self.ABC2,textvariable=gender,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=7,column=1,pady=1)
        
        self.txtmobilephone=Entry(self.ABC2,textvariable=mobilephone,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=8,column=1,pady=1)
        self.txtaddress=Entry(self.ABC2,textvariable=address,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=9,column=1,pady=1)
        
        
        #======================================================================================================================
        #======================================================================================================================
        self.lblorderdetails=Label(self.ABC3,text="Order details",font=('arial',20,'bold'),pady=1,bd=8,bg="cadet blue",
                           fg="Cornsilk",width=25,justify=CENTER).grid(row=0,column=0,columnspan=4)
        self.lblorderid=Label(self.ABC3,text="Order ID",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=1,column=0,sticky=W)
        self.lblordername=Label(self.ABC3,text="Order name",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=2,column=0,sticky=W)
        self.lblquantity=Label(self.ABC3,text="Quantity",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=3,column=0,sticky=W)
        self.lblordertype=Label(self.ABC3,text="Order Type",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=4,column=0,sticky=W)
        self.lblemployeeid=Label(self.ABC3,text="Employee ID",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=6,column=0,sticky=W)
        self.lblshippingid=Label(self.ABC3,text="Shipping ID",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=7,column=0,sticky=W)
        self.lblshipaddress=Label(self.ABC3,text="Shipping address",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=8,column=0,sticky=W)
        self.lblddate=Label(self.ABC3,text="Delivery date",bg="powder blue",
                           font=('arial',18,'bold'),justify=LEFT).grid(row=9,column=0,sticky=W)
        #======================================================================================================================
        self.txtorderid=Entry(self.ABC3,textvariable=orderid,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=1,column=1,pady=1)
        self.txtordername=Entry(self.ABC3,textvariable=ordername,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=2,column=1,pady=1)
        self.txtquantity=Entry(self.ABC3,textvariable=quantity,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=3,column=1,pady=1)
        self.txtordertype=Entry(self.ABC3,textvariable=ordertype,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=4,column=1,pady=1)
        self.lblorder=Label(self.ABC3,text="Order Details",font=('arial',20,'bold'),pady=1,bd=8,bg="cadet blue",
                           fg="Cornsilk",width=25,justify=CENTER).grid(row=5,column=0,columnspan=4)
        self.txtemployeeid=Entry(self.ABC3,textvariable=employeeid,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=6,column=1,pady=1)
        self.txtshippingid=Entry(self.ABC3,textvariable=shippingid,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=7,column=1,pady=1)
        
        self.txtshipaddress=Entry(self.ABC3,textvariable=shipaddress,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=8,column=1,pady=1)
        self.txtaddress=Entry(self.ABC3,textvariable=ddate,font=('arial',18,'bold'),bd=8,bg="powder blue",
                           fg="black",width=12,justify=CENTER).grid(row=9,column=1,pady=1)
        #======================================================================================================================
        self.txtReceipt=Text(self.ABC5,height=30,width=51,bd=20,font=('arial',9,'bold'))
        self.txtReceipt.grid(row=0,column=0)
        #======================================================================================================================
        self.btnTotal=Button(self.ABC6,padx=15,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=7,bg="powder blue",
                        text="Display",command=Displayx).grid(row=0,column=0)
        self.btnAdddata=Button(self.ABC6,padx=15,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=7,bg="powder blue",
                        text="Add data",command=AddData).grid(row=0,column=1)
        self.btnExit=Button(self.ABC6,padx=15,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=7,bg="powder blue",
                        text="Exit",command=iExit).grid(row=0,column=2)
        #======================================================================================================================
        
        root.mainloop()
                
        #==============================================================================================================
        
        
if __name__ =="__main__":
    main()
