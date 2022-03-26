"""
    mkstatus - make an html page of the daily stats
"""
import sys

def getFilename():
    fname = sys.argv[1]
    return fname




def mkline():
    """
    Make a func to add html stuff to each line
    """

    colorarr = ['white', 'green']
    index = int(2)
    
    def doit(line):
        nonlocal index
        if not line == '':
            retval = f'<li class="{colorarr[index%2]}band"> {line}</li>'
            index += 1
        else:
            retval = line
        return retval

    return doit























def main():
    all = []
    with open(getFilename(), 'r')as ff:
        all = ff.read()
    doline = mkline()
    for line in all.split('\n'):
        print(doline(line))
        




main()
