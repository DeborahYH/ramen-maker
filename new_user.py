from tkinter import *
from tkcalendar import *
import customtkinter
from CTkMessagebox import CTkMessagebox
import sqlite3
import re
from PIL import Image
import maskpass


# Theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Creates the main window
root = customtkinter.CTk()
root.geometry('800x600')

# Layout
frame_t = customtkinter.CTkFrame(root)
frame_t.pack(side="top", fill="both", expand=True)
frame_m = customtkinter.CTkFrame(root)
frame_m.pack(side="top", fill="both", expand=True)
frame_b = customtkinter.CTkFrame(root)
frame_b.pack(side="top", fill="both", expand=True)

frame_m1 = customtkinter.CTkFrame(frame_m, fg_color="#DBDBDB")
frame_m1.pack(side="left", fill="both", expand=True)
frame_m2 = customtkinter.CTkFrame(frame_m, fg_color="#DBDBDB")
frame_m2.pack(side="left", fill="both", expand=True)
frame_m3 = customtkinter.CTkFrame(frame_m, fg_color="#DBDBDB")
frame_m3.pack(side="left", fill="both", expand=True)
frame_m4 = customtkinter.CTkFrame(frame_m, fg_color="#DBDBDB")
frame_m4.pack(side="left", fill="both", expand=True)


# Creates or connects to a database
db = sqlite3.connect('app_records.db')

# Creates a cursor
cursor = db.cursor()

# Creates a table with its columns
cursor.execute("""CREATE TABLE IF NOT EXISTS user_info (
               name text,
               birth_date text,
               phone_number text,
               address text,
               email text,
               password text
               )""")

# Commits changes to the database
# Closes the connection to the database
db.commit()
db.close()


# Cleans the entry if there is a date and allows the user to select a different date
def dob_action(event):
    dob_value = entry_birth.get()
    if dob_value != "":
        entry_birth.delete(0, END)
    pick_date(event)

# Called by dob_action after cleaning the field.
# Opens a calendar widget in a new window
# Gets the selected date when the user closes the calendar
# grab_set(): window blocks interactions with other windows until closed.
def pick_date(event):
    global calendar, date_window
    date_window = Toplevel()
    date_window.grab_set()
    date_window.geometry('350x350')

    calendar = Calendar(date_window, font=("Arial", 12), selectmode="day", date_pattern="mm/dd/y", 
                        background="#EB4F35", disabledbackground="#EB4F35", bordercolor="#EB4F35", 
                        headersbackground="#EB4F35", headersforeground='white',
                        normalbackground="white", normalforeground='#525252', foreground='white', 
                        weekendbackground="white", weekendforeground='#525252',
                        othermonthbackground='#EACFC8', othermonthforeground='#525252',
                        othermonthwebackground='#EACFC8', othermonthweforeground='#525252')
    calendar.pack(pady=20)

    btn_submit_date = customtkinter.CTkButton(date_window, fg_color="#D83215", hover_color="#ED5A41", width=100, height=30, font=("Helvetica", 15), text="Submit", command=obtain_date)
    btn_submit_date.pack()

# Inserts the selected date into the entry field and closes the calendar window.
def obtain_date():
    entry_birth.insert(0, calendar.get_date())
    date_window.destroy()


# Checks if the email is valid
def check_email(event):

    # Creates a pattern to be compared to the target string
    pattern = re.compile("^[a-z 0-9]+[._]?[a-z 0-9]+[@][a-zA-Z0-9]+\.[a-zA-Z]{2,3}$")
  
    # Compares the pattern to the email inserted by the user 
    email = entry_email.get()
    match = pattern.match(email) 
    
    if not match:
        CTkMessagebox(width=100, fg_color="#DBDBDB", title="Error!", message="Email is not valid!", icon="cancel", justify="center", button_color="#ED5A41", font=("Helvetica", 15))
        

# Checks if the password is strong based on 4 requirements
def check_password(event):
    password = entry_password.get()
    while True:
        if len(password) < 8:
            CTkMessagebox(width=100, fg_color="#DBDBDB", title="Warning!", message="Password must be at least 8 characters long", icon="cancel", justify="center", button_color="#ED5A41", font=("Helvetica", 15))
            break
        elif re.search(r'[!@#$%&]', password) is None:
            CTkMessagebox(width=100, fg_color="#DBDBDB", title="Warning!", message="Password must have at least 1 special character", icon="cancel", justify="center", button_color="#ED5A41", font=("Helvetica", 15))
            break
        elif re.search(r'[0-9]', password) is None:
            CTkMessagebox(width=100, fg_color="#DBDBDB", title="Warning!", message="Password must have at least 1 number between 0-9", icon="cancel", justify="center", button_color="#ED5A41", font=("Helvetica", 15))
            break
        elif re.search(r'[A-Z]', password) is None:
            CTkMessagebox(width=100, fg_color="#DBDBDB", title="Warning!", message="Password must have at least 1 uppercase letter", icon="cancel", justify="center", button_color="#ED5A41", font=("Helvetica", 15))
            break
        else: 
            break

