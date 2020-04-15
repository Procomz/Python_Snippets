# -*- coding: utf-8 -*-

OK = 0
ERROR = 1

class hex_handler():
    def __init__(self, filepath):
        self.file = open(filepath, 'r')
        # readlines read the next lines not read yet
        self.lines = self.file.readlines()
    
    def printLines(self):
        for line in self.lines:
            if line.endswith('\n'):
                line = line[:-1]
            print(line)
            
    def lineComprehension(self, line):
        # returns data structure in hexa, or None if an error occured
        if line.endswith('\n'):
            line = line[:-1]
        
        if line.startswith(':'):
            sizedata = line[1:3]
            address = line[3:7]
            typeHex = line[7:9]
            data = line[9:-2]
            checksum = line[-2:]
            return (sizedata, address, typeHex, data, checksum)
        else:
            return None
            
    def computeChecksum(self, line):
        computedCks = 0
        
        size, address, typeHex, data, checksum = self.lineComprehension(line)
        
        computedCks += int(size, 16)
        computedCks += int(address[0:2], 16)
        computedCks += int(address[2:4], 16)
        computedCks += int(typeHex, 16)
        for i in range(0, len(data), 2):
            # concatenates two char in a string
            computedCks += int((data[i] + data[i+1]), 16)
        
        computedCks = computedCks % 256
        computedCks = computedCks ^ 0xFF # 1 complement
        computedCks = computedCks + 1
        computedCks = computedCks % 256
        
        return computedCks
        
    def checkChecksum(self, raises = False, debug = False):
        for i, line in enumerate(self.lines):
            if debug:
                print(self.lineComprehension(line))
            size, address, typeHex, data, checksum = self.lineComprehension(line)
            
            computedCks = self.computeChecksum(line)
            if computedCks != int(checksum, 16):
                if raises:
                    raise RuntimeError("Incorrect checksum on line " + str(i+1) 
                                     + ". Found " + str(int(checksum, 16)) 
                                     + " Computed " + str(computedCks))
                return ERROR
        return OK
    

#### @todo not working
    def findClosestAddress(self, address):
        closestAddress = 0
        closestLine = 0
        
        address = int(address, 16)
        
        for i, line in enumerate(self.lines):
            size, addressread, typeHex, data, checksum = self.lineComprehension(line)
            
            addressread = int(addressread, 16)
            if abs(addressread - address) < abs(closestAddress - address):
                # a better address was found
                closestAddress = addressread
                closestLine = i+1
        return (hex(closestAddress), closestLine)
    
        
if __name__ == '__main__':
    file_in = r".\DC37DC38.hex"
#    file_in = r".\CB8R_1.hex"
    
    hh = hex_handler(file_in)
#    hh.printLines()
    hh.checkChecksum(raises = True)
    print(hh.findClosestAddress('0x279C'))
    
    