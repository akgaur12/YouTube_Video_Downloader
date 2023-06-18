from tkinter import *
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import pytube
from pytube import YouTube

bg_color = "#D7D7D7"

root = Tk()
root.title("YouTube Video Downloader")
root.geometry("600x650+500+50")
root.iconbitmap("logo.ico")
root.resizable(0,0)
root.config(bg=bg_color)
