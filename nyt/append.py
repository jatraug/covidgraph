'''
append.py - concat two DBs - us-counties.py up to beginning of us-counties-2020.csv

'''

import pandas as pd
import datetime
import numpy as np

countiesFirst =  'datasets/us-counties.csv' ##Dnloaded from github; ends with 2022-05-13
countiesSecond = 'datasets/us-counties-2022.csv' ## GOOD From github; starts before 2022-05-13 - this part needs to be dumped.
countiesFixed =  'datasets/us-counties-fixed.csv' ## output. us-coujnties-2002 fixed
countiesFinal =  'datasets/countiesfinal.csv' ## us-counties and us-counties-fixed concatenated. 



def openCounties2022File():
    with open(countiesSecond, 'r')as cs:
        filecontents = cs.read()
    return filecontents.split('\n')

def remove_2022():
    """
    Use all lines prior to 2022-01-01'
    """
    with open(countiesFinal, 'w') as final:
        with open(countiesFirst,'r') as cf:
            all = cf.read().split('\n')
            goforit = True 
            for line in all:
                if '2022-01-01' in line:
                    goforit = False
                if goforit:
                    final.write(f'{line}\n')
                    
    
def filterCounty():
    ## Remove all lines before this date:
    magicDate ='2022-05-14'
    contents = openCountiesFile()
    saveline = False
    with open(countiesFixed, 'w') as fix:
        for line in contents:
            if not saveline:
                if magicDate in line:
                    fix.write(f'{line}\n') 
                    ##print('YUP')
                    saveline=True
                    continue
            else:
                fix.write(f'{line}\n') ##print(line)
        
def concatDB():
    with open(countiesFinal, 'w') as final:
        with open(countiesFirst,'r') as cf:
            all = cf.read().split('\n')
            for line in all:
                final.write(f'{line}\n')
            all_2022_Lines = openCounties2022File()
            for line2022 in all_2022_Lines:
                if not 'date,county' in line2022:
                    final.write(f'{line2022}\n')
               
#        with open (countiesFixed, 'r') as fix:
#             all2 = fix.read().split('\n')
#             for line in all2:
#                final.write(f'{line}\n')
#        nowlines = openCounties2022File()
#        for line in nowlines:
#            final.write(f'{line}\n')

def doit():
    ##filterCounty()
    concatDB()
    


    
def main():
    doit()


if __name__ == '__main__':
    doit()
