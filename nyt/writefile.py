'''
write to a file (or append)
'''

from statfile import Statfile as sf

class fWrite():
    def __init__(self):
        self.fname = sf.makeName()

    def append(self,text):
        with open(self.fname, 'a') as fn:
            fn.write(text + '\n')

    def write(self,text):
        with open(self.fname, 'w') as fn:
            fn.write(text + '\n')
        
