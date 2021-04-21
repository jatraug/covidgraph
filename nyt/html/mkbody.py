

import os, sys
from stat import *

pathname = '/Users/jimt/work/covid/nyt/images'

def mkHtmlWithFiles(pathname, smclass="", lgclass=""):
    for f in os.listdir(pathname):
        fname = os.path.join(pathname, f)
        ourstat = os.stat(fname)
        mode = ourstat.st_mode
        if S_ISREG(mode):
            print(f'<a img class=\"{lgclass}\" href=\"{fname}\">\n\
            <img class=\"{smclass}\"src=\"{fname}\">\n\
            </a>')

            ##print(f'<img class=\"{xclass}\" src=\"{fname}\">')


    print('</html>')                   

mkHtmlWithFiles(pathname, 'crop-img', 'large-img')
