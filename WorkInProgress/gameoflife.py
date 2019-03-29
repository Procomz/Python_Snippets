# -*- coding: utf-8 -*-

from image import imageTool
import random

WHITE = [255,255,255]
RED = [255,0,0]
GREEN = [0,255,0]

NONE = WHITE
ALIVE = GREEN
DEAD = RED

class gameOfLife:
    def __init__(self, gridSize, gridHeight, gridWidth):
        self.gridSize = gridSize
        self.gridHeight = gridHeight
        self.gridWidth = gridWidth
        self.image = imageTool(gridWidth*gridSize, gridHeight*gridSize, self.gridSize)
        self.data = self.image.getGrid()
    
    def newGame(self, path, numberOfAlive):
        #erasing the board
        for i in range(self.gridHeight):
            for j in range(self.gridWidth):
                self.data[i,j] = NONE
                
        for i in range(numberOfAlive):
            self.data[random.randint(0,self.gridHeight-1), random.randint(0,self.gridWidth-1)] = ALIVE
        
        #loading data into picture
        self.image.setGrid(self.data)
        self.image.gridToImage()
        self.image.save(path)
    
    def nextStep(self, pathOld, pathNew):
        #getting old grid
        self.image.readImage(pathOld)
        self.image.readGrid()
        self.data = self.image.getGrid()
        #next data grid to use
        self.nextData = self.image.getGrid()
        
        #compute next data
        for i in range(self.gridHeight):
            for j in range(self.gridWidth):
                if((self.data[i,j] == ALIVE).all()):
                    if(self.countAlive(i,j) == 3 or self.countAlive(i,j) == 2):
                        self.nextData[i,j] = ALIVE
                    elif(self.countAlive(i,j) > 3 or self.countAlive(i,j) < 2):
                        self.nextData[i,j] = DEAD
                    else:
                        pass
                elif((self.data[i,j] == NONE).all() or (self.data[i,j] == DEAD).all()):
                    if(self.countAlive(i,j) == 3):
                        self.nextData[i,j] = ALIVE
                    else:
                        self.nextData[i,j] = NONE
                else:
                    raise Exception('error in the picture')
                    
        self.image.setGrid(self.nextData)
        self.image.gridToImage()
        self.image.save(pathNew)
    
    def countAlive(self, currentHeight, currentWidth):
        count = 0;
        if(currentHeight >= 1 and currentWidth >= 1):
            if((self.data[currentHeight-1, currentWidth-1] == ALIVE).all()):
                count+=1
        if(currentHeight >= 1 and currentWidth >= 0):
            if((self.data[currentHeight-1, currentWidth] == ALIVE).all()):
                count+=1
        if(currentHeight >= 1 and currentWidth <= (self.gridWidth-2)):
            if((self.data[currentHeight-1, currentWidth+1] == ALIVE).all()):
                count+=1
        if(currentHeight >= 0 and currentWidth >= 1):
            if((self.data[currentHeight, currentWidth-1] == ALIVE).all()):
                count+=1
        if(currentHeight >= 1 and currentWidth <= (self.gridWidth-2)):
            if((self.data[currentHeight, currentWidth+1] == ALIVE).all()):
                count+=1
        if(currentHeight <= (self.gridHeight-2) and currentWidth >= 1):
            if((self.data[currentHeight+1, currentWidth-1] == ALIVE).all()):
                count+=1
        if(currentHeight <= (self.gridHeight-2) and currentWidth >= 0):
            if((self.data[currentHeight+1, currentWidth] == ALIVE).all()):
                count+=1
        if(currentHeight <= (self.gridHeight-2) and currentWidth <= (self.gridWidth-2)):
            if((self.data[currentHeight+1, currentWidth+1] == ALIVE).all()):
                count+=1
            
        return count

if __name__ == '__main__':
    #Wfor 1920*1080 game
    game = gameOfLife(60, 18, 32)
    #half of the game
    game.newGame('C://Dev/game0.png', (9*32))
    
    for i in range(2):
        string = 'C://Dev/game' + str(i) +'.png'
        stringp1 = 'C://Dev/game' + str(i+1) +'.png'
        print(string)
        game.nextStep(string, stringp1)
        
        