# Copypasta Typer
import sys
import time
from tkinter import *



# Variables

recording = False;


# #tkinter part

mw=Tk()

mw.title('NTX 2022 Project')


# 3 subsections

tf = Frame(master=mw, height=200, width=600)
tf.grid(row=0, column=0, sticky="NESW", padx=20, pady=10)
tf.grid_columnconfigure(0, weight=1)
tf.grid_columnconfigure(2, weight=1)

mf = Frame(master=mw, height=200, width=600)
mf.grid(row=1, column=0, sticky="NESW", padx=20, pady=10)
mf.grid_columnconfigure(0, weight=1)
mf.grid_columnconfigure(3, weight=1)

bf = Frame(master=mw, height=200, width=600)
bf.grid(row=2, column=0, sticky="NESW", padx=20, pady=10)
bf.grid_columnconfigure(0, weight=1)
bf.grid_columnconfigure(4, weight=1)


# top frame

label = Label(master=tf, text="Connection Status: Pending")
label.grid(column=1, row=0)

# bottom frame

b1 = Button(master=mf, text='Start recording',
 command=lambda: getInput()).grid(row=0, column=1, padx=5)

b3 = Button(master=bf, text='Quit',
 command=lambda:quit()).grid(row=0, column=2, padx=5)


b4 = Button(master=bf, text='Output to CSV',
 command=lambda:outputToCSV()).grid(row=0, column=3, padx=5)





#keyboard functions


def getInput():
    
    #
    #if recording == False:
    #    recording = True
    #    b1.config(text = 'Stop Recording')
    #elif recording == True:
    #    recording = False
    #    b1.config(text = 'Start Recording')
    
    print("input function here")

def quit():
    mw.destroy()

def outputToCSV():
    print("output function")


mainloop() #runs interface



 