from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import ast
import customtkinter
from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image , ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl , xlrd
from openpyxl import Workbook
import pathlib




root = Tk()
root.title("Login")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()


    file=open('datasheet2.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    # print(r.keys())
    # print(r.values())


    if username in r.keys() and password==r[username]:
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry("1250x700+210+150")
        screen.configure(bg="white")

        # Label(screen,text="Hello Everyone!",bg="#fff",font=("Calibri(Body)",50,"bold")).pack(expand=True)
########this block of code is the dashboard of our app
        ############# figure out how to add text to this frame
        """
        Sources to figure out how to add text to this frame :
        1) watch parvat technology youtube video and see how he edits text
        2) learn how to add buttons to frame



        THINGS TO MAKE THE PAGE LOOK MORE ATTRACTIVE
        1) Add a small tree icon on the 

        """

        Label(screen,text=username.get() , bg="#fff", font=("Calibri(Body)",50,"bold")).pack(expand=True)
        # Label(screen,text="Welcome to Tech Veda                                                                             " , bg="#f0687c",borderwidth= 3,  font=("Harlow Solid Italic",30,"bold")).place(x=5,y=20)
        

        screen.mainloop()
    
    else:
        messagebox.showerror("Invalid","invalid username or password")
 

##### defining user variable

def on_enter(e):
        user.delete(0,"end")

def on_leave(e):
        name=user.get()
        if name=="":
            user.insert(0,"Username")

user = Entry(root,width=25,fg="black",border=0, bg="white",font = ("Microsoft Yahei UI Light",11))
user = Entry(root,width=25,fg="black", border=0,bg="white",font=("Microsoft Yahei UI Light",11,"bold") )
user.place(x=30 , y =80)
user.insert(0,'username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

#########################################################


def on_enter(e):
        code.delete(0,"end")

def on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0,"Password")


code = Entry(root,width=10,fg="black", border=0,bg="white",font=("Microsoft Yahei UI Light",11,"bold") )
code.place(x=30 , y =150)
code.insert(0,'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)





root.mainloop()