from tkinter import *
import customtkinter 
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from ttkthemes import themed_tk
from PIL import Image, ImageTk
from tkinter import filedialog
from mutagen.mp3 import MP3
import os
import time
import pygame
import threading
import datetime
import time
import music_player

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

self = customtkinter.CTk()
self.title("Home Page")
self.geometry('1200x700+210+100')
self.grid_columnconfigure(0, weight=1)
self.grid_rowconfigure((0, 1), weight=1)
pygame.mixer.init()


my_image = customtkinter.CTkImage(light_image=Image.open('gradient2.png'),dark_image=Image.open('gradient2.png'),size=(1500,700))

image_label = customtkinter.CTkLabel(self,text="",image=my_image)
image_label.place(x=0,y=0)




main_frame = customtkinter.CTkFrame(master=self,width=1000,height=600,corner_radius=0,border_width=0,border_color="#808080",fg_color="#363538")
main_frame.place(x=155,y=85) 

textbox =customtkinter.CTkTextbox(main_frame,width=1000,height =600,font=("Helvatica",20),bg_color="#4F5151")
textbox.place(x=0,y=0)

text ="""                                                                        Welcome to Tech-Veda 
Namaste ! Welcome to Tech-Veda, your digital gateway to the world of agriculture! We are thrilled to welcome you to our online platform dedicated to all things agriculture. Whether you're a seasoned farmer, an aspiring gardener, or simply curious about the wonders of the agricultural world, you've come to the right place.

At Tech-Veda, we're committed to providing you with a wealth of resources, insights, and tools to help you navigate the ever-changing landscape of agriculture. From expert tips on crop cultivation and livestock management to in-depth articles on sustainable farming practices and the latest industry trends, we've got you covered.

Explore our diverse range of content, engage with fellow enthusiasts in our vibrant community forums, and discover innovative solutions to enhance your agricultural endeavors. Whether you're looking to grow your knowledge, expand your skills, or connect with like-minded individuals, Tech-Veda is your trusted partner every step of the way.

Join us as we embark on a journey to celebrate the rich heritage, embrace the challenges, and unlock the endless possibilities of agriculture together. Welcome to Tech-Veda—where passion meets purpose, and the seeds of knowledge are sown for a greener, more sustainable future.


"""


textbox.insert("0.0",text)


# switchng frames from the toggle menu

def home_page():
    home_frame = customtkinter.CTkFrame(main_frame,width=1000,height=600,border_width=0,corner_radius=2,border_color="#808080",fg_color="#363538")
    home_frame.place(x=0,y=0) 
    
    home_label = customtkinter.CTkLabel(main_frame,text="This is the home page " ,font=("Helvatica",20),fg_color="#363538",width=300,height=50,bg_color="#363538")
    home_label.place(x=150,y=150)

    new_win_btn = customtkinter.CTkButton(home_frame,text="Submit",command=new)
    new_win_btn.place(x=450,y=450)

    textbox =customtkinter.CTkTextbox(main_frame,width=1000,height =600,font=("Helvatica",20),bg_color="#4F5151")
    textbox.place(x=0,y=0)

    text =""""""


    textbox.insert("0.0",text)




    

def chat_page():
    chat_frame = customtkinter.CTkFrame(main_frame,width=1000,height=600,border_width=0,border_color="#016008",fg_color="black")
    chat_frame.place(x=0,y=40) 

    chat_label = customtkinter.CTkLabel(main_frame,text="Chat-Bot" ,font=("Helvatica",30,"bold"),fg_color="#36CA03",text_color="black",width=1000,height=50,bg_color="#363538")
    chat_label.place(x=0,y=0)

    

    def start():
    # Start chat
        txt = customtkinter.CTkTextbox(chat_frame, width=1000, height=600)
        txt.place(x=0, y=0)
        txt.insert(tk.END, "\n" )
        entry = customtkinter.CTkEntry(chat_frame, placeholder_text="Hello User ! Please Enter a message", width=950,height=50)
        entry.place(x=0, y=480)
        main_button_1 = customtkinter.CTkButton(chat_frame, text="Send", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), width=95,height=50, command=lambda: Text(txt, entry)).place(x=900, y=480)

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



