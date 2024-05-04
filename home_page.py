from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import customtkinter
import os
import time
import pygame
import threading
import datetime
import time
import tkinter as tk
import pygame
import Harvesting_chatbot as cb
from tkinter import filedialog

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


home= Tk()
home.title("Home Page")
screen_width = home.winfo_screenwidth()
screen_height = home.winfo_screenheight()
home.geometry(f"{screen_width}x{screen_height}+0+0")

background = ImageTk.PhotoImage(Image.open("jk.png"))
bglabel = Label(home,image=background , width = 1400 , height = 700)
bglabel.place(x=0 , y = 0)

pygame.mixer.init

home.configure(bg="#E1E8E2")
home.resizable(True,True)  

framebg = "black"

frame1 = customtkinter.CTkFrame(master=home,width=1500,height=40,border_width=0,border_color="#808080",fg_color="#363538")
frame1.place(x=0,y=0)
name = customtkinter.CTkLabel(home,text="Tech Veda" ,fg_color="#363538", text_color="#EEEDF4",  font=("Arial Rounded MT Bold",20),width=200,height=40)
name.place(x=550,y=0)

#  function for playing and pausing song
def play_song(song_path, duration_minutes):
    pygame.mixer.init()
    if not os.path.exists(song_path):
        print("Error", f"Song file '{song_path}' not found.")
        return

    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    # Calculate duration in seconds
    duration_seconds = duration_minutes * 60

    # Wait for the specified duration while checking if the song is still playing
    start_time = pygame.time.get_ticks() / 1000  # Get current time in seconds
    while pygame.mixer.music.get_busy() and (pygame.time.get_ticks() / 1000 - start_time) < duration_seconds:
        pygame.time.Clock().tick(10)  # Adjust tick rate to control the loop frequency

    pygame.mixer.music.stop()

clicked_frequency = StringVar()
# clicked_frequency.set(song_paths[1])




def play():
    song_path = clicked_frequency.get().strip()  # Get the selected song path
    duration_text= clicked.get().strip()
    if song_path and duration_text:  # Ensure a valid song path is selected
        try:
            duration_minute=int(duration_text.split()[0])
            threading.Thread(target=play_song,args=(song_path,duration_minute),daemon=True).start()
        except ValueError:
            print("Error","Invalid")
def pause():
    pygame.mixer.music.pause()










# submit button

play_btn = customtkinter.CTkButton(home,text="Play",width=100,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=play)
play_btn.place(x=650,y=500)
pause_btn = customtkinter.CTkButton(home, text="Pause", width=100, height=40, border_width=0, border_spacing=0, font=("Helvetica", 20), fg_color="#363538", command=pause)
pause_btn.place(x=350, y=500)


#####Drop Down Box ####################

myLabel = Label(home,text="Select the type of Insect "  , font=("arial",20,"bold"), bg = "#E1E8E2").place(x= 200 ,  y = 100)



clicked = StringVar()
clicked.set("Select the type of Insect")

# def music(event) :
#     music_label = Label(home, text = clicked.get() , font = 20).place(x = 200, y = 225)
#     if clicked.get() == "Caterpillar" :
#         music_label = Label(home, text = "play catterpillar song   ",font=20 , bg = "#E1E8E2").place(x = 275, y = 225)
#     if clicked.get() == "Grasshopper" :
#         music_label = Label(home, text = "play grasshopper song",font=20 , bg = "#E1E8E2").place(x = 275, y = 225)
#     if clicked.get() == "Locust     " :
#         music_label = Label(home, text = "play locust song          ",font=20 ,bg = "#E1E8E2").place(x = 275, y = 225)


        

options = [
    "Caterpillar",
    "Locust     ",
    "Grasshopper"
]


drop = OptionMenu(home,clicked, *options  )
drop.config(width=45 , height = 2 )
drop.place(x= 200 ,  y = 175)




# drop down for frequency

myLabel2 = Label(home,text="Select the frequency " ,  font=("arial",20,"bold"), bg = "#E1E8E2").place(x= 750 ,  y = 100)



