import sys
import os
import getopt

class Options:
    def __init__(self, argv, exename):
        self.state = 'NoState'
        self.county = 'NoCounty'
        self.doplot = True # Plot the graph
        self.exename = exename

        try:
            opts, args = getopt.getopt(argv, "hs:c:n")
        except getopt.GetoptError:
            #print ('cases.py -n -s state')
            print(self.exename, ' [-n  (noplot)] [-s State] [-c County]')
            sys.exit("exiting")
        count = 0
        for opt, arg in opts:
            count += 1
            #print(count, opt, arg)
            if opt == '-h':
                print(self.exename, ' [-n  (noplot)] [-s State] [-c County]')
                sys.exit()
            elif opt in ("-n"):
                self.doplot = False
            elif opt in ("-s"):
                self.state = arg
            elif opt in ('-c'):
                self.county = arg   
    def getState(self):
        return self.state

    def getCounty(self):
        return self.county

    def getDoplot(self):
        return self.doplot