def about_page():
    about_frame = customtkinter.CTkFrame(main_frame,width=1000,height=600,border_width=0,border_color="#808080",fg_color="#363538")
    about_frame.place(x=0,y=0) 

    about_us_label = customtkinter.CTkLabel(main_frame,text="About Us" ,font=("Bahnschrift SemiLight Condensed",30,"bold"),fg_color="#36CA03",text_color="black",width=1000,height=50,bg_color="#363538")
    about_us_label.place(x=0,y=0)

    about_label = customtkinter.CTkLabel(main_frame,text=" About Us Page" ,font=("Bahnschrift SemiLight Condensed",30,"bold"),text_color="black",width=1000,height=100,bg_color="#363538")
    about_label.place(x=0,y=50)

    textbox =customtkinter.CTkTextbox(main_frame,width=1000,height =600,font=("Helvatica",20),)
    textbox.place(x=0,y=0)

    text ="""                                                                            About Us
Welcome to Tech-Veda , where agriculture meets convenience! We are a passionate team dedicated to revolutionizing the conventional ways of agriculture , by combining mordern technologies with the core values of agriculture. At Tech-Veda, we believe in the power of technology to simplify everyday tasks, enhance productivity, and bring people closer together. Our journey began with a simple yet profound vision: to create an app that seamlessly integrates into your life, providing intuitive solutions to common challenges while fostering connection and community.

Driven by a shared commitment to excellence and a deep understanding of user needs, our diverse team of developers, designers, and visionaries has poured countless hours into crafting an app that exceeds expectations. Our goal is not just to meet your needs, but to anticipate them, offering features and functionality that anticipate your desires before you even realize them.

But Tech-Veda is more than just a product—it's a reflection of our values and our dedication to making a positive impact. We believe in accessibility, inclusivity, and sustainability, striving to create an app that is not only user-friendly but also environmentally conscious. Through ongoing research and development, we are committed to staying at the forefront of technological advancements, ensuring that Tech-eda remains relevant and valuable in an ever-evolving digital landscape.

At Tech-Veda , we pride ourselves on our unwavering commitment to customer satisfaction. Your feedback is not only welcomed but actively sought after, as we believe that collaboration is key to continual improvement. Whether you're a seasoned tech enthusiast or a first-time user, we are here to support you every step of the way, offering responsive customer service and comprehensive resources to address any questions or concerns you may have.

As we look to the future, our vision for Tech-Veda remains clear: to empower individuals, businesses, and communities to thrive in a rapidly changing world. Thank you for joining us on this journey—we couldn't do it without you!
    
Commited to growing green fields and a sustainable future.


    """


    textbox.insert("0.0",text)


def contact_page():
    contact_frame = customtkinter.CTkFrame(main_frame,width=1000,height=600,border_width=0,border_color="#808080",fg_color="#363538")
    contact_frame.place(x=0,y=0) 

    contact_label = customtkinter.CTkLabel(main_frame,text="This is the contact page " ,font=("Helvatica",20),fg_color="#363538",width=300,height=50,bg_color="#363538")
    contact_label.place(x=350,y=350)

    textbox =customtkinter.CTkTextbox(main_frame,width=1000,height =600,font=("Helvatica",20))
    textbox.place(x=0,y=0)

    text = """                                                                           Contact Us

We’re thrilled to connect with you! Whether you have questions, feedback, or just want to say hello, feel free to 
reach out. Our team is here to assist you.You can drop us a message using the form below or directly email us
at info@example.com. We promise to get back to you promptly. Thank you for choosing us!


Email : 

Phone :

    """
    textbox.insert("0.0",text)





# function for toggle menu
def toggle_menu():

    def collapse_toggle_menu():
        toggle_mn_frame.destroy()
        toggle_button = customtkinter.CTkButton(self,text="☰",width=50,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=toggle_menu)
        toggle_button.place(x=0,y=35)
