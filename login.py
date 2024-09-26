from tkinter import *
import customtkinter
from CTkMessagebox import CTkMessagebox
import sqlite3
from PIL import Image 

# Theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")


class Login(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry('300x500')
        self.resizable(False, False)            

        self.frame_t = customtkinter.CTkFrame(self)
        self.frame_t.pack(side="top", fill="both", expand=True)
        self.frame_m = customtkinter.CTkFrame(self)
        self.frame_m.pack(side="top", fill="both", expand=True)
        self.frame_b = customtkinter.CTkFrame(self)
        self.frame_b.pack(side="top", fill="both", expand=True)

        # Adds the logo
        self.logo = customtkinter.CTkImage(light_image = Image.open('images/logo.png'), dark_image = Image.open('images/logo.png'), size=(200,200))
        self.lbl_logo = customtkinter.CTkLabel(self.frame_t, text = "", image = self.logo)
        self.lbl_logo.place(relx = 0.5, rely = 0.55, anchor = 'center')

        # Entry fields
        self.lbl_email = customtkinter.CTkLabel(self.frame_m, font=("Helvetica", 15), text = "Email")
        self.lbl_email.place(relx = 0.2, rely = 0.1)

        self.entry_email = customtkinter.CTkEntry(self.frame_m, placeholder_text = "example@mail.com")
        self.entry_email.place(relx = 0.2, rely = 0.25)

        self.lbl_password = customtkinter.CTkLabel(self.frame_m, font=("Helvetica", 15), text = "Password")
        self.lbl_password.place(relx = 0.2, rely = 0.5)

        self.entry_password = customtkinter.CTkEntry(self.frame_m, placeholder_text = "*****", show="*")
        self.entry_password.place(relx = 0.2, rely = 0.65)

        self.img_show = customtkinter.CTkImage(Image.open("images/show.png"),size=(20,20))
        self.img_hide = customtkinter.CTkImage(Image.open("images/hide.png"),size=(20,20))
        self.btn_eye = customtkinter.CTkButton(self.frame_m, width=8, fg_color="#DBDBDB", image=self.img_show, text='', command=self.password_view)
        self.btn_eye.place(relx = 0.7, rely = 0.65)

        # Button allows the users to submit their information
        self.btn_login = customtkinter.CTkButton(self.frame_b, fg_color="#D83215", hover_color="#ED5A41", width=100, height=30, font=("Helvetica", 15), text="Login", command = self.login)
        self.btn_login.place(relx = 0.5, rely = 0.2, anchor = 'center')

    # cget() returns the current value of the specified option.
    def password_view(self):
        if self.entry_password.cget('show') == '*':
            self.entry_password.configure(show='')
            self.btn_eye.configure(image=self.img_hide)
        else: 
            self.btn_eye.configure(image=self.img_show)
            self.entry_password.configure(show='*')

    def login(self):

        # Creates or connects to a database
        db = sqlite3.connect('app_records.db')

        # Creates a cursor
        cursor = db.cursor()   

        # Obtains the current value inserted by the user into these two fields 
        email = self.entry_email.get().strip()
        password = self.entry_password.get().strip()

        # Checks if the user didn't fill one of the entry fields
        if not email or not password:
            CTkMessagebox(width=100, fg_color="#DBDBDB", title="Warning!", message="All fields must be filled!", icon="cancel", justify="center", button_color="#ED5A41", font=("Helvetica", 15))
            return  # Exits the function
        
        # Obtains the password from the record containing the user's email 
        cursor.execute("SELECT password FROM user_info WHERE email=?", [email])
        result = cursor.fetchone()

        # Extract the password from the fetched record
        # Checks if the registered password is the same as the one entered by the user
        if result:
            stored_password = result[0]  
            if password == stored_password:
                CTkMessagebox(width=100, fg_color="#DBDBDB", title="Success", message="Login Sucessful!", icon="check", justify="center", button_color="#4CAF50", font=("Helvetica", 15))
            else:
                CTkMessagebox(width=100, fg_color="#DBDBDB", title="Warning!", message="Incorrect password!", icon="cancel", justify="center", button_color="#ED5A41", font=("Helvetica", 15))
        else:
            CTkMessagebox(width=100, fg_color="#DBDBDB", title="Warning!", message="Email not found!", icon="cancel", justify="center", button_color="#ED5A41", font=("Helvetica", 15))

app_login = Login()
app_login.mainloop()
