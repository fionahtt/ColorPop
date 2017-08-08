# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *
import random

def initGameBoard(data):
    data.startX = 30
    data.startY = 145
    data.size = 10
    data.blockSize = 50
    data.margin = 5
    data.gameBoard = [([0]*data.size) for i in range(data.size)]
    data.colors = ["pink", "yellow", "turquoise", "green", "blue", "lavender", "orange"]
    data.level = "EASY"
    data.game = 0
    data.boardFinished = False
    data.gameOver = False
    data.score = 0
    data.sectionSize = 1
    data.visited = set()
    if (data.level == "EASY"):
        data.numColors = 2
    elif (data.level == "MEDIUM"):
        data.numColors = 4
    elif (data.level == "HARD"):
        data.numColors = 6
    generateBoard(data)
    
def drawGameBoard(canvas, data):
    drawLabels(canvas, data)
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
                
            canvas.create_rectangle(data.startX + (c*data.blockSize) + (c*data.margin), data.startY + (r*data.blockSize) + (r*data.margin), data.startX + ((c+1)*data.blockSize) + (c*data.margin), data.startY + ((r+1)*data.blockSize) + (r*data.margin), fill = color, outline = "")
            
def drawLabels(canvas, data):
    settings= PhotoImage(file = "settings.gif")
    label = Label(image=settings)
    label.image = settings
    label.pack()
    canvas.create_image(275, 30, anchor = NW, image = label.image)
    canvas.create_text(30, 50, anchor = NW, text = "DIFFICULTY: " + data.level, fill = "black", font = "Verdana 20")
    canvas.create_text(400, 50, anchor = NW, text = "SCORE: " + str(data.score), fill = "black", font = "Verdana 20")
    
def generateBoard(data):
    data.score = 0
    data.game += 1
    data.boardFinished = False
    for r in range(data.size):
        for c in range(data.size):
            data.gameBoard[r][c] = data.colors[random.randint(0,data.numColors)]
            while (not checkSection(data,r,c)):
                data.gameBoard[r][c] = data.colors[random.randint(0,data.numColors)]
            
    #depending on game number, make board harder

def checkSection(data, row, col):
    data.visited = set()
    getSectionSize(data,row, col)
    data.sectionSize = len(data.visited)
    if (data.level == "EASY"):
        if(data.sectionSize > 20-data.game): #or data.sectionSize<4):
            return False
    elif (data.level == "MEDIUM"):
        if(data.sectionSize > 15-data.game): #or data.sectionSize<3):
            return False
    elif(data.level == "HARD"):
        if(data.sectionSize > 10-data.game): #or data.sectionSize<2):
            return False
    return True
    
def checkColor(data, row1, col1, row2, col2):
    if(isValid(data, row1, col1) and isValid(data,row2, col2)):
        if(data.gameBoard[row1][col1] == data.gameBoard[row2][col2]):
            return True
    return False
    
def isValid(data, row, col):
    if (row<0 or row>9 or col<0 or col>9):
        return False
    elif (data.gameBoard[row][col] == 0):
        return False
    return True   
    
def getSectionSize(data, row, col):
    data.visited.add((row, col))

    if(checkColor(data, row, col, row, col+1)): #right
        if(not (row, col+1) in data.visited):
            getSectionSize(data, row, col+1)
    if(checkColor(data,row, col, row, col-1)): #left
        if (not (row, col-1) in data.visited):
            getSectionSize(data, row, col-1)
    if(checkColor(data, row, col, row +1, col)): #down
        if (not (row+1, col) in data.visited):
            getSectionSize(data, row+1, col)       
    if(checkColor(data,row, col, row -1, col)): #up
        if (not (row-1, col) in data.visited):
            getSectionSize(data, row-1, col)
    return
    
    
def removeSection(data, row, col):
    data.visited = set()
    getSectionSize(data, row, col)
    if (len(data.visited)>1):
        for x in data.visited:
            data.gameBoard[x[0]][x[1]] = "white"
        data.score += len(data.visited) * (len(data.visited) - 1)
    else:
        print("that wasn't a valid move!")
        
    
def playMousePressed(event, data):
    #start playing game
    col = int((event.x-30)//55)
    row = int((event.y-145)//55)
    removeSection(data,row, col)

def playTimerFired(data):
    if (not data.gameOver):
        if(data.boardFinished):
            data.generateBoard()

    
