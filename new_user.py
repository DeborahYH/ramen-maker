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

class NewUser(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry('800x600')
        self.resizable(False, False)

        # Layout
        self.frame_t = customtkinter.CTkFrame(self)
        self.frame_t.pack(side="top", fill="both", expand=True)
        self.frame_m = customtkinter.CTkFrame(self)
        self.frame_m.pack(side="top", fill="both", expand=True)
        self.frame_b = customtkinter.CTkFrame(self)
        self.frame_b.pack(side="top", fill="both", expand=True)

        self.frame_m1 = customtkinter.CTkFrame(self.frame_m, fg_color="#DBDBDB")
        self.frame_m1.pack(side="left", fill="both", expand=True)
        self.frame_m2 = customtkinter.CTkFrame(self.frame_m, fg_color="#DBDBDB")
        self.frame_m2.pack(side="left", fill="both", expand=True)
        self.frame_m3 = customtkinter.CTkFrame(self.frame_m, fg_color="#DBDBDB")
        self.frame_m3.pack(side="left", fill="both", expand=True)
        self.frame_m4 = customtkinter.CTkFrame(self.frame_m, fg_color="#DBDBDB")
        self.frame_m4.pack(side="left", fill="both", expand=True)


        # Adds the logo
        self.logo = customtkinter.CTkImage(light_image = Image.open('images/logo.png'), dark_image = Image.open('images/logo.png'), size=(200,200))
        self.lbl_logo = customtkinter.CTkLabel(self.frame_t, text = "", image = self.logo)
        self.lbl_logo.pack(pady=10)

        self.lbl_new_user = customtkinter.CTkLabel(self.frame_t, font=("Helvetica", 20), text = "New User Registration")
        self.lbl_new_user.pack(pady=0)

        self.lbl_new_user = customtkinter.CTkLabel(self.frame_t, font=("Helvetica", 15), text = "Please fill out the following fields to complete your registration")
        self.lbl_new_user.pack(pady=(0,5))

        # Entry fields
        self.lbl_name = customtkinter.CTkLabel(self.frame_m2, font=("Helvetica", 15), anchor="e", justify="left", text = "Name")
        self.lbl_name.pack(pady=(10,0))
        self.entry_name = customtkinter.CTkEntry(self.frame_m2, width=180, placeholder_text="Insert your name here")
        self.entry_name.pack(pady=(0,15), padx=5)

        # Binds dob_action() to the entry field to decide whether it must be cleaned before choosng a date
        self.lbl_birth = customtkinter.CTkLabel(self.frame_m2, font=("Helvetica", 15), anchor="e", justify = "left", text = "Birth Date")
        self.lbl_birth.pack(pady=(10,0))
        self.entry_birth = customtkinter.CTkEntry(self.frame_m2, width=180, placeholder_text="mm/dd/yyyy")
        self.entry_birth.pack(pady=(0,15), padx=5)
        self.entry_birth.bind("<1>", self.dob_action)

        self.lbl_phone = customtkinter.CTkLabel(self.frame_m2, font=("Helvetica", 15), anchor="e", justify = "left", text = "Phone")
        self.lbl_phone.pack(pady=(10,0))
        self.entry_phone = customtkinter.CTkEntry(self.frame_m2, width=180, placeholder_text="")
        self.entry_phone.pack(pady=(0,15), padx=5)

        self.lbl_address = customtkinter.CTkLabel(self.frame_m3, font=("Helvetica", 15), anchor="e", justify = "left", text = "Address")
        self.lbl_address.pack(pady=(10,0))
        self.entry_address = customtkinter.CTkEntry(self.frame_m3, width=180, placeholder_text="Street Address")
        self.entry_address.pack(pady=(0,15), padx=5)

        self.lbl_email = customtkinter.CTkLabel(self.frame_m3, font=("Helvetica", 15), anchor="w", justify = "left", text = "Email")
        self.lbl_email.pack(pady=(10,0))
        self.entry_email = customtkinter.CTkEntry(self.frame_m3, width=180, placeholder_text="example@domain.com")
        self.entry_email.pack(pady=(0,15), padx=5)
        self.entry_email.bind("<FocusOut>", self.check_email)

        self.lbl_password = customtkinter.CTkLabel(self.frame_m3, font=("Helvetica", 15), anchor="w", justify = "left", text = "Password")
        self.lbl_password.pack(pady=(10,0))
        self.entry_password = customtkinter.CTkEntry(self.frame_m3, width=180, placeholder_text="Enter your password", show="*")
        self.entry_password.pack(pady=(0,15), padx=5)
        self.entry_password.bind("<FocusOut>", self.check_password)

        # Button to submit user information
        self.btn_submit = customtkinter.CTkButton(self.frame_b, width=100, height=30, fg_color="#D83215", hover_color="#ED5A41", font=("Helvetica", 15), text = "Create New User", command = self.submit)
        self.btn_submit.pack(pady=10)


    # Cleans the entry if there is a date and allows the user to select a different date
    def dob_action(self, event):
        dob_value = self.entry_birth.get()
        if dob_value != "":
            self.entry_birth.delete(0, END)
        self.pick_date(event)

    # Called by dob_action after cleaning the field.
    # Opens a calendar widget in a new window
    # Gets the selected date when the user closes the calendar
    # grab_set(): window blocks interactions with other windows until closed.
    def pick_date(self, event):
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

        btn_submit_date = customtkinter.CTkButton(date_window, fg_color="#D83215", hover_color="#ED5A41", width=100, height=30, font=("Helvetica", 15), text="Submit", command=self.obtain_date)
        btn_submit_date.pack()

    # Inserts the selected date into the entry field and closes the calendar window.
    def obtain_date(self):
        self.entry_birth.insert(0, calendar.get_date())
        date_window.destroy()


    # Checks if the email is valid
    def check_email(self, event):

        # Creates a pattern to be compared to the target string
        pattern = re.compile("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        # Compares the pattern to the email inserted by the user 
        email = self.entry_email.get()
        match = pattern.match(email) 
        
        if not match:
            CTkMessagebox(width=100, fg_color="#DBDBDB", title="Error!", message="Email is not valid!", icon="cancel", justify="center", button_color="#ED5A41", font=("Helvetica", 15))
            

    # Checks if the password is strong based on 4 requirements
    def check_password(self, event):
        password = self.entry_password.get()
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
    def submit(self):
        
        # Connects to the database
        db = sqlite3.connect('app_records.db')

        # Creates a cursor
        cursor = db.cursor()    

        # Obtains the current value in all fields inserted by the user
        name = self.entry_name.get().strip()
        birth_date = self.entry_birth.get().strip()
        phone_number = self.entry_phone.get().strip()
        address = self.entry_address.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get().strip()

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
                    {'entry_name': self.entry_name.get(),
                        'entry_birth': self.entry_birth.get(),
                        'entry_phone': self.entry_phone.get(),
                        'entry_address': self.entry_address.get(),
                        'entry_email': self.entry_email.get(),
                        'entry_password': self.entry_password.get()
                    })

        CTkMessagebox(width=100, fg_color="#DBDBDB", title="Success", message="Acount Registered Successfully!", icon="check", justify="center", button_color="#4CAF50", font=("Helvetica", 15))

        # Commits changes to the database
        # Closes the connection to the database
        db.commit()
        db.close()

        # Clears all entry boxes
        self.entry_name.delete(0, END)
        self.entry_birth.delete(0, END)
        self.entry_phone.delete(0, END)
        self.entry_address.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_password.delete(0, END)


# Defines the app and creates the app's mainloop
app_new_user = NewUser()
app_new_user.mainloop()