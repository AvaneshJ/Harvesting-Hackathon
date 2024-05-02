from tkinter import *
import customtkinter as ctk
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

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

self = ctk.CTk()
self.title("Home Page")
self.geometry('1200x700+210+100')
self.grid_columnconfigure(0, weight=1)
self.grid_rowconfigure((0, 1), weight=1)


def start():
    # Start chat
    txt = ctk.CTkTextbox(self, width=800, height=580)
    txt.place(x=200, y=0)
    txt.insert(tk.END, "\n" )
    entry = ctk.CTkEntry(self, placeholder_text="Message SongGenie", width=400)
    entry.place(x=210, y=500)
    main_button_1 = ctk.CTkButton(self, text="Send", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), width=75, command=lambda: Text(txt, entry)).place(x=620, y=500)

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

self.mainloop()



