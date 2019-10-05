# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 03:56:17 2019

@author: Pale
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 22:31:16 2019

@author: Pale
"""

from tkinter import*
import tkinter.messagebox as tk
from tkinter import ttk
import sys,random
import time
import datetime

root=Tk()
root.title("Goods Management")
root.geometry("1350x700+0+0")
root.config(bg='cadet blue')

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
ABC5.grid(row=1,column=3,sticky=W)

ABC6=Frame(root,bg="powder blue",bd=10,relief=RIDGE)
ABC6.grid(row=2,column=3,columnspan=4,sticky=W)
#=================variables=======================================================================================
Date1=StringVar()
Time1=StringVar()
Receipt_ref=StringVar()
Tax=StringVar()
Total=StringVar()

Litbooks=StringVar()
SciFibooks=StringVar()
Historybooks=StringVar()
Mythologybooks=StringVar()
Laptops=StringVar()
Powerbanks=StringVar()
Mobilephones=StringVar()
Desktops=StringVar()

Calculators=StringVar()
Stapels=StringVar()
Envelopes=StringVar()
Stickynotes=StringVar()
Tracksuits=StringVar()
Jerseys=StringVar()
Blazers=StringVar()
Trousers=StringVar()

Litbooks.set("0")
SciFibooks.set("0")
Historybooks.set("0")
Mythologybooks.set("0")
Laptops.set("0")
Powerbanks.set("0")
Mobilephones.set("0")
Desktops.set("0")

Calculators.set("0")
Stapels.set("0")
Envelopes.set("0")
Stickynotes.set("0")
Tracksuits.set("0")
Jerseys.set("0")
Blazers.set("0")
Trousers.set("0")

#=================date and time=======================================================================================
Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))
#======================================================================================================================
def iExit():
    iExit=tkinter.messagebox.askyesno("Campus goods billing system","Confirm if you want to exit")
    if iExit>0:
        root.destroy()
        return
    
def Total():
    Item1=float(Litbooks.get())
    Item2=float(SciFibooks.get())
    Item3=float(Historybooks.get())
    Item4=float(Mythologybooks.get())
    Item5=float(Laptops.get())
    Item6=float(Powerbanks.get())
    Item7=float(Mobilephones.get())
    Item8=float(Desktops.get())
    
    Item9=float(Calculators.get())
    Item10=float(Stapels.get())
    Item11=float(Envelopes.get())
    Item12=float(Stickynotes.get())
    Item13=float(Tracksuits.get())
    Item14=float(Jerseys.get())
    Item15=float(Blazers.get())
    Item16=float(Trousers.get())

    PriceofItem1=("$")+str('%.2f'%(Item1*32.99))
    PriceofItem2=("$")+str('%.2f'%(Item2*22.99))
    PriceofItem3=("$")+str('%.2f'%(Item3*24.99))
    PriceofItem4=("$")+str('%.2f'%(Item4*29.99))
    PriceofItem5=("$")+str('%.2f'%(Item5*349.99))
    PriceofItem6=("$")+str('%.2f'%(Item6*49.99))
    PriceofItem7=("$")+str('%.2f'%(Item7*299.99))
    PriceofItem8=("$")+str('%.2f'%(Item8*499.99))
    PriceofItem9=("$")+str('%.2f'%(Item9*14.99))
    PriceofItem10=("$")+str('%.2f'%(Item10*6.99))
    PriceofItem11=("$")+str('%.2f'%(Item11*3.99))
    PriceofItem12=("$")+str('%.2f'%(Item12*4.99))
    PriceofItem13=("$")+str('%.2f'%(Item13*34.99))
    PriceofItem14=("$")+str('%.2f'%(Item14*24.99))
    PriceofItem15=("$")+str('%.2f'%(Item15*14.99))
    PriceofItem16=("$")+str('%.2f'%(Item16*12.99))
    
    PriceofTextbooks=(Item1*32.99)+(Item2*22.99)+(Item3*24.99)+(Item4*29.99)
    PriceofElectronics= (Item5*349.99)+(Item6*49.99)+(Item7*299.99)+(Item8*499.99)
    PriceofStationery=(Item9*14.99)+(Item10*6.99)+(Item11*3.99)+(Item12*4.99)
    PriceofUniform=(Item13*34.99)+(Item14*24.99)+(Item15*14.99)+(Item16*12.99)
    
    SubTotal=("$")+str('%.2f'%(PriceofTextbooks+PriceofElectronics+PriceofStationery+PriceofUniform))
    iTax=("$")+str('%.2f'%((PriceofTextbooks+PriceofElectronics+PriceofStationery+PriceofUniform)*0.15))
    tt=(PriceofTextbooks+PriceofElectronics+PriceofStationery+PriceofUniform)
    tc=((PriceofTextbooks+PriceofElectronics+PriceofStationery+PriceofUniform)*0.15)
    TotalCost=("$")+str('%.2f'%(tt+tc))
    
    txtReceipt.delete("1.0",END)
    x=random.randint(10747,500298)
    randomRef=str(x)
    Receipt_ref.set("BILL"+randomref)
    txtReceipt.insert(END,'Receipt_ref:\t\t\t\t'+Receipt_ref.get()+'\n'+Date1.get()+'\t\t\t\t'+Time1.get()+"\n")
    txtReceipt.insert(END,'-----------------------------------------------------------------------------'+"\n")
    txtReceipt.insert(END,'Item \t\t\t\t'+"COST OF ITEMS:\n")
    txtReceipt.insert(END,'-----------------------------------------------------------------------------'+"\n")
    txtReceipt.insert(END,'Literature books \t\t\t\t'+PriceofItem1+"\n")
    txtReceipt.insert(END,'Sci-Fi books \t\t\t\t'+PriceofItem2+"\n")
    txtReceipt.insert(END,'History books \t\t\t\t'+PriceofItem3+"\n")
    txtReceipt.insert(END,'Mythology books \t\t\t\t'+PriceofItem4+"\n")
    txtReceipt.insert(END,'Laptops \t\t\t\t'+PriceofItem5+"\n")
    txtReceipt.insert(END,'Powerbanks \t\t\t\t'+PriceofItem6+"\n")
    txtReceipt.insert(END,'Mobile phones \t\t\t\t'+PriceofItem7+"\n")
    txtReceipt.insert(END,'Desktops \t\t\t\t'+PriceofItem8+"\n")
    txtReceipt.insert(END,'Calculators \t\t\t\t'+PriceofItem9+"\n")
    txtReceipt.insert(END,'Stapels \t\t\t\t'+PriceofItem10+"\n")
    txtReceipt.insert(END,'Envelopes \t\t\t\t'+PriceofItem11+"\n")
    txtReceipt.insert(END,'Sticky notes \t\t\t\t'+PriceofItem12+"\n")
    txtReceipt.insert(END,'Tracksuits \t\t\t\t'+PriceofItem13+"\n")
    txtReceipt.insert(END,'Jerseys \t\t\t\t'+PriceofItem14+"\n")
    txtReceipt.insert(END,'Blazers \t\t\t\t'+PriceofItem15+"\n")
    txtReceipt.insert(END,'Trousers \t\t\t\t'+PriceofItem16+"\n")
    txtReceipt.insert(END,'Tax \t\t\t\t'+iTax+"\n")
    txtReceipt.insert(END,'Subtotal \t\t\t\t'+SubToal+"\n")
    txtReceipt.insert(END,'Total cost \t\t\t\t'+TotalCost+"\n")


#======================================================================================================================


lblDate=Label(ABC1,textvariable=Date1,font=('arial',30,'bold'),padx=22,pady=9,
              bg="cadet blue",fg="cornsilk",justify=CENTER).grid(row=0,column=0)


lblTitle=Label(ABC1,text="\tCampus Goods Billing System\t",font=('arial',30,'bold'),padx=9,pady=9,
              bg="cadet blue",fg="cornsilk").grid(row=0,column=1)


lblTime=Label(ABC1,textvariable=Time1,font=('arial',30,'bold'),padx=9,pady=9,
              bg="cadet blue",fg="cornsilk",justify=CENTER).grid(row=0,column=2)
#======================================================================================================================
lblTextbooks=Label(ABC2,text="Textbooks",font=('arial',20,'bold'),pady=1,bd=8,bg="cadet blue",
                   fg="Cornsilk",width=25,justify=CENTER).grid(row=0,column=0,columnspan=4)
lblLitbooks=Label(ABC2,text="Literature books",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=1,column=0,sticky=W)
lblSciFibooks=Label(ABC2,text="Sci-Fi books",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=2,column=0,sticky=W)
lblHistbooks=Label(ABC2,text="History books",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=3,column=0,sticky=W)
lblMythologybooks=Label(ABC2,text="Mythology books",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=4,column=0,sticky=W)
lblLaptops=Label(ABC2,text="Laptops",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=6,column=0,sticky=W)
lblPowerBanks=Label(ABC2,text="Power Banks",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=7,column=0,sticky=W)
lblMobilephones=Label(ABC2,text="Mobile Phones",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=8,column=0,sticky=W)
lblDesktops=Label(ABC2,text="Desktop computers",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=9,column=0,sticky=W)
#======================================================================================================================
txtLitbooks=Entry(ABC2,textvariable=Litbooks,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=1,column=1,pady=1)
txtSciFibooks=Entry(ABC2,textvariable=SciFibooks,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=2,column=1,pady=1)
txtHistbooks=Entry(ABC2,textvariable=Historybooks,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=3,column=1,pady=1)
txtMythologybooks=Entry(ABC2,textvariable=Mythologybooks,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=4,column=1,pady=1)
lblElectronics=Label(ABC2,text="Electronics",font=('arial',20,'bold'),pady=1,bd=8,bg="cadet blue",
                   fg="Cornsilk",width=25,justify=CENTER).grid(row=5,column=0,columnspan=4)
txtLaptops=Entry(ABC2,textvariable=Laptops,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=6,column=1,pady=1)
txtPowerbanks=Entry(ABC2,textvariable=Powerbanks,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=7,column=1,pady=1)

txtMobilephones=Entry(ABC2,textvariable=Mobilephones,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=8,column=1,pady=1)
txtDesktops=Entry(ABC2,textvariable=Desktops,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=9,column=1,pady=1)




#======================================================================================================================
#======================================================================================================================
lblStationery=Label(ABC3,text="Stationery",font=('arial',20,'bold'),pady=1,bd=8,bg="cadet blue",
                   fg="Cornsilk",width=25,justify=CENTER).grid(row=0,column=0,columnspan=4)
lblCalculators=Label(ABC3,text="Calculators",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=1,column=0,sticky=W)
lblStaples=Label(ABC3,text="Stapels",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=2,column=0,sticky=W)
lblEnvelopes=Label(ABC3,text="Envelopes",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=3,column=0,sticky=W)
lblStickynotes=Label(ABC3,text="Sticky Notes",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=4,column=0,sticky=W)
lblTracksuits=Label(ABC3,text="tracksuits",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=6,column=0,sticky=W)
lblJerseys=Label(ABC3,text="Jerseys",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=7,column=0,sticky=W)
lblBlazers=Label(ABC3,text="Blazers",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=8,column=0,sticky=W)
lblTrousers=Label(ABC3,text="Trousers",bg="powder blue",
                   font=('arial',18,'bold'),justify=LEFT).grid(row=9,column=0,sticky=W)
#======================================================================================================================
txtCalculators=Entry(ABC3,textvariable=Calculators,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=1,column=1,pady=1)
txtStapels=Entry(ABC3,textvariable=Stapels,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=2,column=1,pady=1)
txtEnvelopes=Entry(ABC3,textvariable=Envelopes,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=3,column=1,pady=1)
txtStickynotes=Entry(ABC3,textvariable=Stickynotes,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=4,column=1,pady=1)
lblUniform=Label(ABC3,text="Uniform",font=('arial',20,'bold'),pady=1,bd=8,bg="cadet blue",
                   fg="Cornsilk",width=25,justify=CENTER).grid(row=5,column=0,columnspan=4)
txtTracksuits=Entry(ABC3,textvariable=Tracksuits,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=6,column=1,pady=1)
txtJerseys=Entry(ABC3,textvariable=Jerseys,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=7,column=1,pady=1)

txtBlazers=Entry(ABC3,textvariable=Blazers,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=8,column=1,pady=1)
txtTrousers=Entry(ABC3,textvariable=Trousers,font=('arial',18,'bold'),bd=8,bg="powder blue",
                   fg="black",width=12,justify=CENTER).grid(row=9,column=1,pady=1)
#======================================================================================================================
txtReceipt=Text(ABC5,height=30,width=51,bd=20,font=('arial',9,'bold'))
txtReceipt.grid(row=0,column=0)
#======================================================================================================================
btnTotal=Button(ABC6,padx=50,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=7,bg="powder blue",
                text="Total",command=Total).grid(row=0,column=0)
btnExit=Button(ABC6,padx=50,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=7,bg="powder blue",
                text="Exit",command=iExit).grid(row=0,column=1)
#======================================================================================================================

root.mainloop()