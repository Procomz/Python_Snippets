# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image
import random

class imageTool:
    def __init__(self, width, height, sizeOfGrid = 1):
        self.width = width
        self.height = height
        self.sizeOfGrid = sizeOfGrid
        
        #pixels of the picture
        self.pixels = np.zeros( (self.height, self.width, 3), dtype=np.uint8 )
        self.img = None
        self.imgRead = None
        
        #grid init
        if(False == self.__checkcompat(self.sizeOfGrid, self.sizeOfGrid)):
            self.data = None
        else:
            self.gridWidth = int(self.width / self.sizeOfGrid)
            self.gridHeight = int(self.height / self.sizeOfGrid)
            self.data = np.zeros((self.gridHeight, self.gridWidth, 3), dtype=np.uint8)
        
    #Creates a checkerboard
    def checkerboard(self, size):
        for i in range(self.height):
            for j in range(self.width):
                if(int(i/size)%2 == 1):
                    if(int(j/size)%2 == 1):
                        self.pixels[i,j] = [0,0,0]
                    else:
                        self.pixels[i,j] = [255,255,255]
                else:
                    if(int(j/size)%2 == 1):
                        self.pixels[i,j] = [255,255,255]
                    else:
                        self.pixels[i,j] = [0,0,0]
        self.__toimage()
    
    #Creates a random image
    def random(self):
        for i in range(self.height):
            for j in range(self.width):
                self.pixels[i,j] = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
        self.__toimage()
        
    def grey(self):
        self.color([128,128,128])
    
    def color(self, rgb):
        for i in range(self.height):
            for j in range(self.width):
                self.pixels[i,j] = rgb
        self.__toimage()
        
    def gridRandom(self):
        for i in range(self.gridHeight):
            for j in range(self.gridWidth):
                self.data[i,j] = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
        self.gridToImage()
    
    def gridCheckerboard(self):
        for i in range(self.gridHeight):
            for j in range(self.gridWidth):
                if((i+j) % 2 == 1):
                    self.data[i,j] = [255,255,255]
                else:
                    self.data[i,j] = [0,0,0]
        self.gridToImage()
        
    def gridToImage(self):                        
        for i in range(self.height):
            for j in range(self.width):
                indexi = int(i/self.sizeOfGrid)
                indexj = int(j/self.sizeOfGrid)
                
                self.pixels[i,j] = self.data[indexi, indexj]
        self.__toimage()
        
    def __toimage(self):
        self.img = Image.fromarray(self.pixels)
        
    #reads a picture and loads pixels values
    def readImage(self, path):
        self.imgRead = Image.open(path, mode = 'r')
        self.pixels = np.array(self.imgRead)
        
    def readGrid(self):
        value = [0,0,0]
        oldValue = [0,0,0]
        
        for k in range(self.gridHeight):
            for l in range(self.gridWidth):
                for i in range(self.sizeOfGrid):
                    for j in range(self.sizeOfGrid):
                        if(i==0 and j==0):
                            value = self.pixels[i+(self.sizeOfGrid*k),j+(self.sizeOfGrid*l)]
                            oldValue = self.pixels[i+(self.sizeOfGrid*k),j+(self.sizeOfGrid*l)]
                        else:
                            oldValue = value
                            value = self.pixels[i+(self.sizeOfGrid*k),j+(self.sizeOfGrid*l)]
                        
                        if((value == oldValue).all()):
                            pass
                        else:
                            raise Exception('Grid not consistent')
                            
                self.data[k,l] = value  
        
    def __checkcompat(self, deltaWidth, deltaHeight):
        if(self.width % deltaWidth != 0):
            return False
        if(self.height % deltaHeight != 0):
            return False
        return True
        
    def show(self):
        self.img.show()
        
    def save(self, path):
        self.img.save(path)
        
    def getGrid(self):
        return self.data
    
    def setGrid(self, grid):
        for i in range(self.gridHeight):
            for j in range(self.gridWidth):
                self.data[i,j] = grid[i,j]
        
if __name__ == '__main__':
    image = imageTool(1920, 1080, 40)
    
    #image.checkerboard(16)
    #image.random()
    #image.grey()
    #image.gridCheckerboard()
    #image.gridRandom()
    
    #image.save('C://Dev/test.png')
    image.readImage('C://Dev/test.png')
    image.readGrid()
    image.gridToImage()
    image.show()