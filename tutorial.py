# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *

def initTutorial(data):
    data.tutorialMode = 1

def drawTutorial(canvas, data):
    if(data.tutorialMode == 1):
        tutorial1= PhotoImage(file = "tutorial1.gif")
        label = Label(image=tutorial1)
        label.image = tutorial1
        label.pack()
        canvas.create_image(0, 0, anchor = NW, image = label.image)
    elif(data.tutorialMode == 2):
        tutorial2= PhotoImage(file = "tutorial2.gif")
        label = Label(image=tutorial2)
        label.image = tutorial2
        label.pack()
        canvas.create_image(0, 0, anchor = NW, image = label.image)
    elif(data.tutorialMode == 3):
        tutorial3= PhotoImage(file = "tutorial3.gif")
        label = Label(image=tutorial3)
        label.image = tutorial3
        label.pack()
        canvas.create_image(0, 0, anchor = NW, image = label.image)
    elif(data.tutorialMode == 4):
        tutorial4= PhotoImage(file = "tutorial4.gif")
        label = Label(image=tutorial4)
        label.image = tutorial4
        label.pack()
        canvas.create_image(0, 0, anchor = NW, image = label.image)
    elif(data.tutorialMode == 5):
        tutorial5= PhotoImage(file = "tutorial5.gif")
        label = Label(image=tutorial5)
        label.image = tutorial5
        label.pack()
        canvas.create_image(0, 0, anchor = NW, image = label.image)
    elif(data.tutorialMode == 6):
        tutorial6= PhotoImage(file = "tutorial6.gif")
        label = Label(image=tutorial6)
        label.image = tutorial6
        label.pack()
        canvas.create_image(0, 0, anchor = NW, image = label.image)
            
def tutorialMousePressed(event, data):
    if(data.tutorialMode == 1):
        if ((event.x>66 and event.x<234 and event.y>224 and event.y<390) or (event.x>246 and event.x<414 and event.y>225 and event.y<333) or (event.x>425 and event.x<534 and event.y>225 and event.y<273)):
            data.tutorialMode = 2
    elif(data.tutorialMode == 2):
        if ((event.x>67 and event.x<235 and event.y>399 and event.y<683) or (event.x>248 and event.x<416 and event.y>340 and event.y<508) or (event.x>428 and event.x<536 and event.y>281 and event.y<685)):
            data.tutorialMode = 3
    elif(data.tutorialMode == 3):
        if (event.x>67 and event.x<236 and event.y>518 and event.y<684):
            data.tutorialMode = 4
    elif(data.tutorialMode == 4):
        data.tutorialMode = 5
    elif(data.tutorialMode == 5):
        data.tutorialMode = 6
    elif(data.tutorialMode == 6):
        if (event.x>138 and event.x<465 and event.y>455 and event.y<522):
            data.tutorialMode = 1
        elif (event.x>139 and event.x<465 and event.y>549 and event.y<615):
            data.mode = "homeScreen"
            data.tutorialMode = 1
