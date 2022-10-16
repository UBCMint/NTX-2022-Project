from random import randint
import threading
from threading import Thread
from tkinter import Toplevel
import customtkinter as CTk
from stimulus import cubeWindow,changeRotation


CTk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
CTk.set_default_color_theme("GUI/Assets/MintTheme.json")  # Themes: "blue" (standard), "green", "dark-blue"

class App(CTk.CTk):
    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()
        self.cubeOpen = False
        self.title("NTX-2022-PROJECT")
        self.iconbitmap("GUI/Assets/logo.ico")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # Create color toplevel
        self.colorWindow = CTk.CTkToplevel()
        self.colorWindow.destroy()

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(1, weight=1, minsize=360)
        self.grid_rowconfigure(0, weight=1)

        self.menu = CTk.CTkFrame(master=self,
                                                corner_radius=0)
        self.menu.grid(row=0, column=1, sticky="nswe")

        self.stimulusWindow = CTk.CTkFrame(master=self)
        self.stimulusWindow.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)

        # ============ Menu ============

        # configure grid layout (1x2)
        self.menu.grid_rowconfigure(0, weight=1)
        self.menu.grid_rowconfigure(1, weight=1)
        self.menu.grid_columnconfigure(0, weight=1)

        self.analyzeMenu = CTk.CTkFrame(master=self.menu
                                                )
        self.analyzeMenu.grid(row=0, column=0, sticky="nswe",padx=2,pady=2)
        self.recordMenu = CTk.CTkFrame(master=self.menu
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

        self.recordLabel = CTk.CTkLabel(master=self.recordMenu,
                                              text="Record",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.recordLabel.grid(row=1, column=0, columnspan=4, pady=10, padx=10, sticky="we")
        self.recordFileName = CTk.CTkEntry(master=self.recordMenu,
                                            placeholder_text="File Name")
        self.recordFileName.grid(row=2, column=0, columnspan=3, pady=5, padx=5, sticky="we")

        self.defaultButton = CTk.CTkButton(master=self.recordMenu,
                                                width=70,
                                                text="Default",
                                                command=self.button_event)
        self.defaultButton.grid(row=2, column=3, pady=5, padx=5)

        self.recordButton = CTk.CTkButton(master=self.recordMenu,
                                                text="Record",
                                                command=self.button_event)
        self.recordButton.grid(row=9, column=0, columnspan=2, pady=5, padx=5, sticky="we")

        self.stopButton = CTk.CTkButton(master=self.recordMenu,
                                                text="Stop",
                                                command=self.button_event,
                                                state="disabled")
        self.stopButton.grid(row=9, column=2, columnspan=2, pady=5, padx=5, sticky="we")

        self.cancelButton = CTk.CTkButton(master=self.recordMenu,
                                                text="Cancel",
                                                command=self.button_event,
                                                state="disabled")
        self.cancelButton.grid(row=10, column=0, columnspan=2, pady=5, padx=5, sticky="we")

        self.saveButton = CTk.CTkButton(master=self.recordMenu,
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

        self.recordLabel = CTk.CTkLabel(master=self.analyzeMenu,
                                              text="Analyze",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.recordLabel.grid(row=1, column=0, columnspan=4, pady=10, padx=10, sticky="we")

        self.analyzeFileName = CTk.CTkLabel(master=self.analyzeMenu,
                                                text="File Name.csv")
        self.analyzeFileName.grid(row=2, column=0, columnspan=3, pady=5, padx=5, sticky="we")

        self.openFileButton = CTk.CTkButton(master=self.analyzeMenu,
                                                text="Open",
                                                command=self.button_event)
        self.openFileButton.grid(row=2, column=3, pady=5, padx=5)

        self.playButton = CTk.CTkButton(master=self.analyzeMenu,
                                                text="Play",
                                                command=self.button_event)
        self.playButton.grid(row=9, column=0, columnspan=4, pady=5, padx=5, sticky="we")

        # ============ Stimuli Window ============
        self.stimulusWindow.grid_rowconfigure(0,minsize=50)
        self.stimulusWindow.grid_rowconfigure(3,minsize=50)

        #Colour buttons
        self.colorLabel = CTk.CTkLabel(master=self.stimulusWindow,
                                        text="Colour Stimulus",
                                        text_font=("Roboto Medium", -20),
                                        anchor="w")
        self.colorLabel.grid(row=1,column=0,columnspan=2,pady=5,padx=20, sticky="we")

        self.redButton = CTk.CTkButton(master=self.stimulusWindow,
                                        fg_color="red", 
                                        text="",
                                        height=40,
                                        command=lambda:self.displayColor("red"))
        self.redButton.grid(row=2,column=0,pady=5,padx=10, sticky="we")

        self.blueButton = CTk.CTkButton(master=self.stimulusWindow,
                                        fg_color="blue",
                                        text="",height=40,
                                        command=lambda:self.displayColor("blue"))
        self.blueButton.grid(row=2,column=1,pady=5,padx=0, sticky="we")

        self.greenButton = CTk.CTkButton(master=self.stimulusWindow,
                                            fg_color="green",
                                            text="",
                                            height=40,
                                            command=lambda:self.displayColor("green"))
        self.greenButton.grid(row=2,column=2,pady=5,padx=10, sticky="we")

        #Cube buttons
        self.cubeLabel = CTk.CTkLabel(master=self.stimulusWindow,
                                        text="Cube Stimulus",
                                        text_font=("Roboto Medium", -20),
                                        anchor="w")
        self.cubeLabel.grid(row=4,column=0,columnspan=2,pady=5,padx=20, sticky="we")

        self.spinningCubeButton = CTk.CTkButton(master=self.stimulusWindow,
                                                text="Spinning Cube",
                                                command=self.spinCube)
        self.spinningCubeButton.grid(row=5, column=0, pady=5, padx=5)

        self.stillCubeButton = CTk.CTkButton(master=self.stimulusWindow,
                                        text="Still Cube",
                                        command=self.stillCube)
        self.stillCubeButton.grid(row=5, column=1, pady=5, padx=5)
        


    #define functions for each button and input

    def button_event(self):
        print(threading.activeCount())
        print("Button pressed")

    def displayColor(self,color):
        if not CTk.CTkToplevel.winfo_exists(self.colorWindow): 
            self.colorWindow = CTk.CTkToplevel()
            self.colorWindow.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.colorWindow.configure(bg=color)

    def openCube(self):
        self.cubeOpen = True
        Thread(target=cubeWindow).start()

    def spinCube(self):
        if not self.cubeOpen: self.openCube()
        changeRotation(5,3)

    def stillCube(self):
        if not self.cubeOpen: self.openCube()
        changeRotation(0,0)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()