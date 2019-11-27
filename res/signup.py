# signup
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext as st
import func
import mainscr

def showWindow():
    global pwordE 
    global roots
    roots = Tk()
    roots.title('Unforgettable')
    roots.config(background="black")
    roots.geometry('500x200')
    roots.resizable(0,0)
    instruction = Label(roots, text='Please Enter New Credentials',fg="White",bg="black",  font="Helvetica 20 bold") 
    instruction.grid(row=0, column=0, columnspan=3, sticky=E) 
    headingL = Label(roots, text='\nWelcome to the Unforgettable. Please enter a master password below. This will be used to view the saved passwords .\n',justify='left',wraplength=300,fg="White",bg="black")
    headingL.grid(row=1, column=0, columnspan=3, rowspan=3,sticky=W) 
    pwordL = Label(roots, text='Global Password: ',fg="White",bg="black") 
    pwordL.grid(row=5, column=0, sticky=W)
    pwordE = Entry(roots,fg="White",bg="black",show='*')
    pwordE.grid(row=5, column=1) 
    signupButton = Button(roots, text='Continue', fg="green",bg="black" ,command=storeGlobalPwd)
    signupButton.grid(row=5,column=3, sticky=W)
    roots.mainloop()
    
def storeGlobalPwd():
    import algogp
    import mainscr
    algogp.genSalt()
    pwd = algogp.encrypt(pwordE.get()) 
    algogp.storeGlobal(pwd)
    func.createDataFile()
    roots.destroy() 
    mainscr.showWindow()
