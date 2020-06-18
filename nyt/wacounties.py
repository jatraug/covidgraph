## List latest for each county in Washington

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import sklearn
from sklearn.cluster import KMeans

import sys
sys.path.append('/Users/jimt/work/python/pytools')
import avg as avg
from options import Options


class countyList:
    def __init__(self):
        self.list = [{'date': '00-00-00', 'county': 'aaa', 'cases': 0, 'deaths':0}] ## DataFrame(columns = ['date', 'county', 'cases', 'deaths'])
                                            

    def insert(self,line):
        #print(line.date, '  ', line.county, '  ', line.cases, '  ', line.deaths)

        self.list.append({'date':line.date, 'county': line.county, 'cases': line.cases, 'deaths': line.deaths})
            
    def sortkey(self, k):
        return k['date']
        
    def getlist(self):
        print('sorting')
        ##        df = self.list.sort_values(by=['county'], inplace=False)
        self.list.sort(reverse=True, key=self.sortkey)
        return self.list
    
    
class countyInfo:
    def __init__(self):
        pass

    def SetupAndRun(self):
        clist = countyList()
        matplotlib.style.use('fivethirtyeight')
        
       ## df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv' )
        df = pd.read_csv('datasets/us-counties.csv' )
        #df = pd.read_csv('datasets/us-states.csv' )
        print (df.head())
        print (df.describe())
        print (df.dtypes)
        
        #print(df['state'][3])
        dates = []
        cases = []
        deaths = []

                #### Change statename for another state: 
        statename  = self.getState() ##'Washington'
        #county = self.getCounty()
            
        for i, j in df.iterrows(): 
            if(j['state'] == statename ):
                clist.insert(j)
                #print(j['date'],j['cases'], j['deaths'])
                cases.append(j['cases'])
#                print('Date: ', 'date')
                dates.append(j['date'])
                deaths.append(j['deaths'])

        
        theList = clist.getlist()
        print(theList)

        df = DataFrame(data=theList,columns = ['date', 'county', 'cases', 'deaths'])
        print(df.head())
        #df2 = df[0]
        #df3 = df2.append(df[1])
        #print('df2: ', d2)
        self.getcountybydate(df)
        #print(df3.head())

        #Get the two top dates from sorted(by date) df:
    def getcountybydate(self,df):
        for i, j in df.iterrows():
            if(i == 0):
                date0 = j['date']
            if(j['date'] != date0):
                #extract these
                dftmp0 = df.iloc[0:i-1]
                ind = i
                date1 = j['date']
        print('dftmp0: ')
        print(dftmp0)




        
    def getState(self):
        return 'Washington'

def main(argv):
    cinfo = countyInfo()
    cinfo.SetupAndRun()


    
if __name__ == "__main__":
    main(sys.argv[1:])
