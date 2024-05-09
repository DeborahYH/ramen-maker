from tkinter import *
import customtkinter
from PIL import Image 

# Theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Creates the main window
root = customtkinter.CTk()
root.geometry('300x500')

# Adds the logo
logo = customtkinter.CTkImage(light_image = Image.open('images/logo.png'), dark_image = Image.open('images/logo.png'), size=(200,200))
lbl_logo = customtkinter.CTkLabel(root, image = logo)
lbl_logo.pack(pady=10)

# Fields where the users can insert their login information
lbl_email = customtkinter.CTkLabel(root, text = "Email")
lbl_email.pack(pady=5)

entry_email = customtkinter.CTkEntry(root, placeholder_text = "example@mail.com")
entry_email.pack(pady=5)

lbl_password = customtkinter.CTkLabel(root, text = "Password")
lbl_password.pack(pady=5)

entry_password = customtkinter.CTkEntry(root, placeholder_text = "*****", show="*")
entry_password.pack(pady=5)

# Button allows the users to submit their information
btn_submit = customtkinter.CTkButton(root, text="Submit")
btn_submit.pack(pady=10)

root.mainloop()