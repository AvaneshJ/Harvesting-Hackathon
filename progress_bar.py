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
home.title("Home Page")
home.geometry('1200x700+210+100')
home.configure(bg="#E1E8E2")
home.resizable(True,True)




# Add song function

def add_song():
    pass






#  create menu
my_menu = Menu(home)
home.config(menu=my_menu)

    #  add add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs",menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To playlist",command=add_song)












home.mainloop()