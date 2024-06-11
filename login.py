from tkinter import *
import customtkinter
from PIL import Image 

# Theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Creates the main window
root = customtkinter.CTk()
root.geometry('300x500')

# cget() returns the current value of the specified option.
def password_view():
    if entry_password.cget('show') == '*':
        entry_password.configure(show='')
        btn_eye.configure(image=img_hide)
    else: 
        btn_eye.configure(image=img_show)
        entry_password.configure(show='*')

frame_top = customtkinter.CTkFrame(root, fg_color="#B5F5FF")
frame_top.pack(side="top", fill="both", expand=True)
frame_middle = customtkinter.CTkFrame(root, fg_color="#DD5FDA")
frame_middle.pack(side="top", fill="both", expand=True)
frame_bottom = customtkinter.CTkFrame(root, fg_color="#FFCAEB")
frame_bottom.pack(side="top", fill="both", expand=True)

frame_middle1 = customtkinter.CTkFrame(frame_middle, fg_color="#B2AFBA")
frame_middle1.pack(side="top", fill="both", expand=True)
frame_middle2 = customtkinter.CTkFrame(frame_middle, fg_color="#B2AFBA")
frame_middle2.pack(side="top", fill="both", expand=True)

frame_middle1A = customtkinter.CTkFrame(frame_middle1, fg_color="#B2AFBA")
frame_middle1A.pack(side="top", fill="x", expand=False)
frame_middle1B = customtkinter.CTkFrame(frame_middle1, fg_color="#B2AFBA")
frame_middle1B.pack(side="top", fill="x", expand=False)
frame_middle2A = customtkinter.CTkFrame(frame_middle2, fg_color="#B2AFBA")
frame_middle2A.pack(side="top", fill="x", expand=False)
frame_middle2B = customtkinter.CTkFrame(frame_middle2, fg_color="#B2AFBA")
frame_middle2B.pack(side="top", fill="x", expand=False)

# Adds the logo
logo = customtkinter.CTkImage(light_image = Image.open('images/logo.png'), dark_image = Image.open('images/logo.png'), size=(200,200))
lbl_logo = customtkinter.CTkLabel(frame_top, image = logo)
lbl_logo.pack(pady=20)

# Fields where the users can insert their login information
lbl_email = customtkinter.CTkLabel(frame_middle1A, font=("Helvetica", 15), text = "Email")
lbl_email.pack(side="left", pady=0, padx=60)

entry_email = customtkinter.CTkEntry(frame_middle1B, placeholder_text = "example@mail.com")
entry_email.pack(side="left", pady=(0,5), padx=60)

lbl_password = customtkinter.CTkLabel(frame_middle2A, font=("Helvetica", 15), text = "Password")
lbl_password.pack(side="left", pady=0, padx=60)

entry_password = customtkinter.CTkEntry(frame_middle2B, placeholder_text = "*****", show="*")
entry_password.pack(side="left", pady=(0,5), padx=(60,10))

img_show = customtkinter.CTkImage(Image.open("images/show.png"),size=(20,20))
img_hide = customtkinter.CTkImage(Image.open("images/hide.png"),size=(20,20))
btn_eye = customtkinter.CTkButton(frame_middle2B, width=8, fg_color="#EBEBEB", image=img_show, text='', command=password_view)
btn_eye.pack(side="left", pady=0, padx=0)

# Button allows the users to submit their information
btn_submit = customtkinter.CTkButton(frame_bottom, fg_color="#D83215", hover_color="#ED5A41", width=100, height=30, font=("Helvetica", 15), text="Submit")
btn_submit.pack(pady=20)

root.mainloop()