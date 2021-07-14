from guizero import App, Combo, Text, CheckBox, ButtonGroup, PushButton, info, TextBox, Picture, Slider, Window, info
from tkinter import *
import tkinter.filedialog

def xz():
    filename = tkinter.filedialog.askopenfilename()

app = App(title="Homepage",bg = "white")
# app.set_full_screen()
btn1 = PushButton(app,text="select",command = xz)
app.display()