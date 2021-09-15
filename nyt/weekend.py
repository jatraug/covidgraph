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

def WHATTTT():
    dontRemove = False
    fl = "South Carolina_Charleston_cases.jpg"
    for s in lazyStates:
        if s not in fl:
            dontRemove = True
            break
        if dontRemove == True:
            print("nope")
        else:
            print(f"remove {fl}")



def doOrDontRemove(pathname):

    for f in os.listdir(pathname):
        dontRemove = False
        fname = os.path.join(pathname, f)

        for s in lazyStates:
            if s not in f:
                dontRemove = True
                break        
        if dontRemove == True:
            print(f"{fname}: keep")
        else:
            print(f"remove {fname}")



def main():
    doOrDontRemove(facts.IMAGES)
if __name__ == "__main__":
    main()
