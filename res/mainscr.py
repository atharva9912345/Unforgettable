#main screen
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import messagebox
from tkinter import simpledialog
import func
import datarw
import algogp
import algoac

unlocked = False

def showWindow():
    global pwordE  
    global roots

    roots = Tk() 
    roots.title('Unforgettable') 
    roots.config(background="black")
    window_height = "175" if datarw.countAccounts() == -1 else str(175 + (datarw.countAccounts() * 35))
    roots.geometry('580x'+window_height)
    roots.resizable(0,0)

    title = Label(roots, text='All your Passwords are now UNFORGETTABLE and so am I!', font="comicsansms 12 bold",fg="White",bg="black")
    title.grid(row=0, column=0, columnspan=3, sticky=W)
    gapL = Label(roots, text='\n', justify=LEFT,bg="black",fg="white").grid(row=1,column=0,sticky=W)
    if datarw.countAccounts() > 0:
        deleteAllBtn = Button(roots, text='Delete All', fg='red',bg="black", command=confirmDeleteAll).grid(row=3, column=2, sticky=E, padx=5)
        addEntryBtn = Button(roots, text='Add Entry', command=addEntry,bg="black",fg="white").grid(row=3, column=1, sticky=E, padx=5)
    else:
        addEntryBtn = Button(roots, text='Add Entry', command=addEntry,bg="black",fg="white").grid(row=3, column=1, sticky=E, padx=45)

    myaccL = Label(roots, text='\nMy Accounts', font="Helvetica 12 bold",bg="black",fg="white")
    myaccL.grid(row=4, column=0, sticky=W, columnspan=3)

    if datarw.countAccounts() == 0:
        nodataL = Label(roots, text='\nNo accounts found. Click on Add Entry above to add a new account.',bg="black",fg="white")
        nodataL.grid(row=5, column=0, sticky=W, columnspan=3)
    elif datarw.countAccounts() == -1:
        errorL = Label(roots, text='\nThere was an error fetching the data.',fg="red",bg="black")
        errorL.grid(row=5, column=0, sticky=W, columnspan=3)
    else:
        displayAccounts()

    
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

def refreshWindow():
    roots.destroy()
    showWindow()

def addEntry():
    global entryWindow
    global nameE
    global unameE
    global passE
    global gapL
    entryWindow = Tk()
    entryWindow.config(background="black")
    entryWindow.title('New Entry')
    entryWindow.geometry('350x250')
    entryWindow.resizable(0,0)
    title = Label(entryWindow, text='Enter New Account Details\n', font="Helvetica 15 bold",bg="black",fg="white").grid(row=0, column=0, columnspan=3, sticky=W)
    nameL = Label(entryWindow, text='Account Name: ',bg="black",fg="white").grid(row=1, column=0, sticky=W)
    nameE = Entry(entryWindow,bg="black",fg="white")
    nameE.grid(row=1, column=1)
    unameL = Label(entryWindow, text='Username: ',bg="black",fg="white").grid(row=2, column=0, sticky=W)
    unameE = Entry(entryWindow,bg="black",fg="white")
    unameE.grid(row=2, column=1)
    passL = Label(entryWindow, text='Password: ',bg="black",fg="white").grid(row=3, column=0, sticky=W)
    passE = Entry(entryWindow, show='*',bg="black",fg="white")
    passE.grid(row=3, column=1)
    gapL = Label(entryWindow, text='\n',bg="black",fg="white")
    gapL.grid(row=4, column=0, columnspan=2, sticky=W)
    entryBtn = Button(entryWindow, text='Add New Account', fg='green',bg="black", command=validateAdd).grid(row=5, column=1, columnspan=2, sticky=E)

def validateAdd():
    name = nameE.get()
    uname = unameE.get()
    pwd = passE.get()
    if name == "" or uname == "" or pwd == "":
        gapL.config(text='\nPlease enter all the fields.\n', fg='red')
    else:
        if datarw.addEntry(name, uname, pwd):
            gapL.config(text='\nSuccess!\n', fg='green')
            entryWindow.destroy()
            refreshWindow()
        else:
            gapL.config(text='\nThere was an error.\n', fg='red')

def displayAccounts():
    accounts = datarw.readData()
    row = 6
    for key, value in accounts.items():
        account = value
        Label(roots, text=account["n"], font="sans-serif 10 bold",bg="black",fg="white").grid(row=row, column=0, sticky=W, pady=5)
        Button(roots, text='View Details', fg='green',bg="black", command=lambda key=key: viewDetails(key)).grid(row=row, column=2, sticky=E,padx=10)
        if not unlocked:
            deleteBtn = Button(roots, text='Delete Account',bg="black",fg="red", command=lambda key=key: deleteEntryHandler(key)).grid(row=row, column=3, padx=10, sticky=E)
        else:
          deleteBtn = Button(roots, text='Delete Account',bg="black",fg="red", command=lambda key=key: deleteEntryHandler(key)).grid(row=row, column=3, padx=10, sticky=E)  

        row += 1

