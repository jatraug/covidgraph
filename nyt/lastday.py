## Process nyt data for Washington
'''
Graph cases and deaths for all counties of state


'''

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

class fileOpts(Options):
    pass
   # def __init__(self, argv, exename):

        
class lastDayGraph:
    def __init__(self, argv):
        self.opts = fileOpts(argv, os.path.basename(__file__))
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
        try:
            assert self.getState() != 'NoState'
        except AssertionError:
            print('No state entered!')
            sys.exit()
            
        df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
        #df = pd.read_csv('datasets/us-counties.csv' )
        #print(df.head())
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
        deaths =[]
        for cn in self.counties:
            ours = theState.loc[theState['county'] == cn]
            # current cases at the end
            currentCases = ours.iloc[-1]['cases'] - ours.iloc[-2]['cases']
            currentDeaths = ours.iloc[-1]['deaths'] - ours.iloc[-2]['deaths']
            if currentCases < 0:
                currentCases = 0 
            if currentDeaths < 0:
                currentDeaths = 0

            self.date = ours.iloc[-1]['date']
            #print(f'{cn} - {currentCases}')
                            
            #print(ours.tail())
            cases.append(currentCases)
            deaths.append(currentDeaths)

        self.plotCurrentCases(cases)
        self.doShow()
        self.plotCurrentDeaths(deaths)
        self.doShow()        


    def plotCurrentCases(self, cases):
        fig = plt.figure(figsize=(12.0, 9.0))
        ax = fig.add_subplot(111)

        ax.bar(self.counties, cases, label=self.makeLabel('cases'))
        ax.plot(label=self.makeLabel('cases'))
        plt.xticks(rotation=90)
        plt.subplots_adjust(bottom=0.40)
        plt.tight_layout()
        plt.legend(loc='best')
        imgname = self.getimagename('Cases')
        fig.savefig('images/' + imgname, pil_kwargs={'quality': 60}) 

    def plotCurrentDeaths(self, deaths):
        fig = plt.figure(figsize=(12.0, 9.0))
        ax = fig.add_subplot(111)

        ax.bar(self.counties, deaths, label=self.makeLabel('deaths'))

        ax.plot(label=self.makeLabel('deaths'))
        plt.xticks(rotation=90)
        plt.subplots_adjust(bottom=0.40)
        plt.tight_layout()
        plt.legend(loc='best')
        imgname = self.getimagename('Deaths')
        fig.savefig('images/' + imgname, pil_kwargs={'quality': 60}) 


    def makeLabel(self, CorD): ## cases ofr deaths
        text = f'{self.getState()} COVID-19 {CorD} by county for {self.date}'
        #print(text)
        return text

    def getimagename(self, CorD):
        final = f'{self.getState()}{CorD}ByCounty-{self.date}.jpg'
        #print(final)
        return final
        
def main(argv):
    dograph = lastDayGraph(argv)
    dograph.SetupAndRun()


    
if __name__ == "__main__":
    main(sys.argv[1:])
