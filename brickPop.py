# 15-112, Summer 2, Term Project
######################################
# Full name: Fiona Thendean
# Section: B
# Andrew ID: fthendea
######################################

class brickPop(object):


    def init(data):
        pass
        
    def mousePressed(event, data):
        pass
    
    def keyPressed(event, data):
        pass
    
    def timerFired(data):
        pass
    
    def redrawAll(canvas, data):
        pass
            
    def run(self):
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
        data.height = 775
        data.timerDelay = 100 # milliseconds
        init(data)
        # create the root and the canvas
        root = Tk()
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
        
brickPop().run()