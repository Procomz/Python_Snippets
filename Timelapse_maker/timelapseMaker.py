# -*- coding: utf-8 -*-

import os

class timelapseMaker:
    def __init__(self):
        self.pictures = []
    
    def readPictures(self, path = None):
        if path is None:
            path = os.path.join(os.path.realpath('.'), 'in')
            print(path)
        
        #reads all pictures under the given directory path.
        for (root, dirs, files) in os.walk(path):
            for file in files:
                if file.lower().endswith(".jpg"):
                    self.pictures.append(os.path.join(root, file))
    
    def printList(self):
        for pic in self.pictures:
            print(pic)
            
    def printNumber(self):
        print(str(len(self.pictures)) + " pictures found")

if __name__ == '__main__':
    #print(os.)
    tm = timelapseMaker()
    tm.readPictures()
    tm.printNumber()
    