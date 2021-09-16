"""
Some states don't publish data on weekends. For these states don't
make graphs on weekends.

"""
import timetools as tt #Uncover weekends
import os
import sys
import facts
lazyStates = ["Washington", "Oregon", "South Carolina"]
##  os.remove("file.jpg")




def doOrDontRemove(pathname):

    for f in os.listdir(pathname):
        dontRemove = False
        fname = os.path.join(pathname, f)

        for s in lazyStates:
            if s in f:
                dontRemove = True
                break        
        if dontRemove == True:
            print(f"keep {f}")
        else:
            print(f"remove {f}")



def main():
    doOrDontRemove(facts.DBIMG)
if __name__ == "__main__":
    main()
