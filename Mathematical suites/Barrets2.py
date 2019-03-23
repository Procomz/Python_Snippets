# -*- coding: utf-8 -*-
import itertools

class Barrets2:
#    1/11/21/1211/3112/132112
    def __init__(self, seed):
        self.seed = seed
        self.current = self.seed
        
        self.maxNum = 10
        
        self.lst = []
        self.order = []
        self.currentOrder = 0
        for i in range(self.maxNum):
            self.lst.append(0)
            self.order.append(0)
        
    def computeNext(self):
        items = [list(g) for k,g in itertools.groupby(self.current)]
        
        for item in items:
            self.lst[int(item[0])] = self.lst[int(item[0])] + len(item)
            if int(item[0]) not in self.order:
                self.order[self.currentOrder] = int(item[0])
                self.currentOrder = self.currentOrder + 1
            
        self.build()
        self.printCurrent()
            
    def build(self):
        nextstr = ""
        for i in range(self.maxNum):
            if self.order[i] != 0:
                nextstr = nextstr + str(self.lst[self.order[i]]) + str(self.order[i]) 
        self.current = nextstr
        self.resetLst()
        self.currentOrder = 0
        
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
            self.order[i] = 0
           
if __name__ == "__main__":
    print("debug")
    b = Barrets2('1')
    b.printCurrent()
    for i in range(20):
        b.computeNext()
    