def viewDetails(id):
    global detailsWindow
    global decryptPwdT
    global decryptPwdE
    global decryptPwdBtn
    global detailsGapL2
    global pwdTL

    data = datarw.readData()
    name = data[id]["n"]
    username = data[id]["u"]
    password = "********"

    detailsWindow = Tk()
    detailsWindow.config(background="black")
    detailsWindow.title('Account Details')
    detailsWindow.geometry('450x260')
    detailsWindow.resizable(0,0)
    title = Label(detailsWindow, text=name + '\n', font="Helvetica 15 bold",bg="black",fg="white")
    title.grid(row=0, column=0, columnspan=3, sticky=W)
    unameL = Label(detailsWindow, text='Username', font="sans-serif 10 bold",bg="black",fg="white")
    unameL.grid(row=1, column=0, sticky=W)
    unameTL = Label(detailsWindow, text=username,bg="black",fg="white")
    unameTL.grid(row=2, column=0, sticky=W)
    pwdL = Label(detailsWindow, text='Password', font="sans-serif 10 bold",bg="black",fg="white")
    pwdL.grid(row=1, column=1, sticky=W)
    pwdTL = Label(detailsWindow, text=password,bg="black",fg="white")
    pwdTL.grid(row=2, column=1, sticky=W)

    if not unlocked:
        detailsGapL = Label(detailsWindow, text='\n', justify=LEFT,bg="black",fg="white")
        detailsGapL.grid(row=3, column=0, columnspan=4, sticky=W)
        decryptPwdT = Label(detailsWindow, text="Global Password: ", justify=LEFT,bg="black",fg="white")
        decryptPwdT.grid(row=4, column=0, sticky=W)
        decryptPwdE = Entry(detailsWindow, show='*',bg="black",fg="white")
        decryptPwdE.grid(row=4, column=1, columnspan=3, sticky=W)
        detailsGapL2 = Label(detailsWindow, text='\nEnter global password to decrypt info.\n', justify=LEFT,bg="black",fg="white")
        detailsGapL2.grid(row=5, column=0, columnspan=3, sticky=W)
        decryptPwdBtn = Button(detailsWindow, text='Decrypt Password',bg="black",fg="white", command=lambda key=data[id]["p"]: decryptHandler(key))
        decryptPwdBtn.grid(row=4, column=4, columnspan=4, sticky=E,padx=15)
    else:
        detailsGapL = Label(detailsWindow, text='\n', justify=LEFT,bg="black",fg="white")
        detailsGapL.grid(row=3, column=0, columnspan=4, sticky=W)
        decryptPwdBtn = Button(detailsWindow, text='Decrypt Password',bg="black",fg="white", command=lambda key=data[id]["p"]: decryptHandler(key))
        decryptPwdBtn.grid(row=6, column=1, sticky=W)
        loginPwdBtn = Button(detailsWindow, text='Copy Password',bg="black",fg="white", command=lambda key=data[id]["p"]: copy_button(key))
        loginPwdBtn.grid(row=6, column=5, columnspan=4, sticky=E)
        detailsGapL2 = Label(detailsWindow, text='\n\n')
        detailsGapL2.grid(row=7, column=0, columnspan=2, sticky=W)

def decryptHandler(pwd):
    if not unlocked:
        gpwd = decryptPwdE.get()
        if gpwd != "":
            if algogp.checkPassword(gpwd) == True:
                detailsGapL2.config(text='\nPassword decrypted.\nClose the window to encrypt it.\n', fg='green')
                decryptPwdBtn.grid_remove()
                decryptPwdE.grid_remove()
                decryptPwdT.grid_remove()
                pwdTL.config(text=algoac.decrypt(pwd))
                loginPwdBtn = Button(detailsWindow, text='Copy Password', command=lambda key=pwd: copy_button(key))
                loginPwdBtn.grid(row=6, column=5, columnspan=4, sticky=E)
            else:
                detailsGapL2.config(text='\nIncorrect global password.\n', fg='red')
        else:
            detailsGapL2.config(text='\nPlease enter your global password.\n', fg='red')
    else:
        detailsGapL2.config(text='\nPassword decrypted.\nClose the window to encrypt it.\n', fg='green')
        pwdTL.config(text=algoac.decrypt(pwd))
        decryptPwdBtn.grid_remove()


def deleteEntryHandler(id):
    if not unlocked:
        pwd = simpledialog.askstring("Delete Account?",
                                     "Enter your global password to confirm deletion of this account.\n\nWarning: This can not be undone.",
                                     show='*')
        if pwd is not None:
            if algogp.checkPassword(pwd) == True:
                deleteAccount(id)
            else:
                messagebox.showerror("Error", "Wrong Password. (or error)")
    else:
        confirm = messagebox.askokcancel("Delete Account?",
                                         "Do you want to delete this account?\n\nWarning: This can not be undone.")
        if confirm:
            deleteAccount(id)


def copy_button(pwd):
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(algoac.decrypt(pwd))
    clip.destroy()

def deleteAccount(id):
    if datarw.deleteAccount(id):
        refreshWindow()
    else:
        messagebox.showerror("Error", "Oops! Something went wrong.")

def confirmDeleteAll():
    if not unlocked:
        pwd = simpledialog.askstring("Delete All?",
                                     "Enter your global password to confirm deletion of all accounts.\n\nWarning: This can not be undone.",
                                     show='*')
        if pwd is not None:
            if algogp.checkPassword(pwd) == True:
                deleteAll()
            else:
                messagebox.showerror("Error", "Wrong Password. (or error)")
    else:
        confirm = messagebox.askokcancel("Delete Account?",
                                         "Do you want to delete all accounts?\n\nWarning: This can not be undone.")
        if confirm:
            deleteAll()

def deleteAll():
    if datarw.writeData(""):
        refreshWindow()
    else:
        func.Log("Could not delete all accounts. Must've logged it above.", "deleteAll")



