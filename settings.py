# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *

def initSettings(data):
    pass

def drawSettings(canvas, data):
    levels= PhotoImage(file = "settingsMenu.gif")
    label = Label(image=levels)
    label.image = levels
    label.pack()
    canvas.create_image(0, 0, anchor = NW, image = label.image)
            
def settingsMousePressed(event, data):
    pass