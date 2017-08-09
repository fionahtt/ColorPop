# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *

from playGameBoard import *
from timedGameBoard import *
from playGameOver import *

def drawTimedGameOver(canvas, data):
    timedGameOver= PhotoImage(file = "timedGameOver.gif")
    label = Label(image=timedGameOver)
    label.image = timedGameOver
    label.pack()
    canvas.create_image(0,0, anchor = NW, image = label.image)
    canvas.create_text(302,323, text = str(data.boards), fill = "black", font = "Verdana 100")
    canvas.create_text(327,415, anchor = NW, text = str(data.mostBoards), fill = "black", font = "Verdana 20")
            
def timedGameOverMousePressed(event, data):
    if(event.x>data.gameOverX1 and event.x < data.gameOverX2):
        if (event.y >data.againY1 and event.y<data.againY2):
            data.mode = "timed"
            data.boards = 0
            data.level = "EASY"
            data.time = 300
            data.gameOver = False
            generateBoard(data)
        elif (event.y >data.overExitY1 and event.y<data.overExitY2):
            data.mode = "homeScreen"
            data.gameOver = False