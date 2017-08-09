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
    #coordinates to draw timed button and tutorial button
    data.timedX = 50
    data.timedY = 450
    data.tutorialX = 325
    data.tutorialY = 450
    
    #coordinates to click timed button
    data.timedX1 = 92
    data.timedY1 = 472
    data.timedX2 = 248
    data.timedY2 = 629
    
    #coordinates to click tutorial button
    data.tutorialX1 = 366
    data.tutorialY1 = 472
    data.tutorialX2 = 522
    data.tutorialY2 = 629
    
def homeMousePressed(event, data):
    #click play, go to level chooser
    if (event.x>=256 and event.x <= 358 and event.y >=220 and event.y <=327):
        data.mode = "levelChooser"
    #click timed, reset timed game variables, go to timed game
    elif (event.x>=data.timedX1 and event.x <= data.timedX2 and event.y >=data.timedY1 and event.y <=data.timedY2):
        data.mode = "timed"
        data.level = "EASY"
        data.boards = 0
        data.time = 300
        generateBoard(data)
    #click tutorial, go to tutorial
    elif (event.x>=data.tutorialX1 and event.x <= data.tutorialX2 and event.y >=data.tutorialY1 and event.y <=data.tutorialY2):
        data.mode = "tutorial"

def drawHomeScreen(canvas, data):
    #title
    title= PhotoImage(file = "colorpoptitle.gif")
    label = Label(image=title)
    label.image = title
    label.pack()
    canvas.create_image(0,0, anchor = NW, image = label.image)
    canvas.create_line(20, 120, 580, 120, fill = "black")
    
    #play button
    play= PhotoImage(file = "play.gif")
    label = Label(image=play)
    label.image = play
    label.pack()
    canvas.create_image(175,175, anchor = NW, image = label.image)
    
    #timed mode button
    timed= PhotoImage(file = "timed.gif")
    label = Label(image=timed)
    label.image = timed
    label.pack()
    canvas.create_image(data.timedX,data.timedY, anchor = NW, image = label.image)
    
    #tutorial button
    tutorial= PhotoImage(file = "tutorial.gif")
    label = Label(image=tutorial)
    label.image = tutorial
    label.pack()
    canvas.create_image(data.tutorialX,data.tutorialY, anchor = NW, image =         label.image)