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


    def getState(self):
        return self.opts.getState()

    def getCounty(self):
        return self.opts.getCounty()
    
    def doShow(self):
        if self.opts.getDoplot():
            plt.show() 


    def SetupAndRun(self):
        matplotlib.style.use('fivethirtyeight')
        
        #df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
        df = pd.read_csv('datasets/us-counties.csv' )
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
        for cn in self.counties:
            ours = theState.loc[theState['county'] == cn]
            # current cases at the end
            currentCases = ours.iloc[-1]['cases'] - ours.iloc[-2]['cases']
            print(f'{cn} - {currentCases}')
                            
        




def main(argv):
    dograph = lastDayGraph(argv)
    dograph.SetupAndRun()


    
if __name__ == "__main__":
    main(sys.argv[1:])