##############################################################


    window_height = 700

    toggle_mn_frame = customtkinter.CTkFrame(master=self,width=200,height=window_height,border_width=0,border_color="#808080",fg_color="#363538")
    toggle_mn_frame.place(x=0,y=78)

    home_button = customtkinter.CTkButton(toggle_mn_frame,text="Home",width=200,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=home_page)
    home_button.place(x=0,y=50)
    home_indicator = customtkinter.CTkLabel(toggle_mn_frame,text="" ,fg_color="#363538",width=5,height=40,bg_color="#363538")
    home_indicator.place(x=0,y=50)

    
    chat_button = customtkinter.CTkButton(toggle_mn_frame,text="Chat Bot",width=200,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=chat_page)
    chat_button.place(x=0,y=150)
    chat_indicator = customtkinter.CTkLabel(toggle_mn_frame,text="" ,fg_color="#363538",width=5,height=40,bg_color="#363538")
    chat_indicator.place(x=0,y=150)
    
    
    about_button = customtkinter.CTkButton(toggle_mn_frame,text="About Tech Veda",width=200,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=about_page)
    about_button.place(x=0,y=250)
    about_indicator = customtkinter.CTkLabel(toggle_mn_frame,text="" ,fg_color="#363538",width=5,height=40,bg_color="#363538")
    about_indicator.place(x=0,y=250)

    
    contact_button = customtkinter.CTkButton(toggle_mn_frame,text="Contact Us",width=200,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=contact_page)
    contact_button.place(x=0,y=350)
    contact_indicator = customtkinter.CTkLabel(toggle_mn_frame,text="" ,fg_color="#363538",width=5,height=40,bg_color="#363538")
    contact_indicator.place(x=0,y=350)


    toggle_button = customtkinter.CTkButton(self,text="X",width=50,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=collapse_toggle_menu)
    toggle_button.place(x=0,y=35)
 


# top frame
frame1 = customtkinter.CTkFrame(master=self,width=1500,height=33,border_width=0,border_color="#808080",fg_color="#363538")
frame1.place(x=0,y=0)
name = customtkinter.CTkLabel(self,text="Tech Veda" ,fg_color="#363538", text_color="#EEEDF4",  font=("Arial Rounded MT Bold",20),width=200,height=33)
name.place(x=550,y=0)
# 

# toggle menu bar
frame2 = customtkinter.CTkFrame(master=self,width=1500,height=45,border_width=1,border_color="#808080",fg_color="#363538")
frame2.place(x=0,y=33)
all = customtkinter.CTkLabel(self,text="All" ,fg_color="#363538", text_color="#EEEDF4",  font=("Arial Rounded MT Bold",20),width=100,height=40)
all.place(x=20,y=35)

toggle_button = customtkinter.CTkButton(self,text="☰",width=50,height = 40,border_width=0,border_spacing=0,font=("Helvatica",20),fg_color="#363538",command=toggle_menu)
toggle_button.place(x=0,y=35)



