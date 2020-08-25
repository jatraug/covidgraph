## US cases and deaths

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os
import sys
sys.path.append('/Users/jimt/work/python/pytools')
import avg
from options import Options

class covGraph:
    def __init__(self, argv):
        self.opts = Options(argv, os.path.basename(__file__))
        
    def getimagename(self, dates, ttype):
        final = 'US'+ '_' + ttype + '_' + dates[-1] +'.png'
        print(final)
        return final

    def getState(self):
        return self.opts.getState()

    def doShow(self):
        if(True == self.opts.getDoplot()):
            plt.show()


    ## now do n day average:

    def domap(self, arr, ndays):
        Avg = avg.avg(ndays)
        average = []
        for ii in arr: ##range(0, len(arr)):
            average.append(Avg.addelemandGetaverage(ii))
            
        return average

    def getxdates(self, rawdates):
        xdates = matplotlib.dates.num2date(matplotlib.dates.datestr2num(rawdates))
        return xdates

    def getxaxislabels(self, datearr):
        tickcount = 0
        ticks = []
        labels = []
        dtarr = self.getxdates(datearr)
    
        for ii in dtarr: ##range(0, len(dtarr)):
            tickstr = str(ii.date().__str__()) ## + '\n' + ii.time().__str__())
        
            #        print(tickstr)
            ticks.append(tickcount)
            tickcount += 1
#            print('tickstr: ', tickstr)
            labels.append(tickstr)
        return({'ticks': ticks, 'labels': labels})

    def plotcases(self, dates, cases):
        average = np.array(self.domap(cases, 5))
        #print (len(average))
        
        fig = plt.figure(figsize=(12.0, 9.0))
        ax = fig.add_subplot(111)
        
        xlabels = self.getxaxislabels(dates)
    
        ax.plot(xlabels['ticks'], cases, 'b', label='Covid cases in US' )
        ax.plot(xlabels['ticks'], average, 'g', label='Covid cases in US' + ' - five day running average')
        plt.xticks(xlabels['ticks'], xlabels['labels'][::8], rotation=30)
        plt.locator_params(axis='x', nbins=len(xlabels['labels'])/8)
        plt.legend()
####        plt.tight_layout()
        plt.xticks(rotation=45)
        #before showing, save image
        imgname = self.getimagename( dates, 'cases')
        fig.savefig('images/' + imgname)
        self.doShow()

    def plotdeaths(self, dates, deaths):
        average = np.array(self.domap(deaths, 5))
        ## plot deaths separately:
        fig = plt.figure(figsize=(12.0, 9.0))
        ax = fig.add_subplot(111)
        plt.xticks(rotation=45)
        xlabels = self.getxaxislabels(dates)
        
        ax.plot(xlabels['ticks'], deaths, 'r', label='Covid deaths in US')
        ax.plot(xlabels['ticks'], average, 'g', label='Covid deaths in US' + ' - five day running average')
        plt.xticks(xlabels['ticks'], xlabels['labels'][::8], rotation=45)
        plt.locator_params(axis='x', nbins=len(xlabels['labels'])/8)
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.xticks(rotation=45)
        #before showing, save image
        imgname = self.getimagename( dates, 'death')
        fig.savefig('images/' + imgname)
        self.doShow()

        ## make a bar chart of diffs of cases by day;
    def casesdiff(self, arrcases):
        diffs = []
        yestercases = 0
        for tocase in arrcases:
            tdiffs = int(tocase - yestercases)
            if tdiffs < 0:
                tdiffs = 0
            diffs.append(tdiffs)
            yestercases = tocase
            #        print(list(diffs))
        return diffs

        
    def plotcasediffs(self, dates, cases):
        nowdiffs = self.casesdiff(cases)
        average = np.array(self.domap(nowdiffs, 7))
        fig = plt.figure(figsize=(12.0, 9.0))
        ax = fig.add_subplot(111)
        xlabels = self.getxaxislabels(dates)
        ax.bar(xlabels['ticks'], nowdiffs, label='cases by day in US' )
        ax.plot(xlabels['ticks'], average, 'g', label='Covid cases in US' + ' - seven day running average')
        plt.xticks(xlabels['ticks'], xlabels['labels'][::8], rotation=45)
        plt.locator_params(axis='x', nbins=len(xlabels['labels'])/8)
        plt.legend()
        plt.tight_layout()
        plt.xticks(rotation=45)
        #before showing, save image
        imgname = self.getimagename( dates, 'casediffs')
        fig.savefig('images/' + imgname)
        self.doShow()

    ## make a bar chart of diffs of deaths by day;
    def deathsdiff(self, arrdeaths):
        diffs = []
        yesterdeaths = 0
        for todeath in arrdeaths:
            tdiffs = int(todeath - yesterdeaths)
            if tdiffs < 0:
                tdiffs = 0
            diffs.append(tdiffs)
            yesterdeaths = todeath
            #        print(list(diffs))
        return diffs


    def plotdeathdiffs(self, dates, deaths):
        nowdiffs = self.deathsdiff(deaths)
        average = np.array(self.domap(nowdiffs, 7))
        fig = plt.figure(figsize=(12.0, 9.0))
        ax = fig.add_subplot(111)
        xlabels = self.getxaxislabels(dates)
        ax.bar(xlabels['ticks'], nowdiffs, label='deaths per day ' )
        ax.plot(xlabels['ticks'], average, 'g', label='Covid deaths in US'   + ' - seven day running average')
        plt.xticks(xlabels['ticks'], xlabels['labels'][::8], rotation=45)
        plt.locator_params(axis='x', nbins=len(xlabels['labels'])/8)
        plt.legend()
        plt.tight_layout()
        plt.xticks(rotation=45)
        #before showing, save image
        imgname = self.getimagename( dates, 'deathdiffs')
        fig.savefig('images/' + imgname)
        self.doShow()
    
    def SetupAndRun(self):
        matplotlib.style.use('fivethirtyeight')

        df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv')
        #df = pd.read_csv('datasets/us-states.csv' )
        print(df.head())
        print(df.describe())
        print(df.dtypes)
        
        #print(df['state'][3])
        dates = []
        cases = []
        deaths = []

        
        #### Change statename for another state: 

            
        for i, j in df.iterrows(): 
            print(j['date'], j['cases'], j['deaths'])
            cases.append(j['cases'])
            #                print('Date: ', 'date')
            dates.append(j['date'])
            deaths.append(j['deaths'])

        
        self.plotcases( dates, cases)
        self.plotdeaths(dates, deaths)        
        self.plotdeathdiffs(dates, deaths)
        self.plotcasediffs( dates, cases)




def main(argv):
    dograph = covGraph(argv)
    dograph.SetupAndRun()
    
    
if __name__ == "__main__":
    main(sys.argv[1:])

