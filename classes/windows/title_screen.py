import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


class title_screen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.background_image = Image.open('./assets/img/logo.png')
        self.background_image = self.background_image.resize((self.winfo_screenwidth(), self.winfo_screenheight()))
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(self, image=self.background_photo, bg="black")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.configure_grid()
        self.add_menu_buttons(master=master,target=self)


    def add_menu_buttons(self,master, target):
        self.menu_buttons = {}
        names =["join game","host game","characters","character_creator"]
        for i, name in enumerate(names):
            button_name = name.replace(" ","_")

            button = target.menu_buttons[button_name] = ctk.CTkButton(self, text=name)
            x = self.winfo_screenwidth()/2-75
            y = self.winfo_screenheight()*0.66 + i* 50
            button.place(x=x, y=y)

            button.configure(command=lambda name=button_name: master.show_frame(name))

    def configure_grid(self):
        self.grid_columnconfigure(((0,1,2,3,4,5,6)), weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)

