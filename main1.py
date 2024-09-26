from tkinter import *
import customtkinter
from PIL import Image 

# Theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry('800x600')
        self.resizable(False, False)

        self.frame_t = customtkinter.CTkFrame(self)
        self.frame_t.pack(side="top", fill="both", expand=True)
        self.frame_m = customtkinter.CTkFrame(self)
        self.frame_m.pack(side="top", fill="both", expand=True)
        self.frame_b = customtkinter.CTkFrame(self)
        self.frame_b.pack(side="top", fill="both", expand=True)

        # Adds the logo
        self.logo = customtkinter.CTkImage(light_image = Image.open('images/logo.png'), dark_image = Image.open('images/logo.png'), size=(200,200))
        self.lbl_logo = customtkinter.CTkLabel(self.frame_t, text="", image = self.logo)
        self.lbl_logo.place(relx = 0.5, rely = 0.6, anchor = 'center')

        # Shows the welcome text
        self.lbl_welcome = customtkinter.CTkLabel(self.frame_m, font=("Helvetica", 25), text = "Welcome!")
        self.lbl_welcome.place(relx = 0.5, rely = 0.25, anchor = 'center')

        self.lbl_welcome_text = customtkinter.CTkLabel(self.frame_m, wraplength = 600, font=("Helvetica", 15), justify = "left", text = "Curabitur eget dui ac magna laoreet lacinia. Donec egestas nunc et nulla hendrerit, eget ultricies sem tempor. Phasellus ut maximus turpis. Pellentesque ac faucibus sem. Morbi tincidunt diam nec sapien lobortis, vel congue dolor consequat. Integer ut turpis id sapien interdum semper in eu risus. In vestibulum nibh id risus cursus bibendum. Pellentesque efficitur quis lacus ut tristique.")
        self.lbl_welcome_text.place(relx = 0.5, rely = 0.7, anchor = 'center')

        # Buttons give 2 options
        self.btn_login = customtkinter.CTkButton(self.frame_b, fg_color="#D83215", hover_color="#ED5A41", width=100, height=30, font=("Helvetica", 15), text = "Login", command = "login")
        self.btn_login.place(relx = 0.35, rely = 0.1)

        self.btn_new_user = customtkinter.CTkButton(self.frame_b, fg_color="#D83215", hover_color="#ED5A41", width=100, height=30, font=("Helvetica", 15), text = "New User", command = "create_user")
        self.btn_new_user.place(relx = 0.52, rely = 0.1)

# Defines the app and creates the app's mainloop
app = App()
app.mainloop()