def new():
    

    new_win = customtkinter.CTkToplevel(self)
    new_win.title("This is a new window")
    new_win.geometry("700*500")
    new_win.maxsize(width=750,height=550)
    new_win.minsize(width=540,height=550)

    background = "#013054"
    bg="black"


    # Buttton Images
    pause_icon = Image.open('images/pause.png')
    pause_icon = pause_icon.resize((90, 90))
    pause_icon = ImageTk.PhotoImage(pause_icon)
    
    play_icon = Image.open('images/play.png')
    play_icon = play_icon.resize((90, 90))
    play_icon = ImageTk.PhotoImage(play_icon)

    stop_icon = Image.open('images/stop.png')
    stop_icon = stop_icon.resize((90, 90))
    stop_icon = ImageTk.PhotoImage(stop_icon)

    speaker_icon = Image.open('images/speaker.png')
    speaker_icon = speaker_icon.resize((50, 50))
    speaker_icon = ImageTk.PhotoImage(speaker_icon)
    
    
    # add_song_icon = Image.open('images/song.png')
    # add_song_icon = add_song_icon.resize((25, 25))
    # add_song_icon = ImageTk.PhotoImage(add_song_icon)

    # delete_icon = Image.open('images/delete2.png')
    # delete_icon = delete_icon.resize((25, 25))
    # delete_icon = ImageTk.PhotoImage(add_song_icon)

    # delete_all_icon = Image.open('images/delete.png')
    # delete_all_icon = delete_all_icon.resize((25, 25))
    # delete_all_icon = ImageTk.PhotoImage(delete_all_icon)


    
    # Creating Buttons ,listboxes and labels
    
    background = customtkinter.CTkImage(light_image=Image.open('musicbg.jpeg'),dark_image=Image.open('musicbg.jpeg'),size=(1500,700))

    background_image = customtkinter.CTkLabel(new_win,text="",width=1500,height=700,image=background)
    background_image.place(x=0,y=0)

    song_list = customtkinter.CTkTextbox(new_win, width=100, height=1000)
    song_list.place(x=2000, y=2000)

    control_panel = customtkinter.CTkLabel(new_win,text="",height=500,width=1020)
    control_panel.place(x=0,y=400)

    time_elapsed = customtkinter.CTkLabel(new_win,text="00:00" ,fg_color="#363538", text_color="white",  font=("Arial Rounded MT Bold",20),width=100,height=20)
    time_elapsed.place(x=10,y=400)

    song_duration = customtkinter.CTkLabel(new_win,text="00:00" ,fg_color="#363538", text_color="white",  font=("Arial Rounded MT Bold",20),width=100,height=20)
    song_duration.place(x=660,y=400)


    progress_scale = ttk.Scale(new_win,orient="horizontal",style='TScale',from_=0,length=800,
                                       cursor='hand2')
    progress_scale.place(x=170,y=600)


    play_button = tk.Button(new_win,text="",image=play_icon
                                     )
    play_button.place(x=500,y=650)

    pause_button = tk.Button(new_win,text="",image=pause_icon
                                     )
    pause_button.place(x=400,y=650)

    stop_button = tk.Button(new_win,text="",image=stop_icon
                                     )
    stop_button.place(x=600,y=650)

    speaker_button = tk.Button(new_win,text="",image=speaker_icon,
                               )
    speaker_button.place(x=880,y=700)


    volume_scale = ttk.Scale(new_win,orient="horizontal",style='TScale',from_=0,to=100,
                                       cursor='hand2')
    volume_scale.place(x=950,y=718)


    # adding songs to playlist


    menubar = Menu(new_win)
    new_win.config(menu=menubar)

    songs =[]
    current_song = ""
    paused=False

    def load_music():
        global current_song
        new_win.directory = filedialog.askdirectory()

        for song in os.listdir(new_win.directory):
            name,ext = os.path.splitext(song)
            if ext == ".mp3":
                songs.append(song)

        for song in songs:
            songlist.insert("end",song)
    
        songlist.selection_set(0)
        current_song=songs[songlist.curselection()[0]]

    def play_music():
        global current_song,paused

        if not paused:
            pygame.mixer.music.load
            (os.path.join(new_win.director,current_song))
            pygame.mixer.music.play()

        else:
            pygame.mixer.music.unpause()
            paused = False

    def pause_music():
        global paused

        pygame.mixer.music.pause()
        paused = True
    
    organise_menu = Menu(menubar, tearoff=False)
    organise_menu.add_command(label="Select Song",command=load_music)
    menubar.add_cascade(label='Organise',menu=organise_menu)


    songlist = Listbox(new_win,bg="black",fg="white",width=100,height=15)
    songlist.place(x=1000,y=1000)

    

















# Custom tkinter
    play_button_new_win_btn = customtkinter.CTkButton(new_win,text="",image=play_icon,height=60,width=60)
    play_button_new_win_btn.place(x=500,y=650)

    pause_button_new_win_btn = customtkinter.CTkButton(new_win,text="",image=pause_icon,height=60,width=60)
    pause_button_new_win_btn.place(x=400,y=650)

    stop_button_new_win_btn = customtkinter.CTkButton(new_win,text="",image=stop_icon,height=60,width=60)
    stop_button_new_win_btn.place(x=600,y=650)

    speaker_button_new_win_btn = customtkinter.CTkButton(new_win,text="",image=speaker_icon,height=60,width=60)
    speaker_button_new_win_btn.place(x=880,y=700)









    self.status = tk.Label(new_win,text="Playing : ---------- Song : 0 of 0",fg="black",anchor="w",background="grey",
                               font="lucida 9 bold",bd=5,relief="ridge")
    self.status.place(x=0,y=800,relwidth=1)


    # menu = tk.Menu(new_win)
    # new_win.configure(menu=menu)


    


    
















# new_win_btn = customtkinter.CTkButton(home_frame,text="open a new window",command=new)
# new_win_btn.place(x=200,y=200)

















































self.mainloop()