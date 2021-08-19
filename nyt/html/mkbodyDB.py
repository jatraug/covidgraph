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
dbox = '/users/jimt/Dropbox/Work/covid'

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
    #if not isinstance(pathname, str):
        #pathname = bytes(pathname, 'utf-8')
        #pathname = pathname.encode('utf-8').decode('utf-8')
        #pass
    for file in os.listdir(pathname):
        filearr.append(file)
    filearr.sort()
    Dpath = 'images' ##Dropbox file location and name
    with  open('bodyDB.html', 'w') as fs:
        for f in filearr:
            fname = os.path.join(pathname, f)
            Dname =  os.path.join(Dpath, f)
            ourstat = os.stat(fname)
            mode = ourstat.st_mode
            if S_ISREG(mode) and f != '.DS_Store':
                fs.write( f'<a img class=\"{lgclass}\" href=\"{Dname}\">\n<img class=\"{smclass}\"src=\"{Dname}\">\n')
            
                fs.write( makeCaption(f)) 
                fs.write('</a>')
                lcount +=1
                if lcount %2 == 0:
                    fs.write('<p>')
            ##print(f'<img class=\"{xclass}\" src=\"{fname}\">')


        fs.write( '</html>')
        

mkHtmlWithFiles(imgpathname, 'crop-img', 'large-img')

os.system('cat head.html bodyDB.html > indexDB.html')
