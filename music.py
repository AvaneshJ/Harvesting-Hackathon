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




home= Tk()
home.title("Music player")
home.geometry('1200x700+210+100')

pygame.mixer.init()


menubar = Menu(home)
home.config(menu=menubar)

songs =[]
current_song = ""
paused=False


def load_music():
    global current_song
    home.directory = filedialog.askdirectory()

    for song in os.listdir(home.directory):
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
        (os.path.join(home.director,current_song))
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


songlist = Listbox(home,bg="black",fg="white",width=100,height=15)
songlist.pack()

play_btn_img = PhotoImage(file='play.png')
pause_btn_img = PhotoImage(file='pause.png')



control_frame = Frame(home)
control_frame.pack()


play_btn = Button(control_frame,image=play_btn_img,borderwidth=0,command=play_music)
pause_btn = Button(control_frame,image=pause_btn_img,borderwidth=0,command=pause_music)



play_btn.grid(row=0,column=1,padx=7,pady=10)
pause_btn.grid(row=0,column=2,padx=7,pady=10)











home.mainloop()