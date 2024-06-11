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


# Adds the logo
logo = customtkinter.CTkImage(light_image = Image.open('images/logo.png'), dark_image = Image.open('images/logo.png'), size=(200,200))
lbl_logo = customtkinter.CTkLabel(root, image = logo)
lbl_logo.pack(pady=10)

# Fields where the users can insert their login information
lbl_email = customtkinter.CTkLabel(root, font=("Helvetica", 15), text = "Email")
lbl_email.pack(pady=5)

entry_email = customtkinter.CTkEntry(root, placeholder_text = "example@mail.com")
entry_email.pack(pady=5)

lbl_password = customtkinter.CTkLabel(root, font=("Helvetica", 15), text = "Password")
lbl_password.pack(pady=5)

entry_password = customtkinter.CTkEntry(root, placeholder_text = "*****", show="*")
entry_password.pack(pady=5)

img_show = customtkinter.CTkImage(Image.open("images/show.png"),size=(20,20))
img_hide = customtkinter.CTkImage(Image.open("images/hide.png"),size=(20,20))
btn_eye = customtkinter.CTkButton(root, width=8, fg_color="#EBEBEB", image=img_show, text='', command=password_view)
btn_eye.pack(pady=5)

# Button allows the users to submit their information
btn_submit = customtkinter.CTkButton(root, fg_color="#D83215", hover_color="#ED5A41", width=100, height=30, font=("Helvetica", 15), text="Submit")
btn_submit.pack(pady=10)

root.mainloop()