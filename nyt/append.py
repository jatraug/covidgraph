'''
append.py - concat two DBs - us-counties.py up to beginning of us-counties-2020.csv

'''

import pandas as pd
import datetime
import numpy as np

countiesFirst =  'datasets/us-counties.csv' ##Dnloaded from github; ends with 2022-05-13
countiesSecond = 'datasets/us-counties-2022.csv' ## From github; starts before 2022-05-13 - this part needs to be dumped.
countiesFixed =  'datasets/us-counties-fixed.csv' ## output. us-coujnties-2002 fixed
countiesFinal =  'datasets/countiesfinal.csv' ## us-counties and us-counties-fixed concatenated. 

def openDB(dbName):
    df = pd.read_csv(dbName, infer_datetime_format=True, parse_dates=True)
    return df

def openCountiesFile():
    with open(countiesSecond, 'r')as cs:
        filecontents = cs.read()
        return filecontents.split('\n')


def filterCounty():
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
        with open (countiesFixed, 'r') as fix:
             all2 = fix.read().split('\n')
             for line in all2:
                final.write(f'{line}\n')


    
    #df1 = openDB(countiesFirst)


    #dfFinal = pd.concat(df1,df2, ignore_index=True)

#    dfFinal.to_csv(countiesFinal)
    

    
def doit():
    filterCounty()
    concatDB()
    
    # dfFirst = openDB(countiesFirst)

    # print(dfFirst.head())
    # print(dfFirst.tail())
    # print(dfFirst.dtypes)

    # dfSecond = openDB(countiesSecond)
    # print(dfSecond.head())
    # print(dfSecond.tail())


    # dfTrim = trimDf(dfFirst)
    # #print(dfTrim.tail())
    # #print(dfTrim.dtypes)



def trimDf(df):
    ''' 
    Remove the part of the DB that is duplicated
    '''
    ######dfTrim = pd.to_datetime(df.loc[:'date'])
    ##print(dfTrim.dtypes)
                            

    dfser = df.loc[:'date']
    #dfTrim = df.loc[pd.to_datetime(df[:'date']) < datetime.date.fromisoformat(str('2022-04-18'))]
    #return dfTrim
    print('START')
    print(dfser.head())
    print('DONE')
    
def main():
    doit()


if __name__ == '__main__':
    doit()
