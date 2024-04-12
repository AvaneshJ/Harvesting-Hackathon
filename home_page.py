from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import customtkinter




# background = ImageTk.PhotoImage(Image.open("farm.jpg"))
# bglabel = Label(image=background)
# bglabel.place(x=1200 , y = 700)



home= Tk()
home.title("Home Page")
home.geometry('1200x700+210+100')

background = ImageTk.PhotoImage(Image.open("jk2.png"))
bglabel = Label(image=background , width = 1400 , height = 700)
bglabel.place(x=0 , y = 0)

home.configure(bg="#E1E8E2")
home.resizable(True,True)  

framebg = "grey"

myLabel = Label(home,text="Welcome to Tech Veda                                                                             " , bg="#f0687c",borderwidth= 3,  font=("Harlow Solid Italic",30,"bold")).place(x=0,y=0)

my_img = ImageTk.PhotoImage(Image.open("tree2.jpg"))
my_label = Label(image = my_img)
my_label.place(x=1200 , y=0)


#####Drop Down Box ####################

myLabel = Label(home,text="Select the type of Insect " ,  font=("arial",30,"bold"), bg = "#E1E8E2").place(x= 550 ,  y = 100)



clicked = StringVar()
clicked.set("Select the type of Insect")

def music(event) :
    # music_label = Label(home, text = clicked.get() , font = 20).place(x = 600, y = 225)
    if clicked.get() == "Caterpillar" :
        music_label = Label(home, text = "play catterpillar song   ",font=20 , bg = "#E1E8E2").place(x = 675, y = 225)
    if clicked.get() == "Grasshopper" :
        music_label = Label(home, text = "play grasshopper song",font=20 , bg = "#E1E8E2").place(x = 675, y = 225)
    if clicked.get() == "Locust     " :
        music_label = Label(home, text = "play locust song          ",font=20 ,bg = "#E1E8E2").place(x = 675, y = 225)


        



options = [
    "Caterpillar",
    "Locust     ",
    "Grasshopper"
]


drop = OptionMenu(home,clicked, *options  , command=music)
drop.config(width=50 , height = 2 )
drop.place(x= 600 ,  y = 175)

# sound = Button(home,text = 'Get music from avanesh and figure out how to add the sound to this button ' , command=music)
# sound.place(x = 1000 , y = 175)










##########################################
########## side menu bar ############



f= Frame(home,bd=2 , bg="#54CF1A", width = 400 , height = 700 , relief = GROOVE)
f.place(x=0,y=57)

user_icon = Label(home,text="Hello, User1234" ,font = ("Calibri (Body)", 15 , "bold") , borderwidth= 3  , width = 20 , height = 2, bg = "white")
user_icon.place(x=90 , y = 80)
user_icon = ImageTk.PhotoImage(Image.open("gh2.png"))
my_label = Label(image = user_icon)
my_label.place(x=5 , y=75)


###################### slider bar ########

volume = Label(home, text = "Volume " , font =("calibri(body)" , 15 , "bold"), bg = "#E1E8E2", width = 15 , height =2 )
volume.place(x = 650 , y = 300)

horizontal = Scale(home, from_ =0 , to = 100,  orient=HORIZONTAL)
horizontal.place(x = 700 , y = 350)





###############################################################################################



home.mainloop()