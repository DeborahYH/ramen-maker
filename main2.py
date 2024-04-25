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

# Creates tabs
tabs = customtkinter.CTkTabview(root, fg_color="white", segmented_button_fg_color="#BEA69F", segmented_button_unselected_color="#BEA69F", segmented_button_selected_color="#9D796F", segmented_button_selected_hover_color="#D8CAC6", segmented_button_unselected_hover_color="#D8CAC6", text_color="#1F1817")
tabs.pack(pady=50)
tabs.place(x=290, y=450)

tab_1 = tabs.add("Base")
tab_2 = tabs.add("Toppings")
tab_3 = tabs.add("Appetizers")
tab_4 = tabs.add("Beverages")
tab_5 = tabs.add("Dessert")
tab_6 = tabs.add("Cart")
tab_7 = tabs.add("Logout")

# Tab 1
lbl_size = customtkinter.CTkLabel(tab_1, text="Size")
lbl_size.pack()

radio_s = customtkinter.CTkRadioButton(tab_1, text="Small")
radio_s.pack()
radio_m = customtkinter.CTkRadioButton(tab_1, text="Medium")
radio_m.pack()
radio_l = customtkinter.CTkRadioButton(tab_1, text="Large")
radio_l.pack()

lbl_broth = customtkinter.CTkLabel(tab_1, text="Size")
lbl_broth.pack()

radio_salt = customtkinter.CTkRadioButton(tab_1, text="Salt")
radio_salt.pack()
radio_miso = customtkinter.CTkRadioButton(tab_1, text="Miso")
radio_miso.pack()
radio_shoyu = customtkinter.CTkRadioButton(tab_1, text="Shoyu")
radio_shoyu.pack()
radio_tonkotsu = customtkinter.CTkRadioButton(tab_1, text="Tonkotsu")
radio_tonkotsu.pack()
radio_curry = customtkinter.CTkRadioButton(tab_1, text="Curry")
radio_curry.pack()
radio_vegetarian = customtkinter.CTkRadioButton(tab_1, text="Vegetarian")
radio_vegetarian.pack()

lbl_spice = customtkinter.CTkLabel(tab_1, text="Spiciness")
lbl_spice.pack()

slider_spice = customtkinter.CTkSlider(tab_1, from_ = 1, to = 5, number_of_steps = 5)
slider_spice.pack()

# Tab 2

lbl_toppings = customtkinter.CTkLabel(tab_2, text="Toppings")
lbl_toppings.pack()

item_1 = customtkinter.CTkCheckBox(tab_2, text="beef")
item_1.pack()
item_2 = customtkinter.CTkCheckBox(tab_2, text="pork")
item_2.pack()
item_3 = customtkinter.CTkCheckBox(tab_2, text="chicken")
item_3.pack()
item_4 = customtkinter.CTkCheckBox(tab_2, text="shrimp")
item_4.pack()
item_5 = customtkinter.CTkCheckBox(tab_2, text="squid")
item_5.pack()
item_6 = customtkinter.CTkCheckBox(tab_2, text="clams")
item_6.pack()
item_7 = customtkinter.CTkCheckBox(tab_2, text="egg")
item_7.pack()
item_8 = customtkinter.CTkCheckBox(tab_2, text="wontons")
item_8.pack()
item_9 = customtkinter.CTkCheckBox(tab_2, text="kamaboko")
item_9.pack()
item_10 = customtkinter.CTkCheckBox(tab_2, text="shiitake")
item_10.pack()
item_11 = customtkinter.CTkCheckBox(tab_2, text="shimeji")
item_11.pack()
item_12 = customtkinter.CTkCheckBox(tab_2, text="kikurage")
item_12.pack()
item_13 = customtkinter.CTkCheckBox(tab_2, text="broccoli")
item_13.pack()
item_14 = customtkinter.CTkCheckBox(tab_2, text="negi")
item_14.pack()
item_15 = customtkinter.CTkCheckBox(tab_2, text="cabbage")
item_15.pack()
item_16 = customtkinter.CTkCheckBox(tab_2, text="bok choy")
item_16.pack()
item_17 = customtkinter.CTkCheckBox(tab_2, text="moyashi")
item_17.pack()
item_18 = customtkinter.CTkCheckBox(tab_2, text="garlic")
item_18.pack()
item_19 = customtkinter.CTkCheckBox(tab_2, text="peas")
item_19.pack()
item_20 = customtkinter.CTkCheckBox(tab_2, text="corn")
item_20.pack()
item_21 = customtkinter.CTkCheckBox(tab_2, text="carrots")
item_21.pack()
item_22 = customtkinter.CTkCheckBox(tab_2, text="nori")
item_22.pack()
item_23 = customtkinter.CTkCheckBox(tab_2, text="wakame")
item_23.pack()
item_24 = customtkinter.CTkCheckBox(tab_2, text="kombu")
item_24.pack()
item_25 = customtkinter.CTkCheckBox(tab_2, text="bamboo shoot")
item_25.pack()
item_26 = customtkinter.CTkCheckBox(tab_2, text="rayu")
item_26.pack()
item_27 = customtkinter.CTkCheckBox(tab_2, text="mayu")
item_27.pack()
item_28 = customtkinter.CTkCheckBox(tab_2, text="sesame oil")
item_28.pack()

