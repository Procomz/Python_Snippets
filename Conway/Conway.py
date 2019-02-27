# -*- coding: utf-8 -*-
import itertools

class Conway:
    def __init__(self, seed):
        self.seed = seed
        self.current = self.seed
        
    def computeNext(self):
        nextstr = ""
        items = [list(g) for k,g in itertools.groupby(self.current)]
        
        for item in items:
            nextstr = nextstr + str(len(item)) + item[0]
            
        self.current = nextstr
        return self.current
        
    def printCurrent(self):
        print(self.current)
    
    def getCurrent(self):
        return self.current
        
if __name__ == "__main__":
    print("debug")
    c = Conway('1')
    c.printCurrent()
    for i in range(10):
        print(c.computeNext())
    