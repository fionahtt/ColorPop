# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################
from tkinter import *

from playGameBoard import *
from timedGameBoard import *
from settings import *
            
def timedSettingsMousePressed(event, data):
    if(event.x>data.leftX and event.x < data.rightX):
        if (event.y >data.unpauseY1 and event.y<data.unpauseY2):
            data.mode = "timed"
        elif (event.y >data.restartY1 and event.y<data.restartY2):
            data.mode = "timed"
            data.boards = 0
            data.level = "EASY"
            data.time = 300
            generateBoard(data)
        elif (event.y >data.exitY1 and event.y<data.exitY2):
            data.mode = "homeScreen"