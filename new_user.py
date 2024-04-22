from tkinter import *
import customtkinter
from PIL import Image 

# Theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Creates the main window
root = customtkinter.CTk()
root.geometry('1000x850')

# Adds the logo
logo = customtkinter.CTkImage(light_image = Image.open('images/logo.png'), dark_image = Image.open('images/logo.png'), size=(200,200))
lbl_logo = customtkinter.CTkLabel(root, image = logo)
lbl_logo.pack(pady=10)

# Shows the welcome text
lbl_welcome = customtkinter.CTkLabel(root, font=("Helvetica", 25), text = "Welcome!")
lbl_welcome.pack(pady=15)

# Entry fields
lbl_name = customtkinter.CTkLabel(root, font=("Helvetica", 14), anchor="w", justify="left", text = "Name")
lbl_name.pack(pady=0)
entry_name = customtkinter.CTkEntry(root, width=250, placeholder_text="Insert your name here")
entry_name.pack(pady=10)

lbl_birth = customtkinter.CTkLabel(root, font=("Helvetica", 14), anchor="w", justify = "left", text = "Birth Date")
lbl_birth.pack(pady=0)
entry_birth = customtkinter.CTkEntry(root, width=250, placeholder_text="")
entry_birth.pack(pady=10)

lbl_phone = customtkinter.CTkLabel(root, font=("Helvetica", 14), anchor="w", justify = "left", text = "Phone")
lbl_phone.pack(pady=0)
entry_phone = customtkinter.CTkEntry(root, width=250, placeholder_text="")
entry_phone.pack(pady=10)

lbl_address = customtkinter.CTkLabel(root, font=("Helvetica", 14), anchor="w", justify = "left", text = "Address")
lbl_address.pack(pady=0)
entry_address = customtkinter.CTkEntry(root, width=250, placeholder_text="")
entry_address.pack(pady=10)

lbl_email = customtkinter.CTkLabel(root, font=("Helvetica", 14), anchor="w", justify = "left", text = "Email")
lbl_email.pack(pady=0)
entry_email = customtkinter.CTkEntry(root, width=250, placeholder_text="")
entry_email.pack(pady=10)

lbl_password = customtkinter.CTkLabel(root, font=("Helvetica", 14), anchor="w", justify = "left", text = "Password")
lbl_password.pack(pady=0)
entry_password = customtkinter.CTkEntry(root, width=250, placeholder_text="")
entry_password.pack(pady=10)

# Button to submit user information
btn_submit = customtkinter.CTkButton(root, text = "New User", command = "submit")
btn_submit.pack(pady=15)

root.mainloop()