import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("NTX-2022-PROJECT")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(1, weight=1, minsize=360)
        self.grid_rowconfigure(0, weight=1)

        self.menu = customtkinter.CTkFrame(master=self,
                                                corner_radius=0)
        self.menu.grid(row=0, column=1, sticky="nswe")

        self.stimulusWindow = customtkinter.CTkFrame(master=self)
        self.stimulusWindow.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

        # ============ Menu ============

        # configure grid layout (1x2)
        self.menu.grid_rowconfigure(0, weight=1)
        self.menu.grid_rowconfigure(1, weight=1)
        self.menu.grid_columnconfigure(0, weight=1)

        self.analyzeMenu = customtkinter.CTkFrame(master=self.menu
                                                )
        self.analyzeMenu.grid(row=0, column=0, sticky="nswe",padx=2,pady=2)
        self.recordMenu = customtkinter.CTkFrame(master=self.menu
                                                )
        self.recordMenu.grid(row=1, column=0, sticky="nswe",padx=2,pady=2)

        ## ============ Record ============
        # configure grid layout (4x11?)
        self.recordMenu.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.recordMenu.grid_columnconfigure(0, weight=1, minsize=70)
        self.recordMenu.grid_columnconfigure(2, weight=1)
        self.recordMenu.grid_rowconfigure(3, weight=1)  # empty row as spacing
        self.recordMenu.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.recordMenu.grid_rowconfigure(11, minsize=20)  # empty row with minsize as spacing

        self.recordLabel = customtkinter.CTkLabel(master=self.recordMenu,
                                              text="Record",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.recordLabel.grid(row=1, column=0, columnspan=4, pady=10, padx=10, sticky="we")
        self.recordFileName = customtkinter.CTkEntry(master=self.recordMenu,
                                            placeholder_text="File Name")
        self.recordFileName.grid(row=2, column=0, columnspan=3, pady=5, padx=5, sticky="we")

        self.defaultButton = customtkinter.CTkButton(master=self.recordMenu,
                                                width=70,
                                                text="Default",
                                                command=self.button_event)
        self.defaultButton.grid(row=2, column=3, pady=5, padx=5)

        self.recordButton = customtkinter.CTkButton(master=self.recordMenu,
                                                text="Record",
                                                command=self.button_event)
        self.recordButton.grid(row=9, column=0, columnspan=2, pady=5, padx=5, sticky="we")

        self.stopButton = customtkinter.CTkButton(master=self.recordMenu,
                                                text="Stop",
                                                command=self.button_event,
                                                state="disabled")
        self.stopButton.grid(row=9, column=2, columnspan=2, pady=5, padx=5, sticky="we")

        self.cancelButton = customtkinter.CTkButton(master=self.recordMenu,
                                                text="Cancel",
                                                command=self.button_event,
                                                state="disabled")
        self.cancelButton.grid(row=10, column=0, columnspan=2, pady=5, padx=5, sticky="we")

        self.saveButton = customtkinter.CTkButton(master=self.recordMenu,
                                                text="Save",
                                                command=self.button_event,
                                                state="disabled")
        self.saveButton.grid(row=10, column=2, columnspan=2, pady=5, padx=5, sticky="we")

        ## ============ Analyze ============
        # configure grid layout (4x4?)
        self.analyzeMenu.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.analyzeMenu.grid_columnconfigure(0, weight=1, minsize=70)
        self.analyzeMenu.grid_columnconfigure(2, weight=1)
        self.analyzeMenu.grid_rowconfigure(3, weight=1)  # empty row as spacing
        self.analyzeMenu.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.analyzeMenu.grid_rowconfigure(10, minsize=20)  # empty row with minsize as spacing

        self.recordLabel = customtkinter.CTkLabel(master=self.analyzeMenu,
                                              text="Analyze",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.recordLabel.grid(row=1, column=0, columnspan=4, pady=10, padx=10, sticky="we")

        self.analyzeFileName = customtkinter.CTkLabel(master=self.analyzeMenu,
                                                text="File Name.csv")
        self.analyzeFileName.grid(row=2, column=0, columnspan=3, pady=5, padx=5, sticky="we")

        self.openFileButton = customtkinter.CTkButton(master=self.analyzeMenu,
                                                text="Open",
                                                command=self.button_event)
        self.openFileButton.grid(row=2, column=3, pady=5, padx=5)

        self.playButton = customtkinter.CTkButton(master=self.analyzeMenu,
                                                text="Play",
                                                command=self.button_event)
        self.playButton.grid(row=9, column=0, columnspan=4, pady=5, padx=5, sticky="we")

        # ============ Stimuli Window ============

        #Display some sort of stimulus?


    #define functions for each button and input
    def button_event(self):
        print("Button pressed")

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()