# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *

from playGameBoard import *
from timedGameBoard import *

def initHomeScreen(data):
    data.timedX = 50
    data.timedY = 450
    data.tutorialX = 325
    data.tutorialY = 450
    
    data.timedX1 = 92
    data.timedY1 = 472
    data.timedX2 = 248
    data.timedY2 = 629
    
def homeMousePressed(event, data):
    if (event.x>=256 and event.x <= 358 and event.y >=220 and event.y <=327):
        data.mode = "levelChooser"
    elif (event.x>=data.timedX1 and event.x <= data.timedX2 and event.y >=data.timedY1 and event.y <=data.timedY2):
        data.mode = "timed"
        data.level = "EASY"
        data.boards = 0
        data.time = 300
        generateBoard(data)
        

def drawHomeScreen(canvas, data):
    title= PhotoImage(file = "colorpoptitle.gif")
    label = Label(image=title)
    label.image = title
    label.pack()
    canvas.create_image(0,0, anchor = NW, image = label.image)
    canvas.create_line(20, 120, 580, 120, fill = "black")
    
    play= PhotoImage(file = "play.gif")
    label = Label(image=play)
    label.image = play
    label.pack()
    canvas.create_image(175,175, anchor = NW, image = label.image)
    
    timed= PhotoImage(file = "timed.gif")
    label = Label(image=timed)
    label.image = timed
    label.pack()
    canvas.create_image(data.timedX,data.timedY, anchor = NW, image = label.image)

    tutorial= PhotoImage(file = "tutorial.gif")
    label = Label(image=tutorial)
    label.image = tutorial
    label.pack()
    canvas.create_image(data.tutorialX,data.tutorialY, anchor = NW, image =         label.image)