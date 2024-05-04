import tkinter as tk
import customtkinter as ctk


class character_creator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg="#333333")
        self.configure_grid()
        self.configure_side_panel()
        self.configure_menu_buttons(master=master)

        self.entry = ctk.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(
            row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew"
        )

        self.main_button_1 = ctk.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
        )
        self.main_button_1.grid(
            row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )

        self.textbox = ctk.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.tabview = ctk.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("CTkTabview")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = ctk.CTkOptionMenu(
            self.tabview.tab("CTkTabview"),
            dynamic_resizing=False,
            values=["Value 1", "Value 2", "Value Long Long Long"],
        )

        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.combobox_1 = ctk.CTkComboBox(
            self.tabview.tab("CTkTabview"),
            values=["Value 1", "Value 2", "Value Long....."],
        )

        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.string_input_button = ctk.CTkButton(
            self.tabview.tab("CTkTabview"), text="Open CTkInputDialog"
        )
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.label_tab_2 = ctk.CTkLabel(
            self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2"
        )
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        self.radiobutton_frame = ctk.CTkFrame(self)
        self.radiobutton_frame.grid(
            row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew"
        )
        self.radio_var = tk.IntVar(value=0)
        self.label_radio_group = ctk.CTkLabel(
            master=self.radiobutton_frame, text="CTkRadioButton Group:"
        )
        self.label_radio_group.grid(
            row=0, column=2, columnspan=1, padx=10, pady=10, sticky=""
        )
        self.radio_button_1 = ctk.CTkRadioButton(
            master=self.radiobutton_frame, variable=self.radio_var, value=0
        )
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = ctk.CTkRadioButton(
            master=self.radiobutton_frame, variable=self.radio_var, value=1
        )
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = ctk.CTkRadioButton(
            master=self.radiobutton_frame, variable=self.radio_var, value=2
        )
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # create slider and progressbar frame
        self.slider_progressbar_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(
            row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew"
        )
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)

        self.seg_button_1 = ctk.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(
            row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew"
        )

        self.progressbar_1 = ctk.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(
            row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew"
        )

        self.progressbar_2 = ctk.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_2.grid(
            row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew"
        )

        self.slider_1 = ctk.CTkSlider(
            self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4
        )

        self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_2 = ctk.CTkSlider(
            self.slider_progressbar_frame, orientation="vertical"
        )
        self.slider_2.grid(
            row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns"
        )
        self.progressbar_3 = ctk.CTkProgressBar(
            self.slider_progressbar_frame, orientation="vertical"
        )
        self.progressbar_3.grid(
            row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns"
        )

        self.scrollable_frame = ctk.CTkScrollableFrame(
            self, label_text="CTkScrollableFrame"
        )
        self.scrollable_frame.grid(
            row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew"
        )
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(100):
            switch = ctk.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)

        self.checkbox_slider_frame = ctk.CTkFrame(self)
        self.checkbox_slider_frame.grid(
            row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew"
        )
        self.checkbox_1 = ctk.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_2 = ctk.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_3 = ctk.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        self.checkbox_3.configure(state="disabled")
        self.checkbox_1.select()
        self.scrollable_frame_switches[0].select()
        self.scrollable_frame_switches[4].select()
        self.radio_button_3.configure(state="disabled")
        self.optionmenu_1.set("CTkOptionmenu")
        self.combobox_1.set("CTkComboBox")
        self.slider_1.configure(command=lambda: self.progressbar_2.set)
        self.slider_2.configure(command=lambda: self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        self.textbox.insert(
            "0.0",
            "CTkTextbox\n\n"
            + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n"
            * 20,
        )
        self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        self.seg_button_1.set("Value 2")

    def configure_grid(self):
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

    def configure_side_panel(self):
        side_panel = self.side_panel = ctk.CTkFrame(self, bg_color="#333333", width=140)
        side_panel.grid(column=0, row=0, rowspan=4, sticky="nsew")
        label = ctk.CTkLabel(side_panel, text="Menu", font=("Helvetica", 30))
        label.grid(row=0, pady=20, padx=30, sticky="nsew")
        side_panel.grid_columnconfigure(0, weight=1)

    def configure_menu_buttons(self, master):
        self.menu_buttons = {}
        names = ["characters", "title screen"]
        for i, name in enumerate(names):
            button_name = name.replace(" ", "_")
            button = self.menu_buttons[button_name] = ctk.CTkButton(
                self.side_panel, text=name
            )
            button.grid(row=i+1, pady=10)
            button.configure(command=lambda name=button_name: master.show_frame(name))
