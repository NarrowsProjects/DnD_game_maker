import tkinter as tk
from classes.windows.character_creator import character_creator
from classes.windows.title_screen import title_screen

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Multi-Screen App')
        self.configure(bg="#333333")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.geometry(f'{screen_width}x{screen_height}')
        self.frames = {}

        pages = (character_creator, title_screen)
        for F in pages:
            page_name = F.__name__
            frame = F(self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.show_frame("title_screen")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