# Tab 3

lbl_appetizers = customtkinter.CTkLabel(tab_3, text="Appetizers")
lbl_appetizers.pack()

lbl_item_1 = customtkinter.CTkLabel(tab_3, text="Cold Tofu")
lbl_item_1.pack()
spinbox_1 = Spinbox(tab_3, width=3)
spinbox_1.pack(padx=20, pady=20)

lbl_item_2 = customtkinter.CTkLabel(tab_3, text="Tsukemono Set")
lbl_item_2.pack()
spinbox_2 = Spinbox(tab_3, width=3)
spinbox_2.pack(padx=20, pady=20)

lbl_item_3 = customtkinter.CTkLabel(tab_3, text="Wakame Salad")
lbl_item_3.pack()
spinbox_3 = Spinbox(tab_3, width=3)
spinbox_3.pack(padx=20, pady=20)

lbl_item_4 = customtkinter.CTkLabel(tab_3, text="Edamame")
lbl_item_4.pack()
spinbox_4 = Spinbox(tab_3, width=3)
spinbox_4.pack(padx=20, pady=20)

lbl_item_5 = customtkinter.CTkLabel(tab_3, text="Ceviche")
lbl_item_5.pack()
spinbox_5 = Spinbox(tab_3, width=3)
spinbox_5.pack(padx=20, pady=20)

# Tab 4

lbl_beverages = customtkinter.CTkLabel(tab_4, text="Beverages")
lbl_beverages.pack()

lbl_bev1 = customtkinter.CTkLabel(tab_4, text="Water")
lbl_bev1.pack()
spin_bev1 = Spinbox(tab_4, width=3)
spin_bev1.pack(padx=20, pady=20)

lbl_bev2 = customtkinter.CTkLabel(tab_4, text="Coca-Cola")
lbl_bev2.pack()
spin_bev2 = Spinbox(tab_4, width=3)
spin_bev2.pack(padx=20, pady=20)

lbl_bev3 = customtkinter.CTkLabel(tab_4, text="Juice")
lbl_bev3.pack()
spin_bev3 = Spinbox(tab_4, width=3)
spin_bev3.pack(padx=20, pady=20)

lbl_bev4 = customtkinter.CTkLabel(tab_4, text="Tea")
lbl_bev4.pack()
spin_bev4 = Spinbox(tab_4, width=3)
spin_bev4.pack(padx=20, pady=20)


# Tab 5

lbl_dessert = customtkinter.CTkLabel(tab_5, text="Desserts")
lbl_dessert.pack()

lbl_des1 = customtkinter.CTkLabel(tab_5, text="Coffee Jelly")
lbl_des1.pack()
spin_des1 = Spinbox(tab_5, width=3)
spin_des1.pack(padx=20, pady=20)

lbl_des2 = customtkinter.CTkLabel(tab_5, text="Sakura Mochi")
lbl_des2.pack()
spin_des2 = Spinbox(tab_5, width=3)
spin_des2.pack(padx=20, pady=20)

lbl_des3 = customtkinter.CTkLabel(tab_5, text="Ice Cream Mochi")
lbl_des3.pack()
spin_des3 = Spinbox(tab_5, width=3)
spin_des3.pack(padx=20, pady=20)

lbl_des4 = customtkinter.CTkLabel(tab_5, text="Anmitsu")
lbl_des4.pack()
spin_des4 = Spinbox(tab_5, width=3)
spin_des4.pack(padx=20, pady=20)

lbl_des5 = customtkinter.CTkLabel(tab_5, text="Matcha Cake")
lbl_des5.pack()
spin_des5 = Spinbox(tab_5, width=3)
spin_des5.pack(padx=20, pady=20)

lbl_des6 = customtkinter.CTkLabel(tab_5, text="Matcha Tiramisu")
lbl_des6.pack()
spin_des6 = Spinbox(tab_5, width=3)
spin_des6.pack(padx=20, pady=20)

root.mainloop()