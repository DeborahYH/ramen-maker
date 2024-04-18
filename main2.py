from tkinter import *
import customtkinter
from PIL import Image 

# Theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Creates the main window
root = customtkinter.CTk()
root.geometry('1000x1000')

# Adds the logo
logo = customtkinter.CTkImage(light_image = Image.open('images/logo.png'), dark_image = Image.open('images/logo.png'), size=(200,200))
lbl_logo = customtkinter.CTkLabel(root, image = logo)
lbl_logo.pack(pady=20)

# Shows the welcome text
lbl_welcome = customtkinter.CTkLabel(root, font=("Helvetica", 20), text = "Welcome!")
lbl_welcome.pack(pady=20)

lbl_welcome_text = customtkinter.CTkLabel(root, wraplength = 600, font=("Helvetica", 14), justify = "left", text = "Curabitur eget dui ac magna laoreet lacinia. Donec egestas nunc et nulla hendrerit, eget ultricies sem tempor. Phasellus ut maximus turpis. Pellentesque ac faucibus sem. Morbi tincidunt diam nec sapien lobortis, vel congue dolor consequat. Integer ut turpis id sapien interdum semper in eu risus. In vestibulum nibh id risus cursus bibendum. Pellentesque efficitur quis lacus ut tristique.")
lbl_welcome_text.pack(pady=20, padx=20)

# Buttons appear only after the user finishes selecting the food items 
btn_here = customtkinter.CTkButton(root, text = "Eat Here", command = "eat_here")
btn_here.pack(pady=10)

btn_take_out = customtkinter.CTkButton(root, text = "Take Out", command = "Take_Out")
btn_take_out.pack(pady=10)

btn_delivery = customtkinter.CTkButton(root, text = "Delivery", command = "Delivery")
btn_delivery.pack(pady=10)

# Creates tabs
tabs = customtkinter.CTkTabview(root)
tabs.pack(pady=10)

tab_1 = tabs.add("Base")
tab_2 = tabs.add("Toppings")
tab_3 = tabs.add("Appetizers")
tab_4 = tabs.add("Beverages")
tab_5 = tabs.add("Dessert")
tab_6 = tabs.add("Cart")
tab_7 = tabs.add("Logout")

root.mainloop()