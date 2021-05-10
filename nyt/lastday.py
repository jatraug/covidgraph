## Process nyt data for Washington

import sys
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os
import re

sys.path.append('/Users/jimt/work/python/pytools')
import avg
from options import Options

class lastDayGraph:
    def __init__(self, argv):
        self.opts = Options(argv, os.path.basename(__file__))
        self.counties = []
        self.date = '2020-01-01'


    def getState(self):
        return self.opts.getState()

    def getCounty(self):
        return self.opts.getCount

    
    def doShow(self):
        if self.opts.getDoplot():
            plt.show() 


    def SetupAndRun(self):
        matplotlib.style.use('fivethirtyeight')
        
        df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
        #df = pd.read_csv('datasets/us-counties.csv' )
        print(df.head())
        state = self.getState()
        self.iterateState(df, state)
        
    def getAllCounties(self, theState):
        ''' iterate the state to get all counties
        '''
        counties = {}
        counarr = []
        for i, c in theState.iterrows():
            try:
                counties[c['county']] += 1
            except KeyError:
                counties[c['county']] = 1
        for co in counties.keys():
            counarr.append(co)
        #print([co for co in counties.keys())
        counarr.sort()
        #for cn in list(counarr):
        #    print(cn,' ', end='')
        self.counties = counarr


        
    def appendCounty(self, county):
        self.counties.append(county)

    def iterateState(self,df, statename):
        dates = []
        cases = []
        deaths = []

        theState = df.loc[df['state'] == statename] ## and 'county' == County]
        ##theCounty = theState.loc[theState['county']==County]

        self.getAllCounties(theState)
        self.iterateCounties(theState)

#        first, last = self.getFirstAndLastDates()
#        textstr = f'Graph from {first} to {last}'
#       self.plotdeathdiffs(statename, dates, deaths, textstr)
#        self.plotcasediffs(statename, dates, cases, textstr)
    def iterateCounties(self, theState):
        cases = []
        for cn in self.counties:
            ours = theState.loc[theState['county'] == cn]
            # current cases at the end
            currentCases = ours.iloc[-1]['cases'] - ours.iloc[-2]['cases']
            self.date = ours.iloc[-1]['date']
            print(f'{cn} - {currentCases}')
                            
            print(ours.tail())
            cases.append(currentCases)

        self.plotCurrentCases(cases)
        self.doShow()

    def plotCurrentCases(self, cases):
        fig = plt.figure(figsize=(12.0, 9.0))
        ax = fig.add_subplot(111)

        ax.bar(self.counties, cases, label=self.makeLabel())
        ax.plot(label=self.makeLabel())
        plt.xticks(rotation=90)
        plt.subplots_adjust(bottom=0.40)
        plt.tight_layout()
        plt.legend(loc='best')


    def makeLabel(self):
        text = f'{self.getState()} cases by county for {self.date}'
        print(text)
        return text
        
def main(argv):
    dograph = lastDayGraph(argv)
    dograph.SetupAndRun()


    
if __name__ == "__main__":
    main(sys.argv[1:])
