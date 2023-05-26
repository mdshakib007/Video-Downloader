from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pytube import YouTube

root = Tk()
root.title("Youtube Video Downloader")
root.geometry('900x500+100+50')
root.resizable(False, False)



def how_works():
    messagebox.showinfo("How it's work", "This is just a simple YouTube video downloader. You need to put video link in the entry widget and press 'information' to see details. Then press 'download' and 'yes' to download video in Highest resolution.")



def download_video():
    link = link_var.get()

    try:
        video = YouTube(link)
    except Exception as e:
        lbl_output.delete('1.0', END)
        lbl_output.insert(END, "[ Invalid Link ]")
        messagebox.showerror("Error", "Invalid YouTube link.\nPlease enter a valid link.")
        return

    txt = f"Title: '{video.title}'\n"

    if video.length is not None:
        txt += f"Length: {video.length // 60}m {video.length % 60}s\n"
    else:
        txt += "Length: N/A\n"

    if video.rating is not None:
        txt += f"Rating: {video.rating:.2f}/5.00\n"
    else:
        txt += "Rating: N/A\n"

    txt += f"Views: {video.views}"
    lbl_output.delete('1.0', END)
    lbl_output.insert(END, txt)

    while True:
        try:
            choice = messagebox.askquestion("Confirmation", "Do you want to download the video?")
            
            if choice == "yes":
                lbl_output.delete('1.0', END)
                lbl_output.insert(END, "[ Downloading. Please wait... ]")
                
                stream = video.streams.get_highest_resolution()
                stream.download()
                
                lbl_output.delete('1.0', END)
                lbl_output.insert(END, "[ Download complete. ]")
                break
            
            elif choice == "no":
                lbl_output.delete('1.0', END)
                lbl_output.insert(END, "[ Download canceled. ]")
                break
            
            else:
                lbl_output.delete('1.0', END)
                lbl_output.insert(END, "[ Download failed. ]")
                messagebox.showerror("Error", "Invalid input. Please select Yes or No.")
                
        except:
            lbl_output.delete('1.0', END)
            lbl_output.insert(END, "[ An error occurred. Download failed. ]")
            messagebox.showerror("Error", "An error occurred. Download failed.")
            break
    
def information():
    link = link_var.get()

    try:
        video = YouTube(link)
    except Exception as e:
        lbl_output.delete('1.0', END)
        lbl_output.insert(END, "[ Invalid Link ]")
        messagebox.showerror("Error", "Invalid YouTube link.\nPlease enter a valid link.")
        return

    txt = f"Title     : '{video.title}'\n"

    if video.length is not None:
        txt += f"Length : {video.length // 60}m {video.length % 60}s\n"
    else:
        txt += "Length : N/A\n"

    if video.rating is not None:
        txt += f"Rating  : {video.rating:.2f}/5.00\n"
    else:
        txt += "Rating  : N/A\n"

    txt += f"Views   : {video.views}"
    lbl_output.delete('1.0', END)
    lbl_output.insert(END, txt)
    
    
    
### how it's work
how = Button(root, text="How it's work?", command=how_works, cursor='hand2', relief='solid', borderwidth=0)
how.place(x=0, y=0)
    

# Configure background image
bg = Image.open('assets/bg1.png')
bg_resize = bg.resize((400, 400))
bg_resized = ImageTk.PhotoImage(image=bg_resize)
Label(root, image=bg_resized).place(x=70, y=30)

# Frame for entry and button
frame1 = Frame(root, height=375, width=375, borderwidth=5, background='#f07b5d')

Label(frame1, text='Enter Youtube Video Link: ', font='Roboto 16', background='#f07b5d').place(x=5, y=5)

link_var = StringVar()
link_entry = Entry(frame1, width=32, font='Roboto 13', textvariable=link_var)
link_entry.place(x=5, y=40)

# Button for download
btn_pic = Image.open('assets/dicon.png')
btn_res = btn_pic.resize((60, 60))
btn = ImageTk.PhotoImage(image=btn_res)
Button(frame1, image=btn, background='#f07b5d', cursor='hand2', command=download_video).place(x=70, y=90)
Label(frame1, text='Download', font='Roboto 10', background='#f07b5d').place(x=68, y=150)

# Button for show info
info_pic = Image.open('assets/info.png')
info_res = info_pic.resize((60, 60))
info = ImageTk.PhotoImage(image=info_res)
Button(frame1, image=info, background='#f07b5d', cursor='hand2', command=information).place(x=240, y=90)
Label(frame1, text='Information', font='Roboto 10', background='#f07b5d').place(x=235, y=150)

# Label for show output message
lbl_output = Text(frame1, font='Roboto 15', background='#f07b5d')
lbl_output.place(x=0, y=180)
lbl_output.insert(1.0, "[ This can provide you\nHighest Resolution of download ]")

frame1.place(x=500, y=30)



root.mainloop()
