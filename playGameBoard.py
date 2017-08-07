# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *
import random

class playGameBoard(object):
    
    def drawGameBoard(self, canvas):
        self.drawLabels(self.canvas)
        for r in range(self.size):
            for c in range(self.size):
                color = self.gameBoard[r][c]
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
                    
                canvas.create_rectangle(self.startX + (c*self.blockSize) + (c*self.margin), self.startY + (r*self.blockSize) + (r*self.margin), self.startX + ((c+1)*self.blockSize) + (c*self.margin), self.startY + ((r+1)*self.blockSize) + (r*self.margin), fill = color, outline = "")
                
    def drawLabels(self, canvas):
        settings= PhotoImage(file = "settings.gif")
        label = Label(image=settings)
        label.image = settings
        label.pack()
        canvas.create_image(275, 30, anchor = NW, image = label.image)
        canvas.create_text(30, 50, anchor = NW, text = "DIFFICULTY: " + self.level, fill = "black", font = "Verdana 20")
        canvas.create_text(400, 50, anchor = NW, text = "SCORE: " + str(self.score), fill = "black", font = "Verdana 20")
       
        

    def init(self):
        self.startX = 30
        self.startY = 145
        self.size = 10
        self.blockSize = 50
        self.margin = 5
        self.gameBoard = [([0]*self.size) for i in range(self.size)]
        self.colors = ["pink", "yellow", "turquoise", "green", "blue", "lavender", "orange"]
        self.level = "EASY"
        self.game = 0
        self.boardFinished = False
        self.gameOver = False
        self.score = 0
        self.sectionSize = 1
        if (self.level == "EASY"):
            self.numColors = 2
        elif (self.level == "MEDIUM"):
            self.numColors = 4
        elif (self.level == "HARD"):
            self.numColors == 6
        self.generateBoard()
        
    def generateBoard(self):
        self.score = 0
        self.game += 1
        self.boardFinished = False
        for r in range(self.size):
            for c in range(self.size):
                self.gameBoard[r][c] = self.colors[random.randint(0,self.numColors)]
                while (not self.checkSection(r,c)):
                    self.gameBoard[r][c] = self.colors[random.randint(0,self.numColors)]
                
        #depending on game number, make board harder
    
    def checkSection(self, row, col):
        while (self.checkColor(row, col, row, col-1)):
            row-=1
        while(self.checkColor(row, col, row, col+1)):
            row+=1
            self.sectionSize +=1
        
        
        if (self.level == "EASY"):
            if(self.sectionSize > 20-self.game or self.sectionSize<4):
                return False
        elif (self.level == "MEDIUM"):
            if(self.sectionSize > 15-self.game or self.sectionSize<3):
                return False
        elif(self.level == "HARD"):
            if(self.sectionSize > 10-self.game or self.sectionSize<2):
                return False
    
    def checkColor(self, row1, col1, row2, col2):
        if(self.isValid(row1, col1) and self.isValid(row2, col2)):
            if(self.gameBoard[row1][col1] == self.gameBoard[row2][col2]):
                return True
        return False
        
    def isValid(self, row, col):
        if (row<0 or row>9 or col<0 or col>9):
            return False
        elif (self.gameBoard[row][col] == 0):
            return False
        return True
    
    def playGame(self):
        pass
        
    def mousePressed(self, event):
        #start playing game
        pass
    
    def timerFired(self):
        if (not self.gameOver):
            if(self.boardFinished):
                self.generateBoard()
    
    def redrawAll(self):
        self.drawGameBoard(self.canvas)

    def redrawAllWrapper(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(0, 0, self.width, self.height,
                                    fill='white', width=0)
        self.redrawAll()
        self.canvas.update()    
    
    def mousePressedWrapper(self, event):
        self.mousePressed(event)
        self.redrawAllWrapper()
    
    
    def timerFiredWrapper(self):
        self.timerFired()
        self.redrawAllWrapper()
        # pause, then call timerFired again
        self.canvas.after(self.timerDelay, self.timerFiredWrapper)
        
    def run(self):
        self.width = 600
        self.height = 750
        self.timerDelay = 100 # milliseconds
        self.init()
        # create the root and the canvas
        root = Toplevel()
        self.canvas = Canvas(root, width=self.width, height=self.height)
        self.canvas.pack()
        # set up events
        root.bind("<Button-1>", lambda event:
                                self.mousePressedWrapper(event))
        self.timerFiredWrapper()
        # and launch the app
        root.mainloop()  # blocks until window is closed
        print("bye!")
  
playGameBoard().run()
