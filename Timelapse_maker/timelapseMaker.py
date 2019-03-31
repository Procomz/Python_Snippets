# -*- coding: utf-8 -*-

import os
import cv2

#TODO optimize the size of the ouput file : cf fourcc codec  

class timelapseMaker:
    def __init__(self):
        self.pictures = []
    
    def readPictures(self, lenmax = 0, path = None):
        if path is None:
            path = os.path.join(os.path.realpath('.'), 'in')
            print(path)
        
        #reads all pictures under the given directory path.
        for (root, dirs, files) in os.walk(path):
            for file in files:
                if file.lower().endswith(".jpg"):
                    self.pictures.append(os.path.join(root, file))
                if len(self.pictures) > lenmax and lenmax != 0:
                    break
    
    def printList(self):
        for pic in self.pictures:
            print(pic)
            
    def printNumber(self):
        print(str(len(self.pictures)) + " pictures found")
        
    def buildTM(self, filename = 'video.avi', fps = 30):
        if len(self.pictures) == 0:
            raise RuntimeError("No picture")
        
        frame = cv2.imread(self.pictures[0])
        height, width, layers = frame.shape
        
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        
        video = cv2.VideoWriter(filename, fourcc, fps, (width, height))
        
        for pic in self.pictures:
            video.write(cv2.imread(pic))
            print(pic + " is done")
            
        # close any opened window
        cv2.destroyAllWindows()
        video.release()
        print("video released")

if __name__ == '__main__':
    tm = timelapseMaker()
    tm.readPictures()
    tm.printNumber()
    tm.buildTM()
    