from tkinter import *
from tkcalendar import *
import customtkinter
import sqlite3
from PIL import Image
import maskpass


# Theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Creates the main window
root = customtkinter.CTk()
root.geometry('800x600')

# Layout
frame_top = customtkinter.CTkFrame(root, fg_color="#B5F5FF")
frame_top.pack(side="top", fill="both", expand=True)
frame_middle = customtkinter.CTkFrame(root, fg_color="#DD5FDA")
frame_middle.pack(side="top", fill="both", expand=True)
frame_bottom = customtkinter.CTkFrame(root, fg_color="#FFCAEB")
frame_bottom.pack(side="top", fill="both", expand=True)

frame_middle1 = customtkinter.CTkFrame(frame_middle, fg_color="#B2AFBA")
frame_middle1.pack(side="left", fill="both", expand=True)
frame_middle2 = customtkinter.CTkFrame(frame_middle, fg_color="#B2AFBA")
frame_middle2.pack(side="left", fill="both", expand=True)
frame_middle3 = customtkinter.CTkFrame(frame_middle, fg_color="#B2AFBA")
frame_middle3.pack(side="left", fill="both", expand=True)
frame_middle4 = customtkinter.CTkFrame(frame_middle, fg_color="#B2AFBA")
frame_middle4.pack(side="left", fill="both", expand=True)


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

# Saves data inserted in the entry fields to the user_info table
def submit():
    
    # Connects to the database
    db = sqlite3.connect('app_records.db')

    # Creates a cursor
    cursor = db.cursor()    

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
lbl_logo = customtkinter.CTkLabel(frame_top, image = logo)
lbl_logo.pack(pady=10)

lbl_new_user = customtkinter.CTkLabel(frame_top, font=("Helvetica", 20), text = "New User Registration")
lbl_new_user.pack(pady=15)

lbl_new_user = customtkinter.CTkLabel(frame_top, font=("Helvetica", 15), text = "Please fill out the following fields to complete your registration")
lbl_new_user.pack(pady=0)

# Entry fields
lbl_name = customtkinter.CTkLabel(frame_middle2, font=("Helvetica", 15), anchor="w", justify="left", text = "Name")
lbl_name.pack(pady=(20,0))
entry_name = customtkinter.CTkEntry(frame_middle2, width=230, placeholder_text="Insert your name here")
entry_name.pack(pady=(0,15))

# Binds dob_action() to the entry field to decide whether it must be cleaned before choosng a date
lbl_birth = customtkinter.CTkLabel(frame_middle2, font=("Helvetica", 15), anchor="w", justify = "left", text = "Birth Date")
lbl_birth.pack(pady=(10,0))
entry_birth = customtkinter.CTkEntry(frame_middle2, width=230, placeholder_text="mm/dd/yyyy")
entry_birth.pack(pady=(0,15))
entry_birth.bind("<1>", dob_action)

lbl_phone = customtkinter.CTkLabel(frame_middle2, font=("Helvetica", 15), anchor="w", justify = "left", text = "Phone")
lbl_phone.pack(pady=(10,0))
entry_phone = customtkinter.CTkEntry(frame_middle2, width=230, placeholder_text="")
entry_phone.pack(pady=(0,15))

lbl_address = customtkinter.CTkLabel(frame_middle3, font=("Helvetica", 15), anchor="w", justify = "left", text = "Address")
lbl_address.pack(pady=(20,0))
entry_address = customtkinter.CTkEntry(frame_middle3, width=230, placeholder_text="Street Address")
entry_address.pack(pady=(0,15))

lbl_email = customtkinter.CTkLabel(frame_middle3, font=("Helvetica", 15), anchor="w", justify = "left", text = "Email")
lbl_email.pack(pady=(10,0))
entry_email = customtkinter.CTkEntry(frame_middle3, width=230, placeholder_text="example@domain.com")
entry_email.pack(pady=(0,15))

lbl_password = customtkinter.CTkLabel(frame_middle3, font=("Helvetica", 15), anchor="w", justify = "left", text = "Password")
lbl_password.pack(pady=(10,0))
entry_password = customtkinter.CTkEntry(frame_middle3, width=230, placeholder_text="Enter your password", show="*")
entry_password.pack(pady=(0,15))

# Button to submit user information
btn_submit = customtkinter.CTkButton(frame_bottom, width=100, height=30, fg_color="#D83215", hover_color="#ED5A41", font=("Helvetica", 15), text = "Create New User", command = submit)
btn_submit.pack(pady=20)

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