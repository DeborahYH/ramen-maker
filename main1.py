from tkinter import *
import customtkinter
from PIL import Image 

# Theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Creates the main window
root = customtkinter.CTk()
root.geometry('800x600')
root.resizable(False,False)

frame_t = customtkinter.CTkFrame(root)
frame_t.pack(side="top", fill="both", expand=True)
frame_m = customtkinter.CTkFrame(root)
frame_m.pack(side="top", fill="both", expand=True)
frame_b = customtkinter.CTkFrame(root)
frame_b.pack(side="top", fill="both", expand=True)

# Adds the logo
logo = customtkinter.CTkImage(light_image = Image.open('images/logo.png'), dark_image = Image.open('images/logo.png'), size=(200,200))
lbl_logo = customtkinter.CTkLabel(frame_t, text="", image = logo)
lbl_logo.place(relx = 0.5, rely = 0.6, anchor = 'center')

# Shows the welcome text
lbl_welcome = customtkinter.CTkLabel(frame_m, font=("Helvetica", 25), text = "Welcome!")
lbl_welcome.place(relx = 0.5, rely = 0.25, anchor = 'center')

lbl_welcome_text = customtkinter.CTkLabel(frame_m, wraplength = 600, font=("Helvetica", 15), justify = "left", text = "Curabitur eget dui ac magna laoreet lacinia. Donec egestas nunc et nulla hendrerit, eget ultricies sem tempor. Phasellus ut maximus turpis. Pellentesque ac faucibus sem. Morbi tincidunt diam nec sapien lobortis, vel congue dolor consequat. Integer ut turpis id sapien interdum semper in eu risus. In vestibulum nibh id risus cursus bibendum. Pellentesque efficitur quis lacus ut tristique.")
lbl_welcome_text.place(relx = 0.5, rely = 0.7, anchor = 'center')

# Buttons give 2 options
btn_login = customtkinter.CTkButton(frame_b, fg_color="#D83215", hover_color="#ED5A41", width=100, height=30, font=("Helvetica", 15), text = "Login", command = "login")
btn_login.place(relx = 0.35, rely = 0.1)

btn_new_user = customtkinter.CTkButton(frame_b, fg_color="#D83215", hover_color="#ED5A41", width=100, height=30, font=("Helvetica", 15), text = "New User", command = "create_user")
btn_new_user.place(relx = 0.52, rely = 0.1)

root.mainloop()