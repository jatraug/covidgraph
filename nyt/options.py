import sys
import os
import getopt
from version import Version
import re




    
class Options:
    def __init__(self, argv, exename):
        self.state = 'NoState'
        self.county = 'NoCounty'
        self.doplot = True # Plot the graph
        self.exename = exename
        self.date = False
        try:
            opts, args = getopt.getopt(argv, "hs:c:nvd:")
        except getopt.GetoptError:
            self.printHelp()
#            print(self.exename, ' [-n  (noplot)] [-s State] [-c County]')
            sys.exit("exiting")
        count = 0
        for opt, arg in opts:
            count += 1
            #print(count, opt, arg)
            if opt == '-h':
                self.printHelp()
#                print(self.exename, ' [-n  (noplot)] [-s State] [-c County] -v [-d date (2021-03-30)')
                sys.exit()
            elif opt == '-v':
                print(f'Version {self.getVersion()}')
                sys.exit()
            elif opt in ("-n"):
                self.doplot = False
            elif opt in ("-s"):
                self.state = arg
            elif opt in ('-c'):
                self.county = arg
            elif opt in ('-d'):
                self.date = arg
                dtfmt = re.compile('\d{4}-\d{2}-\d{2}')
                matchobj = re.search(dtfmt, self.date)
                if not matchobj:
                    self.printHelp()
                    sys.exit()
                

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

    def printHelp(self):
        print(f'usage: {self.exename} [-n  (noplot)] [-s State] [-c County] -v [-d date (2021-03-30)')
