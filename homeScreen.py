# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *

def drawHomeScreen(canvas, data):
    title= PhotoImage(file = "colorpoptitle.gif")
    label = Label(image=title)
    label.image = title
    label.pack()
    canvas.create_image(0,0, anchor = NW, image = label.image)
    canvas.create_line(20, 120, 580, 120, fill = "black")
    
    play= PhotoImage(file = "play.gif")
    label = Label(image=play)
    label.image = play
    label.pack()
    canvas.create_image(175,175, anchor = NW, image = label.image)
    
    timed= PhotoImage(file = "timed.gif")
    label = Label(image=timed)
    label.image = timed
    label.pack()
    canvas.create_image(data.timedX,data.timedY, anchor = NW, image = label.image)

    tutorial= PhotoImage(file = "tutorial.gif")
    label = Label(image=tutorial)
    label.image = tutorial
    label.pack()
    canvas.create_image(data.tutorialX,data.tutorialY, anchor = NW, image = label.image)    
    

def init(data):
    data.timedX = 50
    data.timedY = 450
    data.tutorialX = 325
    data.tutorialY = 450
    data.boxWidth = 241
    data.boxHeight = 246
        
def mousePressed(event, data):
    print("X:" + str(event.x))
    print("Y: " + str(event.y))
    
def keyPressed(event, data):
    pass
    
def timerFired(data):
    pass
    
def redrawAll(canvas, data):
    drawHomeScreen(canvas, data)
            
def run():
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                    fill='white', width=0)
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