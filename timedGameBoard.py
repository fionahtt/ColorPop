# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *
import random

from playGameBoard import *

def initTimedBoard(data):
    initGameBoard(data)
    data.time = 300
    data.boards = 0
    data.level = "EASY"
    data.mostBoards = 0
    
def drawTimedBoard(canvas, data):
    if (data.gameOver):
        data.mode = "timedGameOver"
    else:
        drawTimedLabels(canvas, data)
        for r in range(data.size):
            for c in range(data.size):
                color = data.gameBoard[r][c]
                if (color == "pink"):
                    color = "#F18D9E"
                elif(color == "yellow"):
                    color = "#F5E356"
                elif(color == "turquoise"):
                    color = "#5BC8AC"
                elif(color == "green"):
                    color = "#9BC01C"
                elif (color == "blue"):
                    color = "#4897D8"
                elif (color == "lavender"):
                    color = "#9A9EAB"
                elif (color == "orange"):
                    color = "#F9A603"
                else:
                    color = "white"
                    
                canvas.create_rectangle(data.startX + (c*data.blockSize) + (c*data.margin), data.startY + (r*data.blockSize) + (r*data.margin), data.startX + ((c+1)*data.blockSize) + (c*data.margin), data.startY + ((r+1)*data.blockSize) + (r*data.margin), fill = color, outline = "")
            
def drawTimedLabels(canvas, data):
    settings= PhotoImage(file = "settings.gif")
    label = Label(image=settings)
    label.image = settings
    label.pack()
    canvas.create_image(275, 30, anchor = NW, image = label.image)
    time = str(int(data.time)//60) + ":" + str(int(data.time)%60)
    canvas.create_text(30, 50, anchor = NW, text = "TIME: " + time, fill = "black", font = "Verdana 20")
    canvas.create_text(400, 50, anchor = NW, text = "BOARDS: " + str(data.boards), fill = "black", font = "Verdana 20")
    
            
def checkTimedGameOver(data):
    if (data.time == 0):
        data.gameOver = True
    
def checkTimedBoardFinished(data):
    boardFinished = True
    for row in range(data.size):
        for col in range(data.size):
            if(data.gameBoard[row][col] != 0):
                boardFinished = False
    data.boardFinished = boardFinished

def checkNoMoreMoves(data):
    max = 1
    for row in range(data.size):
        for col in range(data.size):
            data.visited = set()
            getSectionSize(data, row, col)
            if (len(data.visited) > max):
                return False
    return True

def timedMousePressed(event, data):
    if (event.x>276 and event.x<319 and event.y>31 and event.y<72):
        
        
        
        ########PAUSE TIMER
        
        data.mode = "timedSettings"
    col = int((event.x-30)//55)
    row = int((event.y-145)//55)
    removeSection(data,row, col)
    fillBoard(data, row, col)
    checkTimedBoardFinished(data)
    checkTimedGameOver(data)

def timedTimerFired(data):
    if (not data.gameOver):
        data.time -= 0.1
        if(data.boardFinished):
            data.boards += 1
            if(data.boards >4 and data.boards <10):
                data.level = "MEDIUM"
            elif(data.boards>9):
                data.level = "HARD"
            generateBoard(data)
        elif (checkNoMoreMoves(data)):
            generateBoard(data)
    else:
        #check for most boards
        data.mode = "timedGameOver"

    
