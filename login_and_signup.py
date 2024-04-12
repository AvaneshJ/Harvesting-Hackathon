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


background="#6283D"
framebg="#EDEDED"
framefg="#06283D"


root = Tk()
root.title("Login")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()


    file=open('datasheet.txt','r')
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

        # Label(screen,text="Welcome to tech veda" , bg="#fff", font=("Calibri(Body)",50,"bold")).pack(expand=True)
        # Label(screen,text="Welcome to Tech Veda                                                                             " , bg="#f0687c",borderwidth= 3,  font=("Harlow Solid Italic",30,"bold")).place(x=5,y=20)
        

        screen.mainloop()
    
    else:
        messagebox.showerror("Invalid","invalid username or password")






############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def signup_command():
    window=Toplevel(root)
    window.title("SignUp")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False,False)

    def signup():
        username=user.get()
        password=code.get()
        confirmpassword=confirmcode.get()

        if password==confirmpassword:
            try:
                file=open("datasheet.txt","r+")
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open("datasheet.txt","w")
                w=file.write(str(r))

                messagebox.showinfo("Signup","Successfully sign up")
            except:
                file=open("datasheet.txt","w")
                pp=str({"Username":"password"})
                file.write(pp)
                file.close()
    
        else:
            messagebox.showerror("Invalid", "Both passwords should match ")
        
        if username==password=="":
            messagebox.showwarning("Invalid", "Please enter username and password")

    def sign():
        window.destroy()
 

    img = ImageTk.PhotoImage(file="signup.jpg")
    Label(window,image=img,bg="white").place(x=1,y=1)

    frame=Frame(window,width=350,height=390,bg="white")
    frame.place(x=480,y=50)


    heading=Label(frame,text="Sign up" ,fg="#57a1f8",bg="white",font = ("Microsoft Yahei UI Light",23,"bold"))
    heading.place(x=100,y=5)

#######################################

    def on_enter(e):
        user.delete(0,"end")

    def on_leave(e):
        name=user.get()
        if name=="":
            user.insert(0,"Username")

    user = Entry(frame,width=25,fg="black",border=0, bg="white",font = ("Microsoft Yahei UI Light",11))
    user = Entry(frame,width=25,fg="black", border=0,bg="white",font=("Microsoft Yahei UI Light",11,"bold") )
    user.place(x=30 , y =80)
    user.insert(0,'username')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame,width=295 , height=2,bg="black").place(x=25,y=107)
#########################################################

    def on_enter(e):
        code.delete(0,"end")

    def on_leave(e):
        name=code.get()
        if name=="":
            code.insert(0,"Password")


    code = Entry(frame,width=10,fg="black", border=0,bg="white",font=("Microsoft Yahei UI Light",11,"bold") )
    code.place(x=30 , y =150)
    code.insert(0,'Password')
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)
    
    Frame(frame,width=295 , height=2,bg="black").place(x=25,y=177)
##################################################

    def on_enter(e):
        confirmcode.delete(0,"end")

    def on_leave(e):
        name=confirmcode.get()
        if name=="":
            confirmcode.insert(0,"Confirm Password")


    confirmcode = Entry(frame,width=50,fg="black", border=0,bg="white",font=("Microsoft Yahei UI Light",11,"bold") )
    confirmcode.place(x=30 , y =230)
    confirmcode.insert(0,'Confirm Password')
    confirmcode.bind("<FocusIn>", on_enter)
    confirmcode.bind("<FocusOut>", on_leave)
    
    
    Frame(frame,width=295 , height=2,bg="black").place(x=25,y=255)
########################################################

    Button(frame,width=39,pady=7,text="Sign up",bg="#57a1f8",fg="white",border=0, command=signup).place(x=35,y=280)
    label=Label(frame,text="I have an account",fg="black",bg="white",font=("Microsoft Yahei UI Light",9) )
    label.place(x=90 , y= 340)
    
    signin=Button(frame,width=6,text="Sign in", border = 0, bg="white",cursor="hand2",fg = "#57a1f8", command=sign)
    signin.place(x=200,y=340)

              

    window.mainloop()
############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




img = ImageTk.PhotoImage(file="login.jpg")
Label(root,image=img,bg="white").place(x=1,y=1)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)


heading=Label(frame,text="Sign In",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
heading.place(x=100 , y=5)

##############################

def on_enter(e):
    user.delete(0,"end")

def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"Username")


user = Entry(frame,width=25,fg="black", border=0,bg="white",font=("Microsoft Yahei UI Light",11,"bold") )
user.place(x=30 , y =80)
user.insert(0,'username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295 , height=2,bg="black").place(x=25,y=107)

##############################

def on_enter(e):
    code.delete(0,"end")

def on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0,"Password")


code = Entry(frame,width=10,fg="black", border=0,bg="white",font=("Microsoft Yahei UI Light",11,"bold") )
code.place(x=30 , y =150)
code.insert(0,'Password')

code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=295 , height=2,bg="black").place(x=25,y=177)
##################################

Button(frame,width=39,pady=7,text="Sign In",bg="#57a1f8",fg="white",border=0 , command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?", fg = "black",bg="white",font=("Microsoft Yahei UI Light",9) )
label.place(x=75 , y =270)

sign_up= Button(frame,width=6,text="Sign up",border=0,bg="white",cursor="hand2",fg="#57a1f8",command=signup_command)
sign_up.place(x=215,y=270)



root.mainloop()
