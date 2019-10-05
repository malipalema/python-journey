# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 06:55:20 2019

@author: Pale
"""

import sqlite3
#backend
def customer_info():
    con=sqlite3.connect("customer.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS customer(id INTEGER PRIMARY KEY, customerid text,firstname text,surname text,dob text,age text,gender text,mobilephone text,address text,orderid text,ordername text,quantity text,ordertype text,employeeid text,shippingid text,shipaddress text,ddate text) ")
    con.commit()
    con.close()
   
    
def addData(customerid, firstname, surname, dob, age, gender, mobilephone, address, orderid, ordername, quantity, ordertype, employeeid,shippingid, shipaddress, ddate):
    con=sqlite3.connect("customer.db")
    cur=con.cursor()
    cur.execute("INSERT INTO custormer VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",customerid, firstname, surname, dob, age, gender, mobilephone, address, orderid, ordername, quantity, ordertype, employeeid,shippingid, shipaddress, ddate)
    con.commit()
    con.close()
    
def displayData():
    con=sqlite3.connect("customer.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM customer")
    rows=cur.fetchall
    con.close
    return rows


