# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *

class levelChooser(object):
    
    def drawLevels(self, canvas):
        levels= PhotoImage(file = "levels.gif")
        label = Label(image=levels)
        label.image = levels
        label.pack()
        canvas.create_image(0, 30, anchor = NW, image = label.image)
        
        root.bind("<Button-1>", lambda event:
                                self.mousePressedWrapper(event))

    def init(self):
        pass
                
    def mousePressed(self, event):
        #go to game board
        pass
    
    def timerFired(self):
        pass
    
    def redrawAll(self):
        self.drawLevels(self.canvas)

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
        
    def runLevels(self):
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
        
levels = levelChooser()
levels.runLevels()