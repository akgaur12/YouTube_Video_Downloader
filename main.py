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

#setting heading image
img = Image.open("heading.png")
resize_img = img.resize((360,110))
img_heading = ImageTk.PhotoImage(resize_img)
lbl_hading_img = Label(root, image=img_heading).place(x=130, y=25)
lbl_heading2 = Label(root, text='Video Downloader', font=('', 17, 'bold'), fg='red', bg=bg_color).place(x=215, y=140)

#setting title
Label(root, text='Paste Video Link to Download', font=('', 14), fg='blue', bg=bg_color).place(x=180, y=210)
Label(root, text='Link-', font=('', 14), bg=bg_color).place(x=78, y=250)

#setting link entry
link = StringVar()
en_link = Entry(root, font=('', 11),justify='center' , textvariable=link)
en_link.place(x=122, y=250, width=400, height=30)

#setting download path
lbl_path = Label(root, text='Please Select Download Path', font=('Bahnschrift', 12), bg=bg_color)
lbl_path.place(x=100, y=320)
