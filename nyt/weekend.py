"""
Some states don't publish data on weekends. For these states don't
make graphs on weekends.

"""
import timetools as tt #Uncover weekends
import os
import sys
import facts
lazyStates = ["Washington", "Oregon", "South Carolina"]
empty = []



##  os.remove("file.jpg")

class RemoveFiles:
    def __init__(self, lazyStates):
        self.removeFiles = []
        self.empty = []
        self.lazyStates = lazyStates

    def doOrDontRemove(self,  pathname):

        for f in os.listdir(pathname):
            keepfile = False
            fname = os.path.join(pathname, f)
                
            for s in self.lazyStates:
                if s in f:
                    keepfile = True
                    break        
            if keepfile == True:
                print(f"keep {f}")
            else:
                print(f"remove {f}")
                self.removeFiles.append(f)



def main():
    rf = RemoveFiles(lazyStates)
    rf.doOrDontRemove(facts.DBIMG)
    
if __name__ == "__main__":
    main()
