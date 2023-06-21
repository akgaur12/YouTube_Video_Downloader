from tkinter import *
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import pytube
from pytube import YouTube

bg_color = "#D7D7D7"

#functons
def select_path():
    path = filedialog.askdirectory()
    if path=='':
        lbl_path.config(text='No Path Selected', font=("Bahnschrift", 11))
    else:
        lbl_path.config(text=path, font=("Bahnschrift", 11))

def download_video():
    global link, res_choice, lbl_path

    try:
        Link = str(link.get())
        user_path = lbl_path.cget('text')
        strm = int(res_choice.get())
        
        url = YouTube(Link)
        video = url.streams
        video[strm].download(user_path)

        messagebox.showinfo('Download', 'Video Downloaded Successfully')
        res_choice.set('')
        link.set('')

    except ValueError:
        messagebox.showwarning('Download', 'Please Paste Link and Select Resolution')
    except pytube.exceptions.RegexMatchError:
        messagebox.showwarning('Download', 'Invalid Video URL')
    except:
        messagebox.showwarning('Download', 'Check your Internet Connection')
        


root = Tk()
root.title("YouTube Video Downloader")
root.geometry("600x620+500+50")
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

btn_path = Button(root, text='Select Path', font=('', 12, 'bold'), bg="#404CEC", fg="white", relief='groove', command=select_path)
btn_path.place(x=400, y=318, height=30)

#setting resolution selection
lbl_res = [Label]*4
list = ['144p', '360p', '480p', '720p']
X = 120
for i in range(4):
    lbl_res[i] = Label(root, text=str(i)+' - '+list[i], font=('', 10),)
    lbl_res[i].place(x=X, y=390)
    X+=100

Label(root, text='Enter Resolution Choice: ', font=('', 12), bg=bg_color).place(x=180, y=445)

res_choice = StringVar()
en_res = Entry(root, font=('', 12), justify='center', textvariable=res_choice)
en_res.place(x=380, y=445, width=40, height=25)

#setting download button
btn_download = Button(
    root, text='Download', 
    font=('', 12, 'bold'), 
    bg='blue', 
    fg='white', 
    activebackground='#158F18', 
    activeforeground='#ffffff',
    relief='flat',
    command=download_video
)
btn_download.place(x=200, y=525, width=200, height=40)

lbl = Label(root, text="Akash Gaur", font=("Harlow Solid Italic", 10), bg='#D7D7D7').place(x=520, y=595)

root.mainloop()

