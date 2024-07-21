import ctypes
import platform

import tkinter as tk
from tkinter import *
import customtkinter as ctk
import ttkbootstrap as ttk

class App(ttk.Window):
    def __init__(self, title, size):
        super().__init__(themename="darkly")
        
        if platform.system() == "Windows":
            ctypes.windll.shcore.SetProcessDpiAwareness(True)
            
        self.title(title)
        
        window_width = size[0]
        window_height = size[1]
        display_width = self.winfo_screenwidth()
        display_height = self.winfo_screenheight()
        
        window_width = min(window_width, int(0.8 * display_width))
        window_height = min(window_height, int(0.8 * display_height))
        
        left = int(display_width / 2 - window_width / 2)
        top = int(display_height / 2 - window_height / 2)
        
        
        self.geometry(f'{window_width}x{window_height}+{left}+{top}')
        self.minsize(size[0],size[1])
        self.resizable(True, True)
        
        self.mainloop()
        
App("Calculator", (600,800))
        