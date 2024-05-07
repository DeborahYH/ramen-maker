from tkinter import *
import customtkinter
from PIL import Image 

# Theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Creates the main window
root = customtkinter.CTk()
root.geometry('1000x900')
root.resizable(False,False)

# Adds the logo
logo = customtkinter.CTkImage(light_image = Image.open('images/logo.png'), dark_image = Image.open('images/logo.png'), size=(200,200))
lbl_logo = customtkinter.CTkLabel(root, image = logo)
lbl_logo.pack(pady=20)

# Shows the welcome text
lbl_welcome = customtkinter.CTkLabel(root, font=("Helvetica", 25), text = "Welcome!")
lbl_welcome.pack(pady=5)

lbl_welcome_text = customtkinter.CTkLabel(root, wraplength = 600, font=("Helvetica", 15), justify = "left", text = "Curabitur eget dui ac magna laoreet lacinia. Donec egestas nunc et nulla hendrerit, eget ultricies sem tempor. Phasellus ut maximus turpis. Pellentesque ac faucibus sem. Morbi tincidunt diam nec sapien lobortis, vel congue dolor consequat. Integer ut turpis id sapien interdum semper in eu risus. In vestibulum nibh id risus cursus bibendum. Pellentesque efficitur quis lacus ut tristique.")
lbl_welcome_text.pack(pady=5, padx=20)

# Buttons appear only after the user finishes selecting the food items 
btn_here = customtkinter.CTkButton(root, fg_color="#D83215", hover_color="#ED5A41", width=100, height=30, font=("Helvetica", 15), text = "Eat Here", command = "eat_here")
btn_here.pack(pady=10)
btn_here.place(x=300, y=400)

btn_take_out = customtkinter.CTkButton(root, fg_color="#D83215", hover_color="#ED5A41", width=100, height=30, font=("Helvetica", 15), text = "Take Out", command = "Take_Out")
btn_take_out.pack(pady=10)
btn_take_out.place(x=450, y=400)

btn_delivery = customtkinter.CTkButton(root, fg_color="#D83215", hover_color="#ED5A41", width=100, height=30, font=("Helvetica", 15), text = "Delivery", command = "Delivery")
btn_delivery.pack(pady=10)
btn_delivery.place(x=600, y=400)

root.mainloop()