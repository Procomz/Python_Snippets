# -*- coding: utf-8 -*-

# Qm.n format : 1 bit sign, m bits integer, n bits fraction


class Qformat:
    def __init__(self):
        pass
    
    def convert(self, number):
        if isinstance(number, float):
            print('float ' + str(number))
            print('Q 15.16 format = ' + self.floatToQ1516(number))
        else:
            print('hex ' + str(hex(number)))
            print('float = ' + str(self.Q1516ToFloat(number)))
        
    def floatToQ1516(self, number):
        return hex(int(number * 2 ** 16))
    
    def Q1516ToFloat(self, number):
        return (float(int(number))) / (2 ** 16)
                
if __name__ == "__main__":
    q = Qformat()
    q.convert(1.5)
    q.convert(0x18000)