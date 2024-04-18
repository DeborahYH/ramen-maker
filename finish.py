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

lbl_goodbye = customtkinter.CTkLabel(root, text = "Thank you for shopping with us.\nYour order number is [000].\nEnjoy!")
lbl_goodbye.pack(pady=10)

food_icon = customtkinter.CTkImage(light_image = Image.open('images/ramen-s.png'), dark_image = Image.open('images/ramen-s.png'), size=(50,50))
lbl_food_icon = customtkinter.CTkLabel(root, image = food_icon, text="")
lbl_food_icon.pack(pady=10)

root.mainloop()