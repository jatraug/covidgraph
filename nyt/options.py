import sys, getopt

class Options:
    def __init__(self, argv):
        self.state = 'Washington'
        self.doplot = True # Plot the graph

        try:
            opts, args = getopt.getopt(argv,"hs:n")
        except getopt.GetoptError:
            print ('cases.py -n -s state')
            sys.exit("exiting")
        count = 0
        for opt, arg in opts:
            count +=1
            $$print(count, opt, arg)
            if opt == '-h':
                print ('cases.py [-n  (noplot)] [-s State]')
                sys.exit()
            elif opt in ("-n"):
                self.doplot = False
            elif opt in ("-s"):
                self.state = arg
                    
    def getState(self):
        return self.state

    def getDoplot(self):
        return self.doplot


