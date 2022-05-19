'''
append.py - concat two DBs - us-counties.py up to beginning of us-counties-2020.csv

'''

import pandas as pd
import datetime
import numpy as np

countiesFirst = 'us-counties.csv'
countiesSecond = 'us-counties-2022.csv'
countiesFixed = 'us-counties-fixed.csv'


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
                    ##print('YUP')
                    saveline=True
                continue
            else:
                fix.write(f'{line}\n') ##print(line)
        
def concatDB():
    df1 = openDB(countiesFirst)
    df2 = openDB(countiesFixed)

    dfFinal = df1.append(df2)

    print(dfFinal.head())
    print(dfFinal.tail())
    

    
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
