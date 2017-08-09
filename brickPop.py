# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *

#import all the files
from homeScreen import *
from levelChooser import *
from playGameBoard import *
from settings import *
from playGameOver import *
from timedGameBoard import *
from timedSettings import *
from timedGameOver import *
from tutorial import *

#framework from 15-112 course notes

###############
#MAIN INIT: initialize all the screens
#################
def init(data):
    data.mode = "homeScreen"
    data.highScore = 0
    data.mostBoards = 0
    initHomeScreen(data)
    initLevels(data)
    initGameBoard(data)
    initSettings(data)
    initplayGameOver(data)
    initTimedBoard(data)
    initTutorial(data)

##################    
#mousepressed, timer, and draw for all the screens
#############
def mousePressed(event, data):
    if(data.mode == "homeScreen"):
        homeMousePressed(event,data)
    elif (data.mode == "levelChooser"):
        #reset play game variables
        data.level = levelsMousePressed(event,data)
        data.score = 0
        data.game = 0
        generateBoard(data)
    elif(data.mode == "play"):
        playMousePressed(event, data)
    elif(data.mode == "settings"):
        settingsMousePressed(event, data)
    elif (data.mode == "playGameOver"):
        playGameOverMousePressed(event, data)
    elif (data.mode == "timed"):
        timedMousePressed(event, data)
    elif(data.mode == "timedSettings"):
        timedSettingsMousePressed(event, data)
    elif (data.mode == "timedGameOver"):
        timedGameOverMousePressed(event, data)
    elif (data.mode == "tutorial"):
        tutorialMousePressed(event, data)

def keyPressed(event, data):
    pass

def timerFired(data):
    if (data.mode == "play"):
        playTimerFired(data)
    elif (data.mode == "timed"):
        timedTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "homeScreen"):
        drawHomeScreen(canvas, data)
    elif (data.mode == "levelChooser"):
        drawLevels(canvas, data)
    elif (data.mode == "play"):
        drawGameBoard(canvas, data)
    elif (data.mode == "settings" or data.mode == "timedSettings"):
        drawSettings(canvas, data)
    elif(data.mode == "playGameOver"):
        drawPlayGameOver(canvas, data)
    elif (data.mode == "timed"):
        drawTimedBoard(canvas, data)
    elif (data.mode == "timedGameOver"):
        drawTimedGameOver(canvas, data)
    elif (data.mode == "tutorial"):
        drawTutorial(canvas, data)

#############################
#RUN        
######################

def run():
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = 600
    data.height = 750
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Toplevel()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")
    
run()