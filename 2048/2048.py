# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/tkinter.html

import tkinter as tk
import random

class App(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        
        self.rows = 3
        self.columns = 4
        self.numbers = []
        self.texts = []
        
        for r in range(self.rows):
           for c in range(self.columns):
               self.numbers.append(None)
               self.texts.append(tk.StringVar(root))
        
        self.create_widgets()
        
        
    def create_widgets(self):
        self.score = tk.Label(root, text = "Score = ", borderwidth = 1)
        self.score.grid(row = 0, column = 0)
        
        self.quit = tk.Button(root, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(row = self.rows + 1, column = self.columns - 1)
        
        self.reset = tk.Button(root, text= "RESET", fg="red", command=self.reset)
        self.reset.grid(row = self.rows + 1, column = 0)
        
        self.print = tk.Button(root, text= "Print", fg="red", command=self.printGrid)
        self.print.grid(row = self.rows + 1, column = 1)
        
        self.newGrid()

    def reset(self):
        # starts a new game
        self.newGrid()
        
    def newGrid(self):
        # Creates a new grid with only one value in it
        for r in range(self.rows):
           for c in range(self.columns):
              self.texts[r*self.columns+c].set(' ')
              self.numbers[r*self.columns+c] = tk.Label(root, textvariable=self.texts[r*self.columns+c], 
                                                        borderwidth=1, width = 5)
              self.numbers[r*self.columns+c].grid(row=r + 1,column=c)
        self.setRandom()
        
    def newGridID(self):
        # prints debug info into cells
        for r in range(self.rows):
           for c in range(self.columns):
              self.texts[r*self.columns+c].set(str(r*self.columns+c))
              self.numbers[r*self.columns+c] = tk.Label(root, textvariable=self.texts[r*self.columns+c], borderwidth=1 )
              self.numbers[r*self.columns+c].grid(row=r + 1,column=c)
        
    def setRandom(self):
        # gets a number : 2 or 4
        number = random.randint(1,2)
        number = number * 2
        
        while True:
            row = random.randint(0, self.rows-1)
            col = random.randint(0, self.columns-1)
            
            if self.texts[row*self.columns + col].get() == ' ':
                # The cell is empty
                self.texts[row*self.columns + col].set(str(number))
                break
            
    def printGrid(self):
        string = ''
        for r in range(self.rows):
           for c in range(self.columns):
               t = self.texts[r*self.columns + c].get()
               if t == ' ':
                   string += '0 '
               else:
                   string += t + ' ' 
           print(string)
           string = ''

if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
