from tkinter import *
import customtkinter
from CTkMessagebox import CTkMessagebox
import sqlite3
from PIL import Image 

# Theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Creates the main window
root = customtkinter.CTk()
root.geometry('300x500')
root.resizable(False, False)

# cget() returns the current value of the specified option.
def password_view():
    if entry_password.cget('show') == '*':
        entry_password.configure(show='')
        btn_eye.configure(image=img_hide)
    else: 
        btn_eye.configure(image=img_show)
        entry_password.configure(show='*')

def login():

    # Creates or connects to a database
    db = sqlite3.connect('app_records.db')

    # Creates a cursor
    cursor = db.cursor()   

    # Obtains the current value inserted by the user into these two fields 
    email = entry_email.get().strip()
    password = entry_password.get().strip()

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
        

frame_t = customtkinter.CTkFrame(root)
frame_t.pack(side="top", fill="both", expand=True)
frame_m = customtkinter.CTkFrame(root)
frame_m.pack(side="top", fill="both", expand=True)
frame_b = customtkinter.CTkFrame(root)
frame_b.pack(side="top", fill="both", expand=True)

# Adds the logo
logo = customtkinter.CTkImage(light_image = Image.open('images/logo.png'), dark_image = Image.open('images/logo.png'), size=(200,200))
lbl_logo = customtkinter.CTkLabel(frame_t, text = "", image = logo)
lbl_logo.place(relx = 0.5, rely = 0.55, anchor = 'center')

# Entry fields
lbl_email = customtkinter.CTkLabel(frame_m, font=("Helvetica", 15), text = "Email")
lbl_email.place(relx = 0.2, rely = 0.1)

entry_email = customtkinter.CTkEntry(frame_m, placeholder_text = "example@mail.com")
entry_email.place(relx = 0.2, rely = 0.25)

lbl_password = customtkinter.CTkLabel(frame_m, font=("Helvetica", 15), text = "Password")
lbl_password.place(relx = 0.2, rely = 0.5)

entry_password = customtkinter.CTkEntry(frame_m, placeholder_text = "*****", show="*")
entry_password.place(relx = 0.2, rely = 0.65)

img_show = customtkinter.CTkImage(Image.open("images/show.png"),size=(20,20))
img_hide = customtkinter.CTkImage(Image.open("images/hide.png"),size=(20,20))
btn_eye = customtkinter.CTkButton(frame_m, width=8, fg_color="#DBDBDB", image=img_show, text='', command=password_view)
btn_eye.place(relx = 0.7, rely = 0.65)

# Button allows the users to submit their information
btn_login = customtkinter.CTkButton(frame_b, fg_color="#D83215", hover_color="#ED5A41", width=100, height=30, font=("Helvetica", 15), text="Login", command = login)
btn_login.place(relx = 0.5, rely = 0.2, anchor = 'center')

root.mainloop()