# -*- coding: utf-8-*-\

import os, sys
from stat import *
import re
from dotenv import load_dotenv
load_dotenv()
from pathlib import PurePath
import unicodedata

##pathname = '/Users/jimt/work/covid/nyt/images
covwork = os.environ.get('COVWORK')
imgpathname = os.environ.get('IMGPATH') ##.encode('utf-8') ##.decode('utf-8')
imgpathname = unicodedata.normalize('NFC', imgpathname)

def rid(mstr):
    ''' 
    Get rid of nastyugly extra " around strings
    '''
    rstr = re.compile('\"')
    ms = re.sub(rstr, '', mstr)
    return ms


def makeCaption(jname):
    ''' make a captin from the jpeg name

    '''
    caption = ''
    #jname = jname.decode('utf-8')
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
    with  open('body.html', 'w') as fs:
        #fs.write('<body>\n')
        fs.write('<div class="container">\n')
        fs.write('<div class="row">\n')
        fs.write('<hr>')
        fs.write('<a href="./summary.html"><img class="tiny-img" src="summary.png">***Summary of COVID Cases/Deaths***</a>')
        fs.write('<p>\n<p><hr>')

        for f in filearr:
            fname = os.path.join(pathname, f)
            ourstat = os.stat(fname)
            mode = ourstat.st_mode
            if S_ISREG(mode) and f != '.DS_Store':
                fs.write('<div class="col-md-6">\n')
                fs.write( f'<a img class=\"{lgclass}\" href=\"{fname}\">\n<img class=\"{smclass}\"src=\"{fname}\">\n')
            
                fs.write( makeCaption(f)) 
                fs.write('</a>\n')
                fs.write('</div>\n')
                lcount +=1
                if lcount %2 == 0:
                    fs.write('<p>')
                    
            ##print(f'<img class=\"{xclass}\" src=\"{fname}\">')

        fs.write('</div\n')
        fs.write('</div\n')
        fs.write('</body\n')

        fs.write( '</html>')
        

mkHtmlWithFiles(imgpathname, 'crop-img', 'large-img')

os.system('cat head.html body.html > index.html')

