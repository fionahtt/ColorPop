# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *

import levelChooser

class brickPop(object):
    
    def drawHomeScreen(self):
        title= PhotoImage(file = "colorpoptitle.gif")
        label = Label(image=title)
        label.image = title
        label.pack()
        self.canvas.create_image(0,0, anchor = NW, image = label.image)
        self.canvas.create_line(20, 120, 580, 120, fill = "black")
        
        play= PhotoImage(file = "play.gif")
        label = Label(image=play)
        label.image = play
        label.pack()
        self.canvas.create_image(175,175, anchor = NW, image = label.image)
        
        timed= PhotoImage(file = "timed.gif")
        label = Label(image=timed)
        label.image = timed
        label.pack()
        self.canvas.create_image(self.timedX,self.timedY, anchor = NW, image = label.image)
    
        tutorial= PhotoImage(file = "tutorial.gif")
        label = Label(image=tutorial)
        label.image = tutorial
        label.pack()
        self.canvas.create_image(self.tutorialX,self.tutorialY, anchor = NW, image =         label.image)
        
    def initHomeScreen(self):
        self.timedX = 50
        self.timedY = 450
        self.tutorialX = 325
        self.tutorialY = 450
        self.boxWidth = 241
        self.boxHeight = 246
        self.levels = False

    def init(self):
        self.initHomeScreen()
        
    def mousePressed(self, event):
        levels = levelChooser.levelChooser()
        levels.runLevels()
    
    def keyPressed(self, event):
        pass
    
    def timerFired(self):
        pass
    
    def redrawAll(self):
       # if (self.levels):
        #    levels = levelChooser.levelChooser()
         #   levels.drawLevels()
        #else:
        self.drawHomeScreen()

    def redrawAllWrapper(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(0, 0, self.width, self.height,
                                    fill='white', width=0)
        self.redrawAll()
        self.canvas.update()    
    
    def mousePressedWrapper(self, event):
        self.mousePressed(event)
        self.redrawAllWrapper()
    
    def keyPressedWrapper(self, event):
        self.keyPressed(event)
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
        root.bind("<Key>", lambda event:
                                self.keyPressedWrapper(event))
        self.timerFiredWrapper()
        # and launch the app
        root.mainloop()  # blocks until window is closed
        print("bye!")
        
brickPop().run()