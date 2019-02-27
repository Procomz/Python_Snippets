# -*- coding: utf-8 -*-
import itertools

class Barrets:
#    1/11/21/1112/3112/211213...
    def __init__(self, seed):
        self.seed = seed
        self.current = self.seed
        
        self.maxNum = 10
        
        self.lst = []
        for i in range(self.maxNum):
            self.lst.append(0)
        
    def computeNext(self):
        items = [list(g) for k,g in itertools.groupby(self.current)]
        
        for item in items:
            self.lst[int(item[0])] = self.lst[int(item[0])] + len(item)
            
        self.build()
        self.printCurrent()
            
    def build(self):
        nextstr = ""
        for i in range(self.maxNum):
            if self.lst[i] != 0:
                nextstr = nextstr + str(self.lst[i]) + str(i) 
        self.current = nextstr
        self.resetLst()
        
    def printLst(self):
        for i in range(self.maxNum):
            print(self.lst[i])
            
    def getCurrent(self):
        return self.current

    def printCurrent(self):
        print(self.current)
        
    def resetLst(self):
        for i in range(self.maxNum):
            self.lst[i] = 0
           
if __name__ == "__main__":
    print("debug")
    b = Barrets('1')
    b.printCurrent()
    for i in range(20):
        b.computeNext()
    