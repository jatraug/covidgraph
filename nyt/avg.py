import functools
import numpy as np

DBPRINT = False

def dbprint(str):
    if(DBPRINT  == True):
        print(str)

# Return a running average:
class avg:
    def __init__(self, len):
        self.avg = 0
        self.arr = []
        self.len = len

    def addelemandGetaverage(self,elem):
        avg = 0
        self.arr.append(elem)

        if (len(self.arr) <=1):
            pass
#            return elem/len(self.arr)
        elif(len(self.arr) > self.len):
            self.arr = self.arr[1: self.len +1] ## left shift 1
        dbprint('arr: ' + str( self.arr))
        avg = np.mean(self.arr)
        
        dbprint('avg: '+ str( avg))
        dbprint(f'std: {np.std(self.arr)}')
        return avg




