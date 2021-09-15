"""
Some states don't publish data on weekends. For these states don't
make graphs on weekends.

"""
import timetools as tt #Uncover weekends
import os
import sys

lazyStates = ["Washington", "Oregon", "South Carolina"]
##  os.remove("file.jpg")
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