clicked = StringVar()
clicked.set("Select the Frequency")

# def music(event) :
#     music_label = Label(home, text = clicked.get() , font = 20).place(x = 775, y = 225)
#     if clicked.get() == "Caterpillar" :
#         music_label = Label(home, text = "50 kHz   ",font=20 , bg = "#E1E8E2").place(x = 850, y = 225)
#     if clicked.get() == "Grasshopper" :
#         music_label = Label(home, text = "100 kHz   ",font=20 , bg = "#E1E8E2").place(x = 850, y = 225)
#     if clicked.get() == "Locust     " :
#         music_label = Label(home, text = "200 kHz          ",font=20 ,bg = "#E1E8E2").place(x = 850, y = 225)


        

options = [
    "50 kHz      ",
    "100 kHz     ",
    "200 kHz     ",
]


drop = OptionMenu(home,clicked, *options  )
drop.config(width=45 , height = 2 )
drop.place(x= 750,  y = 175)



# Drop Down for duration

myLabel3 = Label(home,text="Select the Duration " ,  font=("arial",20,"bold"), bg = "#E1E8E2").place(x= 200 ,  y = 300)



clicked = StringVar()
clicked.set("Select the duration")

# def music(event) :
#     music_label = Label(home, text = clicked.get() , font = 20).place(x = 200, y = 400)
#     if clicked.get() == "1 minute" :
#         music_label = Label(home, text = "play catterpillar song   ",font=20 , bg = "#E1E8E2").place(x = 275, y = 400)
#     if clicked.get() == "1/2 hour" :
#         music_label = Label(home, text = "play grasshopper song",font=20 , bg = "#E1E8E2").place(x = 275, y = 400)
#     if clicked.get() == "1 hour     " :
#         music_label = Label(home, text = "play locust song          ",font=20 ,bg = "#E1E8E2").place(x = 275, y = 400)


        

options = [
    "1 minute       ",
    "1/2 hour       ",
    "1 hour         "
]


drop = OptionMenu(home,clicked, *options  )
drop.config(width=40 , height = 2 )
drop.place(x= 200 ,  y = 375)









##########################################
########## side menu bar ############



# f= Frame(home,bd=2 , bg="#54CF1A", width = 400 , height = 700 , relief = GROOVE)
# f.place(x=0,y=57)

# user_icon = Label(home,text="Hello, User1234" ,font = ("Calibri (Body)", 15 , "bold") , borderwidth= 3  , width = 20 , height = 2, bg = "white")
# user_icon.place(x=90 , y = 80)
# user_icon = ImageTk.PhotoImage(Image.open("gh2.png"))
# my_label = Label(image = user_icon)
# my_label.place(x=5 , y=75)

