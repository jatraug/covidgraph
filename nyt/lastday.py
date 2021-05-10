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
        self.counties = ()
        self.tempCounties = []

    def getState(self):
        return self.opts.getState()

    def getCounty(self):
        return self.opts.getCounty()
    
    def doShow(self):
        if self.opts.getDoplot():
            plt.show() 


    def SetupAndRun(self):
        matplotlib.style.use('fivethirtyeight')
        
        df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
        print(df.head())
        state = self.getState()
        self.iterateState(df, state)
        
    def getAllCounties(self, theState):
        ''' iterate the state to get all counties
        '''
        counties = []
        for i, c in theState.iterrows():
            self.tempCounties.append(c['county'])
        self.counties = tuple(self.tempCounties)
        print([c  for c in self.counties])
        



        
    def appendCounty(self, county):
        self.counties.append(county)

    def iterateState(self,df, statename):
        dates = []
        cases = []
        deaths = []

        theState = df.loc[df['state'] == statename] ## and 'county' == County]
        ##theCounty = theState.loc[theState['county']==County]

        self.getAllCounties(theState)


#        first, last = self.getFirstAndLastDates()
#        textstr = f'Graph from {first} to {last}'
#       self.plotdeathdiffs(statename, dates, deaths, textstr)
#        self.plotcasediffs(statename, dates, cases, textstr)






def main(argv):
    dograph = lastDayGraph(argv)
    dograph.SetupAndRun()


    
if __name__ == "__main__":
    main(sys.argv[1:])
