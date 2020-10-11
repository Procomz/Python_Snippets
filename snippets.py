# -*- coding: utf-8 -*-

# Python 3.5.4 on windows
# Spyder 3.2.4


# Testing the interpreter
#
# A lot of problems only come from the interpreter itself. 
# To ensure that the interpreter is working properly, 
# you can use a simple line of code and run it :

print("Hello World.")

# If the text is printed into the current console, the python interpreter is working.


#Finding the version of the interpreter
#
#If you need to find the version of python used to run your code :

import sys
print(sys.version)


# Random numbers in a .csv file

# Just a little script that writes random numbers into the first column of a csv file.

    
import csv, random
with open('test.csv', 'w', newline='') as csvfile:
    
    writer = csv.writer(csvfile)
    
    #writing the file, row by row
    for i in range(100):
        data = [random.randint(0,10)]
        #data needs to be a list
        writer.writerow(data)