# function for home page
def home_page():
    home_frame = customtkinter.CTkFrame(home,width=1000,height=600,border_width=0,border_color="#016008",fg_color="black")
    home_frame.place(x=200,y=78) 

    home_label = customtkinter.CTkLabel(home_frame,text="Home" ,font=("Helvatica",30,"bold"),fg_color="#36CA03",text_color="black",width=1000,height=50,bg_color="#363538")
    home_label.place(x=0,y=0)

        #####Drop Down Box ####################

    myLabel = Label(home_frame,text="Select the type of Insect "  , font=("arial",20,"bold"), bg = "#E1E8E2").place(x= 200 ,  y = 100)



    clicked = StringVar()
    clicked.set("Select the type of Insect")

    def music(event) :
        music_label = Label(home_frame, text = clicked.get() , font = 20).place(x = 200, y = 225)
        if clicked.get() == "Caterpillar" :
            music_label = Label(home_frame, text = "play catterpillar song   ",font=20 , bg = "#E1E8E2").place(x = 275, y = 225)
        if clicked.get() == "Grasshopper" :
            music_label = Label(home_frame, text = "play grasshopper song",font=20 , bg = "#E1E8E2").place(x = 275, y = 225)
        if clicked.get() == "Locust     " :
            music_label = Label(home_frame, text = "play locust song          ",font=20 ,bg = "#E1E8E2").place(x = 275, y = 225)


            

    options = [
        "Caterpillar",
        "Locust     ",
        "Grasshopper"
    ]


    drop = OptionMenu(home_frame,clicked, *options  , command=music)
    drop.config(width=45 , height = 2 )
    drop.place(x= 200 ,  y = 175)




    # drop down for frequency

    myLabel2 = Label(home_frame,text="Select the frequency " ,  font=("arial",20,"bold"), bg = "#E1E8E2").place(x= 750 ,  y = 100)



    clicked = StringVar()
    clicked.set("Select the Frequency")

    def music(event) :
        music_label = Label(home_frame, text = clicked.get() , font = 20).place(x = 775, y = 225)
        if clicked.get() == "Caterpillar" :
            music_label = Label(home_frame, text = "50 kHz   ",font=20 , bg = "#E1E8E2").place(x = 850, y = 225)
        if clicked.get() == "Grasshopper" :
            music_label = Label(home_frame, text = "100 kHz   ",font=20 , bg = "#E1E8E2").place(x = 850, y = 225)
        if clicked.get() == "Locust     " :
            music_label = Label(home_frame, text = "200 kHz          ",font=20 ,bg = "#E1E8E2").place(x = 850, y = 225)


            

    options = [
        "50 kHz      ",
        "100 kHz     ",
        "200 kHz     ",
    ]


    drop = OptionMenu(home_frame,clicked, *options  , command=music)
    drop.config(width=45 , height = 2 )
    drop.place(x= 750,  y = 175)



    # Drop Down for duration

    myLabel3 = Label(home_frame,text="Select the Duration " ,  font=("arial",20,"bold"), bg = "#E1E8E2").place(x= 200 ,  y = 300)



    clicked = StringVar()
    clicked.set("Select the duration")

    def music(event) :
        music_label = Label(home_frame, text = clicked.get() , font = 20).place(x = 200, y = 400)
        if clicked.get() == "1 minute" :
            music_label = Label(home_frame, text = "play catterpillar song   ",font=20 , bg = "#E1E8E2").place(x = 275, y = 400)
        if clicked.get() == "1/2 hour" :
            music_label = Label(home_frame, text = "play grasshopper song",font=20 , bg = "#E1E8E2").place(x = 275, y = 400)
        if clicked.get() == "1 hour     " :
            music_label = Label(home_frame, text = "play locust song          ",font=20 ,bg = "#E1E8E2").place(x = 275, y = 400)


            

    options = [
        "1 minute       ",
        "1/2 hour       ",
        "1 hour         "
    ]


    drop = OptionMenu(home_frame,clicked, *options  , command=music)
    drop.config(width=40 , height = 2 )
    drop.place(x= 200 ,  y = 375)
   

    


# function for chat page
def chat_page():
    chat_frame = customtkinter.CTkFrame(home,width=1000,height=600,border_width=0,border_color="#016008",fg_color="black")
    chat_frame.place(x=250,y=100) 

    customtkinter.CTkLabel(home,text="Chat-Bot" ,font=("Helvatica",30,"bold"),fg_color="#36CA03",text_color="black",width=1000,height=50,bg_color="#363538").place(x=250,y=78)

    def start():
    # Start chat
        txt = customtkinter.CTkTextbox(chat_frame, width=1000, height=600)
        txt.place(x=0, y=0)
        txt.insert(tk.END, "\n" + "Welcome to the Crop Information Chatbot!")
        entry = customtkinter.CTkEntry(chat_frame, placeholder_text="Please Enter a message", width=950,height=50)
        entry.place(x=0, y=510)
        customtkinter.CTkButton(chat_frame, text="Send", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), width=95,height=50, command=lambda: chatting(txt,entry)).place(x=905, y=510)

    def chatting(txt,entry):
        text = entry.get()
        try:
            if text.strip():  # Check if the input is not empty
                chat = cb.generate_response(text)
                print(chat)
                txt.configure(state="normal")
                txt.insert(tk.END,"\n" + text + "\n" + chat)
                txt.configure(state="disabled")
                entry.delete(0, 'end')
        except Exception as e:
            txt.configure(state="normal")
            txt.insert(tk.END, "\n" + f"An error occurred: {e}")
            txt.configure(state="disabled")
            entry.delete(0, 'end')

    start()

