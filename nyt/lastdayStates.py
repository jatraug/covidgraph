## Process nyt data for Washington
'''
Graph cases and deaths for all states of the US


'''

import sys
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os
import re
from datetime import datetime, timedelta, date


sys.path.append('/Users/jimt/work/python/pytools')
import avg
from options import Options
import getopt
from dotenv import load_dotenv
load_dotenv()

class ourOpts(Options):
    def __init__(self, argv, exename):
        super().__init__(argv, exename)
        self.state = 'NoState'
        self.county = 'NoCounty'
        self.doplot = True # Plot the graph
        self.exename = exename
        self.date = False
        try:
            opts, args = getopt.getopt(argv, "hs:nd:v")
        except getopt.GetoptError:
            self.printHelpAndExit()

        count = 0
        for opt, arg in opts:
            count += 1
            #print(count, opt, arg)
            if opt == '-h':
                self.printHelpAndExit()

            elif opt == '-v':
                print(f'Version {self.getVersion()}')
                sys.exit()
            elif opt in ("-n"):
                self.doplot = False
            elif opt in ("-s"):
                self.state = arg
            elif opt in ('-d'):
                self.date = arg
                dtfmt = re.compile('\d{4}-\d{2}-\d{2}')
                matchobj = re.search(dtfmt, self.date)
                if not matchobj:
                    self.printHelpAndExit()
                    sys.exit()

    def printHelpAndExit(self):
        print(f'usage: {self.exename} [-n  (noplot)] [-s State] -v -d date (2021-03-30)')
        sys.exit('Exiting')
                    
        
class lastDayGraph:
    def __init__(self, argv):
        self.opts = ourOpts(argv, os.path.basename(__file__))
        self.counties = []
        self.date = '2020-01-01'


    def getState(self):
        return self.opts.getState()

    def getLastDate(self):
        return self.opts.getDate()
    
    def doShow(self):
        if self.opts.getDoplot():
            plt.show() 

    def getCsv(self):
        if 'LOCALCSV' in os.environ:
            df = pd.read_csv(os.environ.get('LOCAL_STATES_CSV'))
        else:
            df = pd.read_csv(os.environ.get('NYTIMES_STATES_CSV'))


        return df
    def getListOfStates(self, dfDate):
        states = []
        for i, s in dfDate.iterrows():
            states.append(s['state'])
        
        return list(set(states))
    
    def extractDatesToUse(self, df):
        """
        Get the last date ane nex-ti-last dates in th df.
        """

        lastDate = df.iloc[-1].date
        nextToLastDate = self.dateSubtractOneDay(lastDate) ##df.iloc[-3].date
        return lastDate, nextToLastDate

    def iterateUsForStates(self, df, lastDate, nextToLastDate):
        print(f'dates: {lastDate}   {nextToLastDate}')
## sample:  theState = df.loc[df['state'] == statename]
        dfLastDate = df.loc[df['date'] == lastDate]
        dfNextToLastDate = df.loc[df['date'] == nextToLastDate]
        listOfStates = self.getListOfStates(dfLastDate)
        listOfNextToStates = self.getListOfStates(dfNextToLastDate)
       ## print(listOfStates)


        stateData = {}
        for state in listOfStates:
            casesDeathsData = []
            if state not in listOfNextToStates:
                print (f' {state} is missing!')
            else:
#                print(dfLastDate.loc[dfLastDate['state'] == state].cases)
#                print(dfNextToLastDate.loc[dfNextToLastDate['state'] == state].cases)
                
                casesDeathsData.append(dfLastDate.loc[dfLastDate['state'] == state]['cases'] - dfNextToLastDate.loc[dfNextToLastDate['state'] == state]['cases'])

                casesDeathsData.append(dfLastDate.loc[dfLastDate['state'] == state]['deaths'] - dfNextToLastDate.loc[dfNextToLastDate['state'] == state]['deaths'])

                stateData['state'] = casesDeathsData
                #example: dict(sorted(x.items(), key=lambda item: item[1]))
                sortedStateData = sorted(stateData.items(), key=lambda item: item[1])

        
    def SetupAndRun(self):
        matplotlib.style.use('fivethirtyeight')

        df = self.getCsv()

        lastDate, nextToLastDate = self.extractDatesToUse(df)

        
