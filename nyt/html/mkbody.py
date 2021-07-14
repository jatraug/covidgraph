

import os, sys
from stat import *
import re
from dotenv import load_dotenv
load_dotenv()


##pathname = '/Users/jimt/work/covid/nyt/images
covwork = os.environ.get('COVWORK')
imgpathname = os.environ.get('IMGPATH')

def makeCaption(jname):
    ''' make a captin from the jpeg name

    '''
    caption = ''
    
    goaway = re.compile(r'_2\d{3}-\d{2}-\d{2}.*')
    caption = re.sub(goaway, '', jname)
    return caption
    
def mkHtmlWithFiles(pathname, smclass="", lgclass=""):
    #print('pathname = ', pathname)
    lcount = 0
    filearr = []
    for file in os.listdir(pathname):
        filearr.append(file)
    filearr.sort()
    for f in filearr:
        fname = os.path.join(pathname, f)
        ourstat = os.stat(fname)
        mode = ourstat.st_mode
        if S_ISREG(mode) and f != '.DS_Store':
            print(f'<a img class=\"{lgclass}\" href=\"{fname}\">\n\
            <img class=\"{smclass}\"src=\"{fname}\">\n', end='')
            
            print(makeCaption(f), end='') 
            print('</a>', end='')
            lcount +=1
            if lcount %2 == 0:
                print('<p>')
            ##print(f'<img class=\"{xclass}\" src=\"{fname}\">')


    print('</html>')                   

mkHtmlWithFiles(imgpathname, 'crop-img', 'large-img')
