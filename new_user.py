from tkinter import *
from tkcalendar import *
import customtkinter
from PIL import Image
import maskpass


# Theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Creates the main window
root = customtkinter.CTk()
root.geometry('1000x850')

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


# Adds the logo
logo = customtkinter.CTkImage(light_image = Image.open('images/logo.png'), dark_image = Image.open('images/logo.png'), size=(200,200))
lbl_logo = customtkinter.CTkLabel(root, image = logo)
lbl_logo.pack(pady=10)

# Shows the welcome text
lbl_welcome = customtkinter.CTkLabel(root, font=("Helvetica", 25), text = "Welcome!")
lbl_welcome.pack(pady=15)

# Entry fields
lbl_name = customtkinter.CTkLabel(root, font=("Helvetica", 15), anchor="w", justify="left", text = "Name")
lbl_name.pack(pady=0)
entry_name = customtkinter.CTkEntry(root, width=250, placeholder_text="Insert your name here")
entry_name.pack(pady=10)

# Binds dob_action() to the entry field to decide whether it must be cleaned before choosng a date
lbl_birth = customtkinter.CTkLabel(root, font=("Helvetica", 15), anchor="w", justify = "left", text = "Birth Date")
lbl_birth.pack(pady=0)
entry_birth = customtkinter.CTkEntry(root, width=250, placeholder_text="mm/dd/yyyy")
entry_birth.pack(pady=10)
entry_birth.bind("<1>", dob_action)

lbl_phone = customtkinter.CTkLabel(root, font=("Helvetica", 15), anchor="w", justify = "left", text = "Phone")
lbl_phone.pack(pady=0)
entry_phone = customtkinter.CTkEntry(root, width=250, placeholder_text="")
entry_phone.pack(pady=10)

lbl_address = customtkinter.CTkLabel(root, font=("Helvetica", 15), anchor="w", justify = "left", text = "Address")
lbl_address.pack(pady=0)
entry_address = customtkinter.CTkEntry(root, width=250, placeholder_text="Street Address")
entry_address.pack(pady=10)

lbl_email = customtkinter.CTkLabel(root, font=("Helvetica", 15), anchor="w", justify = "left", text = "Email")
lbl_email.pack(pady=0)
entry_email = customtkinter.CTkEntry(root, width=250, placeholder_text="example@domain.com")
entry_email.pack(pady=10)

lbl_password = customtkinter.CTkLabel(root, font=("Helvetica", 15), anchor="w", justify = "left", text = "Password")
lbl_password.pack(pady=0)
entry_password = customtkinter.CTkEntry(root, width=250, placeholder_text="Enter your password", show="*")
entry_password.pack(pady=10)

# Button to submit user information
btn_submit = customtkinter.CTkButton(root, width=100, height=30, fg_color="#D83215", hover_color="#ED5A41", font=("Helvetica", 15), text = "Create New User", command = "submit")
btn_submit.pack(pady=15)

root.mainloop()