# function for about page

def about_page():

    pass
#     about_frame = customtkinter.CTkFrame(home,width=1000,height=600,border_width=0,border_color="#808080",fg_color="#363538")
#     about_frame.place(x=0,y=0) 

#     about_us_label = customtkinter.CTkLabel(home,text="About Us" ,font=("Bahnschrift SemiLight Condensed",30,"bold"),fg_color="#36CA03",text_color="black",width=1000,height=50,bg_color="#363538")
#     about_us_label.place(x=0,y=0)

#     about_label = customtkinter.CTkLabel(home,text=" About Us Page" ,font=("Bahnschrift SemiLight Condensed",30,"bold"),text_color="black",width=1000,height=100,bg_color="#363538")
#     about_label.place(x=0,y=50)

#     textbox =customtkinter.CTkTextbox(home,width=1000,height =600,font=("Helvatica",20),)
#     textbox.place(x=0,y=0)

#     text ="""                                                                            About Us
# Welcome to Tech-Veda , where agriculture meets convenience! We are a passionate team dedicated to revolutionizing the conventional ways of agriculture , by combining mordern technologies with the core values of agriculture. At Tech-Veda, we believe in the power of technology to simplify everyday tasks, enhance productivity, and bring people closer together. Our journey began with a simple yet profound vision: to create an app that seamlessly integrates into your life, providing intuitive solutions to common challenges while fostering connection and community.

# Driven by a shared commitment to excellence and a deep understanding of user needs, our diverse team of developers, designers, and visionaries has poured countless hours into crafting an app that exceeds expectations. Our goal is not just to meet your needs, but to anticipate them, offering features and functionality that anticipate your desires before you even realize them.

# But Tech-Veda is more than just a product—it's a reflection of our values and our dedication to making a positive impact. We believe in accessibility, inclusivity, and sustainability, striving to create an app that is not only user-friendly but also environmentally conscious. Through ongoing research and development, we are committed to staying at the forefront of technological advancements, ensuring that Tech-eda remains relevant and valuable in an ever-evolving digital landscape.

# At Tech-Veda , we pride ourselves on our unwavering commitment to customer satisfaction. Your feedback is not only welcomed but actively sought after, as we believe that collaboration is key to continual improvement. Whether you're a seasoned tech enthusiast or a first-time user, we are here to support you every step of the way, offering responsive customer service and comprehensive resources to address any questions or concerns you may have.

# As we look to the future, our vision for Tech-Veda remains clear: to empower individuals, businesses, and communities to thrive in a rapidly changing world. Thank you for joining us on this journey—we couldn't do it without you!
    
# Commited to growing green fields and a sustainable future.


#     """


#     textbox.insert("0.0",text)

# function for contact page
def contact_page():

    pass
#     contact_frame = customtkinter.CTkFrame(home,width=1000,height=600,border_width=0,border_color="#808080",fg_color="#363538")
#     contact_frame.place(x=0,y=0) 

#     contact_label = customtkinter.CTkLabel(home,text="This is the contact page " ,font=("Helvatica",20),fg_color="#363538",width=300,height=50,bg_color="#363538")
#     contact_label.place(x=350,y=350)

#     textbox =customtkinter.CTkTextbox(home,width=1000,height =600,font=("Helvatica",20))
#     textbox.place(x=0,y=0)

#     text = """                                                                           Contact Us

# We’re thrilled to connect with you! Whether you have questions, feedback, or just want to say hello, feel free to 
# reach out. Our team is here to assist you.You can drop us a message using the form below or directly email us
# at info@example.com. We promise to get back to you promptly. Thank you for choosing us!


# Email : 

# Phone :

#     """
#     textbox.insert("0.0",text)

# def switch_theme(theme):
#     if theme == 'black':
#         home.tk_setPalette('black')
#         # theme_label.config(text="black")s







