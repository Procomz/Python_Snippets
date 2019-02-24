# -*- coding: utf-8 -*-

class Conway:
    def __init__(self, startStr):
        self.startStr = startStr
        
    def compute(self):
        for char in self.startStr:
            print(char)
    
if __name__ == "__main__":
    print("debug")
    c = Conway("1")
    c.compute()