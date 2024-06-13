from pytube import YouTube, exceptions
import tkinter
import customtkinter
from PIL import Image

# adding theme for the app
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# adding app title and geometry
app = customtkinter.CTk()
app.geometry("720x580")
app.title("TuneTap")

#defining functions
def download_video():
    try:
        video_url = url_area.get()
        yt = YouTube(video_url)
        video_name = yt.title
        yt.streams.filter(progressive=True).first().download(output_path='Downloads', filename=f'{video_name}.mp4', skip_existing=True, max_retries=0)
        url_area.delete(0, tkinter.END)
        result_area.configure(text="Download Completed..", text_color="green")
        
    except:
        result_area.configure(text="Invalid URL", text_colour="red")
        url_area.delete(0, tkinter.END)
    

# providing font style for title and description 
title_font = customtkinter.CTkFont(family='Helvetica', size=44, weight="bold")
dec_font = customtkinter.CTkFont(family="Ariel", size=10, weight="normal", slant="roman")
btn_font = customtkinter.CTkFont(family="Ariel", size=20, weight="normal")
result_font = customtkinter.CTkFont(family="Ariel", size=18, slant="roman")

# title and description of the app
title = customtkinter.CTkLabel(app, text="TuneTap", height=100, width=100, font=title_font)
title.pack()
desc = customtkinter.CTkLabel(app, text="TuneTap is an YouTube Video/Audio downloader feel free to use it", font=dec_font, height=20, width=20)
desc.pack()

# adding URL area
url = tkinter.StringVar()
url_area = customtkinter.CTkEntry(app, width=400, corner_radius=3, placeholder_text="Enter the URL:", textvariable=url)
url_area.pack()

# adding combo box
# combo_box1 = customtkinter.CTkComboBox(app, values="", corner_radius=1, command=download_video)
# combo_box1.pack(pady=10)

# adding button for the application
dowmload_btn = customtkinter.CTkButton(app, text="Download", hover_color="green", corner_radius=4, font=btn_font, height=40, width=200, command=download_video)
dowmload_btn.pack(padx=55, pady=55)

# results area
result_area = customtkinter.CTkLabel(app,text="", font=result_font, text_color="red")
result_area.pack(pady=110)
app.mainloop()