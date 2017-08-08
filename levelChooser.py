# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *

def initLevels(data):
    data.X1 = 90
    data.X2 = 532
    
    data.easyY1 = 229
    data.easyY2 = 331
    
    data.mediumY1 = 392
    data.mediumY2 = 494
    
    data.hardY1 = 555
    data.hardY2 = 658

def drawLevels(canvas, data):
    levels= PhotoImage(file = "levels.gif")
    label = Label(image=levels)
    label.image = levels
    label.pack()
    canvas.create_image(0, 30, anchor = NW, image = label.image)
            
def levelsMousePressed(event, data):
    if(event.x>data.X1 and event.x < data.X2):
        if (event.y >data.easyY1 and event.y<data.easyY2):
            data.mode = "play"
            return "EASY"
        elif (event.y >data.mediumY1 and event.y<data.mediumY2):
            data.mode = "play"
            return "MEDIUM"
        elif (event.y >data.hardY1 and event.y<data.hardY2):
            data.mode = "play"
            return "HARD"