from tkinter import *
import spam_class as sc
import os

root = Tk()
root.resizable(FALSE, FALSE)
root.title("Spam Program")
root.geometry("300x190")
#Class
spam = sc.Spam()
sentence = ""

#Wİndow Icon
myPath = os.getcwd()

def keyboardSpamDef():
	global menubar, keyboardSpamMenu, clickSpamMenu, refreshSpamMenu
	menubar.destroy()
	menubar = Menu(root)
	keyboardSpamMenu = menubar.add_cascade(label="Keyboard Spam", command=keyboardSpamDef, state="disabled")
	clickSpamMenu = menubar.add_cascade(label="Click Spam", command=clickSpamDef, state="normal")
	refreshSpamMenu = menubar.add_cascade(label="Refresh Spam", command=refreshSpamDef, state="normal")
	root.config(menu=menubar)
	spam.keyboardSpam()

def clickSpamDef():
	global menubar, keyboardSpamMenu, clickSpamMenu, refreshSpamMenu
	menubar.destroy()
	menubar = Menu(root)
	keyboardSpamMenu = menubar.add_cascade(label="Keyboard Spam", command=keyboardSpamDef, state="normal")
	clickSpamMenu = menubar.add_cascade(label="Click Spam", command=clickSpamDef, state="disabled")
	refreshSpamMenu = menubar.add_cascade(label="Refresh Spam", command=refreshSpamDef, state="normal")
	root.config(menu=menubar)	
	spam.clickSpam()

def refreshSpamDef():
	global menubar, keyboardSpamMenu, clickSpamMenu, refreshSpamMenu
	menubar.destroy()
	menubar = Menu(root)
	keyboardSpamMenu = menubar.add_cascade(label="Keyboard Spam", command=keyboardSpamDef, state="normal")
	clickSpamMenu = menubar.add_cascade(label="Click Spam", command=clickSpamDef, state="normal")
	refreshSpamMenu = menubar.add_cascade(label="Refresh Spam", command=refreshSpamDef, state="disabled")
	root.config(menu=menubar)
	spam.refreshSpam()

menubar = Menu(root)
keyboardSpamMenu = menubar.add_cascade(label="Keyboard Spam", command=keyboardSpamDef, state="disabled")
clickSpamMenu = menubar.add_cascade(label="Click Spam", command=clickSpamDef, state="normal")
refreshSpamMenu = menubar.add_cascade(label="Refresh Spam", command=refreshSpamDef, state="normal")
root.config(menu=menubar)

#keyboardSpam
spamSpamming = True
spam.keyboardSpam()

root.config(menu=menubar)
root = mainloop()