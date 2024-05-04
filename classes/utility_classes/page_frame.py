import tkinter as tk
import customtkinter as ctk
class page_frame(tk.Frame):
    def __init__(self, master,menu_target,button_names):
        super().__init__(master)
        self.configure(bg="#333333")
        self.configure_grid()
        self.configure_menu_buttons(master=master,target=menu_target, button_names=button_names)

    def configure_grid(self):
        self.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)

    def configure_menu_buttons(self,master,button_names, target):
        self.menu_buttons = {}

        for i, name in enumerate(button_names):
            button_name = name.replace(" ","_")

            button = target.menu_buttons[button_name] = ctk.CTkButton(self, text=name)
            button.grid(row=i, pady=10)
            button.configure(command=lambda name=button_name: master.show_frame(name))
