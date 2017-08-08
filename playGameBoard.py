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
    data.numColors = 2
    data.game = 0
    data.boardFinished = False
    data.gameOver = False
    data.score = 0
    data.highScore = 0
    data.sectionSize = 1
    data.visited = set()
    #generateBoard(data)
    
def drawGameBoard(canvas, data):
    if (data.gameOver):
        data.mode = "playGameOver"
    else:
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
                else:
                    color = "white"
                    
                canvas.create_rectangle(data.startX + (c*data.blockSize) + (c*data.margin), data.startY + (r*data.blockSize) + (r*data.margin), data.startX + ((c+1)*data.blockSize) + (c*data.margin), data.startY + ((r+1)*data.blockSize) + (r*data.margin), fill = color, outline = "")
            
def drawLabels(canvas, data):
    settings= PhotoImage(file = "settings.gif")
    label = Label(image=settings)
    label.image = settings
    label.pack()
    canvas.create_image(275, 30, anchor = NW, image = label.image)
    canvas.create_text(30, 50, anchor = NW, text = "DIFFICULTY: " + data.level, fill = "black", font = "Verdana 20")
    canvas.create_text(400, 50, anchor = NW, text = "SCORE: " + str(data.score), fill = "black", font = "Verdana 20")
    
def getNumColors(data):
    if (data.level == "EASY"):
        data.numColors = 2
    elif (data.level == "MEDIUM"):
        data.numColors = 4
    elif (data.level == "HARD"):
        data.numColors = 6
    
def generateBoard(data):
    getNumColors(data)
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
            data.gameBoard[x[0]][x[1]] = 0
        data.score += len(data.visited) * (len(data.visited) - 1)
        
def fillBoard(data, row, col):
    #fill down
    for col in range(data.size):
        newCol = []
        for row in range(data.size-1, -1, -1):
            if (data.gameBoard[row][col] != 0):
                newCol.append(data.gameBoard[row][col])
        length = len(newCol)
        newCol += [0] * (10-length)
        for row in range(data.size):
            data.gameBoard[row][col] = newCol[data.size - row-1]
    
    #fill to left
    newBoard = [([0]*data.size) for i in range(data.size)]
    counter = 0
    for col in range(data.size):
        for row in range(data.size):
            if (data.gameBoard[row][col] != 0):
                for row1 in range(data.size):
                    newBoard[row1][counter] = data.gameBoard[row1][col]
                counter += 1
                break
    for row in range(data.size):
        for col in range(data.size):
            data.gameBoard[row][col] = newBoard[row][col]
            
def checkGameOver(data):
    max = 1
    gameOver = True
    for row in range(data.size):
        for col in range(data.size):
            data.visited = set()
            getSectionSize(data, row, col)
            if (len(data.visited) > max):
                gameOver = False
    if (data.boardFinished):
        gameOver = False
    data.gameOver = gameOver
    
def checkBoardFinished(data):
    boardFinished = True
    for row in range(data.size):
        for col in range(data.size):
            if(data.gameBoard[row][col] != 0):
                boardFinished = False
    data.boardFinished = boardFinished
    
def playMousePressed(event, data):
    #settings button
    if (event.x>276 and event.x<319 and event.y>31 and event.y<72):
        data.mode = "settings"
    col = int((event.x-30)//55)
    row = int((event.y-145)//55)
    removeSection(data,row, col)
    fillBoard(data, row, col)
    checkBoardFinished(data)
    checkGameOver(data)

def playTimerFired(data):
    if (not data.gameOver):
        if(data.boardFinished):
            data.game += 1
            generateBoard(data)
    else:
        if (data.score>data.highScore):
            data.highScore = data.score

    
