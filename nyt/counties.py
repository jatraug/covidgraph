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


class countyGraph:
    def __init__(self, argv):
        self.opts = Options(argv, os.path.basename(__file__))


    def getimagename(self, state, dates, mtype):
        final = state + '_' + self.getCountyFixed() + '_' + mtype + '_' + dates[-1] +'.jpg'
        #print(final)
        return final

    def getState(self):
        return self.opts.getState()

    def getCounty(self):
        return self.opts.getCounty()

    # return county with spaces changed to '_':
    def getCountyFixed(self):
        cty = self.opts.getCounty()
        if(re.search(' ', cty)):
            cty = re.sub(' ', '_', cty)
        return cty

    def doShow(self):
        if self.opts.getDoplot():
            plt.show()


    ## now do n day average:

    def domap(self, arr, ndays):
        Avg = avg.avg(ndays)
        average = []
        for i in range(0, len(arr)):
            #        print("elem: ", arr[i])
            average.append(Avg.addelemandGetaverage(arr[i]))
        return average

    def getxdates(self, rawdates):
        xdates = matplotlib.dates.num2date(matplotlib.dates.datestr2num(rawdates))
        return xdates

    def getxaxislabels(self, datearr):
        tickcount = 0
        ticks = []
        labels = []
        dtarr = self.getxdates(datearr)
    
        for i in range(0, len(dtarr)):
            tickstr = str(dtarr[i].date().__str__()) ## + '\n' + dtarr[i].time().__str__())
        
            #        print(tickstr)
            ticks.append(tickcount)
            tickcount += 1
#            print('tickstr: ', tickstr)
            labels.append(tickstr)
        return({'ticks': ticks, 'labels': labels})

    def getTodaysInfo(self, df):
        small = df.tail(2)
        cases = small.iloc[1].cases - small.iloc[0].cases
        cases=0 if cases < 0 else cases
        deaths =  small.iloc[1].deaths - small.iloc[0].deaths
        deaths=0 if deaths < 0 else deaths
        date = small.iloc[0].date
        return '\nCases for   ' + str(date) + ': ' + str(cases) +'\nDeaths for '  +  str(date) + ': ' + str(deaths)
        
    def iterateState(self, df, statename):
        dates = []
        cases = []
        deaths = []

        theState = df.loc[df['state'] == statename]
        for i, c in theCounty.iterrows():
            cases.append(c['cases'])
            dates.append(c['date'])
            deaths.append(c['deaths'])



        

        
    def iterateCounty(self,df, statename, County):
        dates = []
        cases = []
        deaths = []

        theState = df.loc[df['state'] == statename] ## and 'county' == County]
        theCounty = theState.loc[theState['county']==County]

       ## print(theState.head())
        for i, c in theCounty.iterrows():
            cases.append(c['cases'])
            dates.append(c['date'])
            deaths.append(c['deaths'])

        text = self.getTodaysInfo(theCounty)

        
        else:
            self.plotdeathdiffs(statename, dates, deaths, text)
            self.plotcasediffs(statename, dates, cases, text)



    def SetupAndRun(self):
        matplotlib.style.use('fivethirtyeight')
        
        df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
        #df = pd.read_csv('datasets/us-states.csv' )
        #print(df.head())
        #print(df.describe())
        #print(df.dtypes)
        

                #### Change statename for another state: 
        statename = self.getState() ##'Washington'
        county = self.getCounty()

        if(county  == 'NoCounty'):
            self.iterateState(df, statename)
            
        else:
            self.iterateCounty(df,statename, county)

            

    def casesdiff(self, arrcases):
        diffs = []
        yestercases = 0
        for tocase in arrcases:
            Ddiffs = (int(tocase - yestercases))
            if(Ddiffs < 0): #Makes up for errors in reporting
                Ddiffs = 0
            diffs.append(Ddiffs)
            yestercases = tocase
            #        print(list(diffs))
        return diffs

        
    def plotcasediffs(self, statename, dates, cases, textstr):
        nowdiffs = self.casesdiff(cases)
        average = np.array(self.domap(nowdiffs, 7))
        fig = plt.figure(figsize=(12.0, 9.0))
        ax = fig.add_subplot(111)
        xlabels = self.getxaxislabels(dates)
        ax.bar(xlabels['ticks'], nowdiffs, label='cases by day ' + self.getCountyFixed() + ' county, ' + statename + '\n' + textstr)
        ax.plot(xlabels['ticks'], average, 'g', label='Covid cases in ' + self.getCountyFixed() + ' county, ' + statename + ' - seven day running average')
        plt.xticks(xlabels['ticks'], xlabels['labels'][::8], rotation=45)
        plt.locator_params(axis='x', nbins=len(xlabels['labels'])/8)
        plt.legend()
        plt.tight_layout()
        plt.xticks(rotation=45)
        #before showing, save image
        imgname = self.getimagename(statename, dates, 'casediffs')
        fig.savefig('images/' + imgname)
        self.doShow()

    ## make a bar chart of diffs of deaths by day;
    def deathsdiff(self, arrdeaths):
        diffs = []
        yesterdeaths = 0

        for todeath in arrdeaths:
            ##print('yesterdeaths: ', yesterdeaths , 'todeath: ', todeath)
            diff = (todeath - yesterdeaths)
            if(diff < 0): #Makes up for errors in reporting
                diff = 0
            ##print('diff: ', diff)
            diffs.append(diff)
            yesterdeaths = todeath
            #        print(list(diffs))
        return diffs

    def plotStateAlone(self, dates):
        pass
    
    def plotdeathdiffs(self, statename, dates, deaths, textstr):
        nowdiffs = self.deathsdiff(deaths)
        ##print(nowdiffs)
        average = np.array(self.domap(nowdiffs, 7))
        fig = plt.figure(figsize=(12.0, 9.0))
        ax = fig.add_subplot(111)
        xlabels = self.getxaxislabels(dates)
        ax.xaxis.set_major_locator(matplotlib.dates.DayLocator(bymonthday=[1,15]))
        ax.bar(xlabels['ticks'], nowdiffs, label='deaths per day ' + self.getCountyFixed() + ' county, '+ statename + '\n' + textstr)
        ax.plot(xlabels['ticks'], average, 'g', label='Covid deaths in ' + self.getCountyFixed() + ' county, ' + statename + ' - seven day running average')

        
        
        plt.xticks(xlabels['ticks'], xlabels['labels'][::8], rotation=45)
        plt.locator_params(axis='x', nbins=len(xlabels['labels'])/8)
        plt.legend()
        plt.tight_layout()
        plt.xticks(rotation=45)
#        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
#        ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
#                verticalalignment='top', bbox=props)
        #before showing, save image
        imgname = self.getimagename(statename, dates, 'deathdiffs')
        fig.savefig('images/' + imgname)
        self.doShow()
    


def main(argv):
    dograph = countyGraph(argv)
    dograph.SetupAndRun()


    
if __name__ == "__main__":
    main(sys.argv[1:])


#    real	0m6.774s
#user	0m2.789s
#sys	0m0.374s

#Original file:
#real	1m17.102s
#user	1m12.862s
#sys	0m0.450s
