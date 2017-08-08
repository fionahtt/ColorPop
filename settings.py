# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *

def initSettings(data):
    data.leftX = 88
    data.rightX = 515
    
    data.unpauseY1 = 176
    data.unpauseY2 = 275
    
    data.restartY1 = 335
    data.restartY2 = 434
    
    data.exitY1 = 491
    data.exitY2 = 589

def drawSettings(canvas, data):
    levels= PhotoImage(file = "settingsMenu.gif")
    label = Label(image=levels)
    label.image = levels
    label.pack()
    canvas.create_image(0, 0, anchor = NW, image = label.image)
            
def settingsMousePressed(event, data):
    if(event.x>data.leftX and event.x < data.rightX):
        if (event.y >data.unpauseY1 and event.y<data.unpauseY2):
            print("hi")
 #           data.mode = "play"
        elif (event.y >data.restartY1 and event.y<data.restartY2):
            print("hello!!")
 #           data.mode = "play"
        elif (event.y >data.exitY1 and event.y<data.exitY2):
            data.mode = "homeScreen"