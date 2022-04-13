"""
    mkstatus - make an html page of the daily stats
"""

import sys
sys.path.append('../')
import statfile as sf
import linehelp as LH

def getFilename():
    fname = f'{sf.Statfile.makeName()}'
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
    lh = LH.LineHelper()
    all = []
    with open(getFilename(), 'r')as ff:
        all = ff.read()
    doline = mkline()
    lines = all.split('\n')
    lh.maxChars(lines)
    lh.mkTopLine()
    for line in lines:
        ##print(doline(line))
        
        if (ll := lh.changeLine(line)):
            print (doline(ll))




main()