#        state = self.getState()
        self.iterateUsForStates(df, lastDate, nextToLastDate )
        
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

    def iterateStates(self,df):
        dates = []
        cases = []
        deaths = []

        #theState = df.loc[df['state'] == statename] ## and 'county' == County]

        #self.getAllCounties(theState)
        #self.iterateCounties(theState)


    def getCurrentCases(self, ours):
        currentCases = ours.iloc[-1]['cases'] - ours.iloc[-2]['cases']
        currentDeaths = ours.iloc[-1]['deaths'] - ours.iloc[-2]['deaths']
        ##print(f'cases: {currentCases}')
        return currentCases, currentDeaths

    def dateSubtractOneDay(self, aDate):
        dtm = date.fromisoformat(aDate)
        dtm += timedelta(-1)
        somedate = dtm.isoformat()
        somedate = re.sub('T.*', '', somedate)
        return somedate
    
    def getCasesByDate(self, ours, thedate, cn):
        otherdate = self.dateSubtractOneDay(thedate)

        #print(f'otherdate: {otherdate}')
        #if cn == 'Alpine':
        #    ours.to_csv('alpine.csv')
        #print(ours.tail())

        
        therow = ours.loc[ours['date'] == thedate]
        theOtherRow =  ours.loc[ours['date'] == otherdate]
        
        datecases = therow['cases'].squeeze()
        dateminuscases = theOtherRow['cases'].squeeze()
        
        datedeaths = therow['deaths'].squeeze()
        dateminusdeaths = theOtherRow['deaths'].squeeze()
            
            
        #print(f'datedeaths: {datedeaths}')
        #print(f'dateminusdeaths: {dateminusdeaths}')

        try:
            if datecases - dateminuscases < 0:
                datecases = 0
                dataminuscases = 0
        except ValueError:
            datecases = 0
            dateminuscases = 0
            datedeaths = 0
            dateminusdeaths = 0
            
        #print(ours.loc[ours['date'] == thedate])
        #print(ours.loc[ours['date'] == otherdate])

        
        #print(datecases, ' <-> ', dateminuscases)
        currentCases = datecases - dateminuscases
        currentDeaths = datedeaths - dateminusdeaths
#        currentDeaths = int(currentDeaths)
        
        #currentCases = ours.loc[ours['date'] == thedate]['cases'] - \
              #         ours.loc[ours['date'] == otherdate]['cases']
        #currentDeaths = ours.iloc[-1]['deaths'] - ours.iloc[-2]['deaths']

        #print(f'currentCases = {currentCases}')
        #print(f'currentDeaths = {currentDeaths}')
        
        return currentCases, currentDeaths

    def iterateCounties(self, theState):
        cases = []
        deaths =[]
        for cn in self.counties:
            ours = theState.loc[theState['county'] == cn]
            # current cases at the end

            #print(f'getlastdate: {self.getLastDate()}')
            
            if not self.getLastDate():
                self.date = ours.iloc[-1]['date']
                currentCases, currentDeaths = self.getCurrentCases(ours)

            else:
                self.date = self.getLastDate()
                currentCases, currentDeaths = self.getCasesByDate(ours,
                                                                  self.getLastDate(), cn)
 

            
            #currentCases = ours.iloc[-1]['cases'] - ours.iloc[-2]['cases']
            #currentDeaths = ours.iloc[-1]['deaths'] - ours.iloc[-2]['deaths']
            if currentCases < 0:
                currentCases = 0 
            if currentDeaths < 0:
                currentDeaths = 0

            #self.date = ours.iloc[-1]['date']
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
