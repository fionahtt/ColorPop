# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *

def drawLevels(canvas, data):
    levels= PhotoImage(file = "levels.gif")
    label = Label(image=levels)
    label.image = levels
    label.pack()
    canvas.create_image(0, 30, anchor = NW, image = label.image)
            
def levelsMousePressed(event, data):
    data.mode = "play"