# toggle menu bar

# function for toggle menu
# def toggle_menu():

#     def collapse_toggle_menu():
#         toggle_mn_frame.destroy()
#         toggle_button = customtkinter.CTkButton(home,text="☰",width=50,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=toggle_menu)
#         toggle_button.place(x=0,y=35)
# ##############################################################


#     window_height = 700

#     toggle_mn_frame = customtkinter.CTkFrame(master=home,width=200,height=window_height,border_width=0,border_color="#808080",fg_color="#363538")
#     toggle_mn_frame.place(x=0,y=78)

#     home_button = customtkinter.CTkButton(toggle_mn_frame,text="Home",width=200,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command = home_page)
#     home_button.place(x=0,y=50)
#     home_indicator = customtkinter.CTkLabel(toggle_mn_frame,text="" ,fg_color="#363538",width=5,height=40,bg_color="#363538")
#     home_indicator.place(x=0,y=50)

    
#     chat_button = customtkinter.CTkButton(toggle_mn_frame,text="Chat Bot",width=200,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=chat_page)
#     chat_button.place(x=0,y=150)
#     chat_indicator = customtkinter.CTkLabel(toggle_mn_frame,text="" ,fg_color="#363538",width=5,height=40,bg_color="#363538")
#     chat_indicator.place(x=0,y=150)
    
    
#     about_button = customtkinter.CTkButton(toggle_mn_frame,text="About Tech Veda",width=200,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=about_page)
#     about_button.place(x=0,y=250)
#     about_indicator = customtkinter.CTkLabel(toggle_mn_frame,text="" ,fg_color="#363538",width=5,height=40,bg_color="#363538")
#     about_indicator.place(x=0,y=250)

    
#     contact_button = customtkinter.CTkButton(toggle_mn_frame,text="Contact Us",width=200,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=contact_page)
#     contact_button.place(x=0,y=350)
#     contact_indicator = customtkinter.CTkLabel(toggle_mn_frame,text="" ,fg_color="#363538",width=5,height=40,bg_color="#363538")
#     contact_indicator.place(x=0,y=350)


#     toggle_button = customtkinter.CTkButton(home,text="X",width=50,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=collapse_toggle_menu)
#     toggle_button.place(x=0,y=35)









frame2 = customtkinter.CTkFrame(master=home,width=1500,height=45,border_width=0,border_color="#808080",fg_color="#363538")
frame2.place(x=0,y=33)

# code for multiple tabs in top frame

def play_song(song_path, duration_minutes):
    pygame.mixer.init()
    if not os.path.exists(song_path):
        print("Error", f"Song file '{song_path}' not found.")
        return

    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    # Calculate duration in seconds
    duration_seconds = duration_minutes * 60

    # Wait for the specified duration while checking if the song is still playing
    start_time = pygame.time.get_ticks() / 1000  # Get current time in seconds
    while pygame.mixer.music.get_busy() and (pygame.time.get_ticks() / 1000 - start_time) < duration_seconds:
        pygame.time.Clock().tick(10)  # Adjust tick rate to control the loop frequency

    pygame.mixer.music.stop()