# Saves data inserted in the entry fields to the user_info table
def submit():
    
    # Connects to the database
    db = sqlite3.connect('app_records.db')

    # Creates a cursor
    cursor = db.cursor()    

    # Obtains the current value in all fields inserted by the user
    name = entry_name.get().strip()
    birth_date = entry_birth.get().strip()
    phone_number = entry_phone.get().strip()
    address = entry_address.get().strip()
    email = entry_email.get().strip()
    password = entry_password.get().strip()

    # Checks if the user didn't fill one of the entry fields
    if not name or not birth_date or not phone_number or not address or not email or not password:
        CTkMessagebox(width=100, fg_color="#DBDBDB", title="Warning!", message="All fields must be filled!", icon="cancel", justify="center", button_color="#ED5A41", font=("Helvetica", 15))
        return  # Exits the function

    # Checks if the email is already registered
    cursor.execute("SELECT email from user_info WHERE email = ?", [email])
    if cursor.fetchone() is not None:
        CTkMessagebox(width=100, fg_color="#DBDBDB", title="Warning!", message="Email is already registered!", icon="cancel", justify="center", button_color="#ED5A41", font=("Helvetica", 15))
        return  # Exits the function
     
    # Inserts data into the table
    cursor.execute("INSERT INTO user_info VALUES (:entry_name, :entry_birth, :entry_phone, :entry_address, :entry_email, :entry_password)",
                   {'entry_name': entry_name.get(),
                    'entry_birth': entry_birth.get(),
                    'entry_phone': entry_phone.get(),
                    'entry_address': entry_address.get(),
                    'entry_email': entry_email.get(),
                    'entry_password': entry_password.get()
                   })

    # Commits changes to the database
    # Closes the connection to the database
    db.commit()
    db.close()

    # Clears all entry boxes
    entry_name.delete(0, END)
    entry_birth.delete(0, END)
    entry_phone.delete(0, END)
    entry_address.delete(0, END)
    entry_email.delete(0, END)
    entry_password.delete(0, END)


# Adds the logo
logo = customtkinter.CTkImage(light_image = Image.open('images/logo.png'), dark_image = Image.open('images/logo.png'), size=(200,200))
lbl_logo = customtkinter.CTkLabel(frame_t, text = "", image = logo)
lbl_logo.pack(pady=10)

lbl_new_user = customtkinter.CTkLabel(frame_t, font=("Helvetica", 20), text = "New User Registration")
lbl_new_user.pack(pady=0)

lbl_new_user = customtkinter.CTkLabel(frame_t, font=("Helvetica", 15), text = "Please fill out the following fields to complete your registration")
lbl_new_user.pack(pady=(0,5))

# Entry fields
lbl_name = customtkinter.CTkLabel(frame_m2, font=("Helvetica", 15), anchor="e", justify="left", text = "Name")
lbl_name.pack(pady=(10,0))
entry_name = customtkinter.CTkEntry(frame_m2, width=180, placeholder_text="Insert your name here")
entry_name.pack(pady=(0,15), padx=5)

# Binds dob_action() to the entry field to decide whether it must be cleaned before choosng a date
lbl_birth = customtkinter.CTkLabel(frame_m2, font=("Helvetica", 15), anchor="e", justify = "left", text = "Birth Date")
lbl_birth.pack(pady=(10,0))
entry_birth = customtkinter.CTkEntry(frame_m2, width=180, placeholder_text="mm/dd/yyyy")
entry_birth.pack(pady=(0,15), padx=5)
entry_birth.bind("<1>", dob_action)

lbl_phone = customtkinter.CTkLabel(frame_m2, font=("Helvetica", 15), anchor="e", justify = "left", text = "Phone")
lbl_phone.pack(pady=(10,0))
entry_phone = customtkinter.CTkEntry(frame_m2, width=180, placeholder_text="")
entry_phone.pack(pady=(0,15), padx=5)

lbl_address = customtkinter.CTkLabel(frame_m3, font=("Helvetica", 15), anchor="e", justify = "left", text = "Address")
lbl_address.pack(pady=(10,0))
entry_address = customtkinter.CTkEntry(frame_m3, width=180, placeholder_text="Street Address")
entry_address.pack(pady=(0,15), padx=5)

lbl_email = customtkinter.CTkLabel(frame_m3, font=("Helvetica", 15), anchor="w", justify = "left", text = "Email")
lbl_email.pack(pady=(10,0))
entry_email = customtkinter.CTkEntry(frame_m3, width=180, placeholder_text="example@domain.com")
entry_email.pack(pady=(0,15), padx=5)
entry_email.bind("<FocusOut>", check_email)

lbl_password = customtkinter.CTkLabel(frame_m3, font=("Helvetica", 15), anchor="w", justify = "left", text = "Password")
lbl_password.pack(pady=(10,0))
entry_password = customtkinter.CTkEntry(frame_m3, width=180, placeholder_text="Enter your password", show="*")
entry_password.pack(pady=(0,15), padx=5)
entry_password.bind("<FocusOut>", check_password)

# Button to submit user information
btn_submit = customtkinter.CTkButton(frame_b, width=100, height=30, fg_color="#D83215", hover_color="#ED5A41", font=("Helvetica", 15), text = "Create New User", command = submit)
btn_submit.pack(pady=10)

# Creates a button and function to show the user records in the table
"""
def show():
    
    # Creates or connects to a database
    db = sqlite3.connect('app_records.db')

    # Creates a cursor
    cursor = db.cursor()    

    # Inserts data into the table
    cursor.execute("SELECT *, oid FROM user_info")
    records = cursor.fetchall()
    print(records)

    # Commits changes to the database
    db.commit()

    # Closes the connection to the database
    db.close()
    
btn_query = customtkinter.CTkButton(frame_bottom, width=100, height=30, fg_color="#D83215", hover_color="#ED5A41", font=("Helvetica", 15), text = "Show", command = show)
btn_query.pack(pady=20)
"""

root.mainloop()