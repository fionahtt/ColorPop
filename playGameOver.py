# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *

from playGameBoard import *

def initplayGameOver(data):
    data.gameOverX1 = 85
    data.gameOverX2 = 514

    data.againY1 = 469
    data.againY2 = 569
    
    data.overExitY1 = 602
    data.overExitY2 = 700

def drawPlayGameOver(canvas, data):
    playGameOver= PhotoImage(file = "playGameOver.gif")
    label = Label(image=playGameOver)
    label.image = playGameOver
    label.pack()
    canvas.create_image(0,0, anchor = NW, image = label.image)
    canvas.create_text(302,323, text = str(data.score), fill = "black", font = "Verdana 100")
    canvas.create_text(327,415, anchor = NW, text = str(data.highScore), fill = "black", font = "Verdana 20")
            
def playGameOverMousePressed(event, data):
    if(event.x>data.gameOverX1 and event.x < data.gameOverX2):
        if (event.y >data.againY1 and event.y<data.againY2):
            data.mode = "play"
            data.score = 0
            data.game = 0
            data.gameOver = False
            generateBoard(data)
        elif (event.y >data.overExitY1 and event.y<data.overExitY2):
            data.mode = "homeScreen"
            data.gameOver = False