def home_page():
    home_frame = customtkinter.CTkFrame(home,width=1000,height=600,border_width=0,border_color="#016008",fg_color="black")
    home_frame.place(x=200,y=78) 

    home_label = customtkinter.CTkLabel(home_frame,text="Home" ,font=("Helvatica",30,"bold"),fg_color="#36CA03",text_color="black",width=1000,height=50,bg_color="#363538")
    home_label.place(x=0,y=0)

    

        #####Drop Down Box ####################

    myLabel = Label(home_frame,text="Select the type of Insect "  , font=("arial",20,"bold"), bg = "#E1E8E2").place(x= 0 ,  y = 100)

    insects = ["",
        "Caterpillar",
        "Locust     ",
        "Grasshopper"
    ]

    clicked_insect = StringVar()
    clicked_insect.set(insects[1])
            


    drop = OptionMenu(home_frame,clicked_insect, *insects , command=music)
    drop.config(width=45 , height = 2 )
    drop.place(x= 0 ,  y = 175)




    # drop down for frequency

    myLabel2 = Label(home_frame,text="Select the frequency " ,  font=("arial",20,"bold"), bg = "#E1E8E2").place(x= 550 ,  y = 100)
    song_paths = ["",
        "20kHz.mp3    ",
        "5kHz.mp3    ",
        "20Hz.mp3    ",
    ]


    clicked_frequency = StringVar()
    clicked_frequency.set(song_paths[1])


    drop = OptionMenu(home_frame,clicked_frequency, *song_paths  , command=music)
    drop.config(width=45 , height = 2 )
    drop.place(x= 550,  y = 175)



    # Drop Down for duration

    myLabel3 = Label(home_frame,text="Select the Duration " ,  font=("arial",20,"bold"), bg = "#E1E8E2").place(x= 0 ,  y = 300)


    options = ["",
        "30 minutes       ",
        "1 hour       ",
        "2 hour         "
    ]
    clicked = StringVar()
    clicked.set(options[1])
    def play():
        song_path = clicked_frequency.get().strip()  # Get the selected song path
        duration_text= clicked.get().strip()
        if song_path and duration_text:  # Ensure a valid song path is selected
            try:
                duration_minute=int(duration_text.split()[0])
                threading.Thread(target=play_song,args=(song_path,duration_minute),daemon=True).start()
            except ValueError:
                print("Error","Invalid")
    def pause():
            pygame.mixer.music.pause()
    




    drop = OptionMenu(home_frame,clicked, *options  , command=music)
    drop.config(width=40 , height = 2 )
    drop.place(x= 0 ,  y = 375)

    # submit button

    play_btn = customtkinter.CTkButton(home_frame,text="Play",width=100,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=play)
    play_btn.place(x=650,y=500)
    pause_btn = customtkinter.CTkButton(home_frame, text="Pause", width=100, height=40, border_width=0, border_spacing=0, font=("Helvetica", 20), fg_color="#363538", command=pause)
    pause_btn.place(x=350, y=500)




# function for chat tab
def chat_page():
    chat_frame = customtkinter.CTkFrame(home,width=1000,height=600,border_width=0,border_color="#016008",fg_color="black")
    chat_frame.place(x=200,y=100) 

    chat_label = customtkinter.CTkLabel(home,text="Chat-Bot" ,font=("Helvatica",30,"bold"),fg_color="#36CA03",text_color="black",width=1000,height=50,bg_color="#363538")
    chat_label.place(x=200,y=78)

    

    def start():
    # Start chat
        txt = customtkinter.CTkTextbox(chat_frame, width=1000, height=600)
        txt.place(x=0, y=0)
        txt.insert(tk.END, "\n" )
        entry = customtkinter.CTkEntry(chat_frame, placeholder_text="Hello User ! Please Enter a message", width=950,height=50)
        entry.place(x=0, y=510)
        main_button_1 = customtkinter.CTkButton(chat_frame, text="Send", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), width=95,height=50, command=lambda: Text(txt, entry)).place(x=905, y=510)

    def Text(txt, entry):
        # Process user input
        txt.configure(state="normal")
        text = entry.get()
        txt.insert(tk.END, "\n" + text)
        txt.configure(state="disabled")
        entry.delete(0, 'end')
        threading.Thread(target=chatting, args=(text,)).start()

    def chatting(text):
        # Placeholder function for your chat functionality
        print("Received message:", text)

    start()
    start.place(x=0,y=0)





home_btn = customtkinter.CTkButton(frame2,text="Home",width=100,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=home_page)
home_btn.place(x=200)

chat_btn = customtkinter.CTkButton(frame2,text="Chat-Bot",width=100,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=chat_page)
chat_btn.place(x=450)

about_btn = customtkinter.CTkButton(frame2,text="About Us",width=100,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538")
about_btn.place(x=700)

contact_btn = customtkinter.CTkButton(frame2,text="Contact Us",width=100,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538")
contact_btn.place(x=950)





###############################################################################################



home.mainloop()

       
       



