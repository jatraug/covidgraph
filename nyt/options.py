import sys
import os
import getopt
from version import Version
import re




    
class Options:
    def __init__(self, argv, exename):
        pass
    
    def getDate(self):
        return self.date
    
    def getState(self):
        return self.state

    def getCounty(self):
        return self.county

    def getDoplot(self):
        return self.doplot

    def getVersion(self):
        vers = Version()
        return vers.get()

    def printHelpAndExit(self):
        print(f'usage: {self.exename} [-n  (noplot)] [-s State] [-c County] -v [-d date (2021-03-30)')
        sys.exit('Exiting')
