## Process nyt data for Washington

import sys
import pandas as pd

from options import Options
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates
import numpy as np
import os
import re
import getopt
from dotenv import load_dotenv
load_dotenv()
import avg
##sys.path.append('/Users/jimt/work/python/pytools')
sys.path.append(os.environ.get("PYTOOLS"))
                

class ourOpts(Options):
    def __init__(self, argv, exename):
        super().__init__(argv, exename)
        self.state = 'NoState'
        self.county = 'NoCounty'
        self.doplot = True # Plot the graph
        self.exename = exename

        try:
            opts, args = getopt.getopt(argv, "hs:c:nd:v")
        except getopt.GetoptError:
            self.printHelpAndExit()

        count = 0
        for opt, arg in opts:
            count += 1

            if opt == '-h':
                self.printHelpAndExit()
            elif opt == '-v':
                print(f'Version {self.getVersion()}')
                sys.exit()
            elif opt in ("-n"):
                self.doplot = False
            elif opt in ("-s"):
                self.state = arg
            elif opt in ('-c'):
                self.county = arg



    def printHelpAndExit(self):
        print(f'usage: {self.exename} [-n  (noplot)] [-s State] [-c County] -v [-d date (2021-03-30)')
        sys.exit('Exiting')

        
        
class countyGraph:
    def __init__(self, argv):
        self.opts = ourOpts(argv, os.path.basename(__file__))
        self.firstDate = '2020-01-01'
        self.lastDate = '2020-01-01'

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


# Tell matplotlib to interpret the x-axis values as dates
###ax.xaxis_date()

# Make space for and rotate the x-axis tick labels
###fig.autofmt_xdate()

    
    def getxdates(self, rawdates):
        xdates = matplotlib.dates.num2date(matplotlib.dates.datestr2num(rawdates))
        # pd.to_datetime(df['TradeDate'], format='%Y%m%d.0')

        #xdates = pd.to_datetime(rawdates, format='%Y%m%d') ##matplotlib.dates.date2num(rawdates)
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
        cases = 0 if cases < 0 else cases
        deaths = small.iloc[1].deaths - small.iloc[0].deaths
        deaths = 0 if deaths < 0 else deaths
        date = small.iloc[0].date
        return 'Cases for   ' + str(date) + ': ' + str(cases) +'\nDeaths for '  +  str(date) + ': ' + str(deaths)
        
    
    def iterateCounty(self, df, statename, County):
        dates = []
        cases = []
        deaths = []

        theState = df.loc[df['state'] == statename] ## and 'county' == County]
        theCounty = theState.loc[theState['county'] == County]

         ## Get first and last dates for graph:
        first = theCounty.iloc[0].date
        last = theCounty.iloc[-1].date
        #print(first, last)
        self.setFirstAndLastDates(first, last)


        
       ## print(theState.head())
        for i, c in theCounty.iterrows():
            cases.append(c['cases'])
            dates.append(c['date'])
            deaths.append(c['deaths'])

        first, last = self.getFirstAndLastDates()
        textstr = f'Graph from {first} to {last}'

        self.plotdeathdiffs(statename, dates, deaths, textstr)
        self.plotcasediffs(statename, dates, cases, textstr)

    def getCsv(self):
        if 'LOCALCSV' in os.environ:
            df = pd.read_csv(os.environ.get('LOCAL_COUNTIES_CSV'))
        else:
            df = pd.read_csv(os.environ.get('NYTIMES_COUNTIES_CSV'))


        return df

        
    def setFirstAndLastDates(self, first, last):
        self.firstDate = first
        self.lastDate = last

    def getFirstAndLastDates(self):
        return self.firstDate, self.lastDate

    def SetupAndRun(self):
        matplotlib.style.use('fivethirtyeight')
        df = self.getCsv()
        ##df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
        #df = pd.read_csv('datasets/us-counties.csv' )
        #print(df.head())
        #print(df.describe())
        #print(df.dtypes)
        

                #### Change statename for another state: 
        statename = self.getState() ##'Washington'
        county = self.getCounty()

        self.iterateCounty(df, statename, county)

            

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


    def scale_y(self, plt):
        ybottom, ytop = plt.ylim()
        #print('CD bottom, top: ', ybottom, ytop)
        ## if ytop > 8000:
        plt.ylim(ybottom, ytop * 0.75) 
        return None


    # Tell matplotlib to interpret the x-axis values as dates


# Make space for and rotate the x-axis tick labels

        
    def plotcasediffs(self, statename, dates, cases, textstr):
        nowdiffs = self.casesdiff(cases)
        average = np.array(self.domap(nowdiffs, 14))
        fig = plt.figure(figsize=(12.0, 9.0))
        ax = fig.add_subplot(111)
        xlabels = self.getxaxislabels(dates)
        ax.bar(xlabels['ticks'], nowdiffs, label='cases by day ' + self.getCountyFixed() + ' county, ' + statename + '\n' + textstr)
        ax.plot(xlabels['ticks'], average, 'r', label='Covid cases in ' + self.getCountyFixed() + ' county, ' + statename + ' - fourteen day running average', linewidth=2.0)
        plt.xticks(xlabels['ticks'], xlabels['labels'], rotation=45)
        ##plt.locator_params(axis='x', nbins=len(xlabels['labels'])/28
        ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(), interval=2))
        ax.xaxis.set_minor_locator(mdates.MonthLocator())
        ax.xaxis_date()
        fig.autofmt_xdate()
        plt.legend()

        self.scale_y(plt)

#        plt.tight_layout()
#        plt.xticks(rotation=45)
        #before showing, save image
        imgname = self.getimagename(statename, dates, 'cases')
        fig.savefig('images/' + imgname, pil_kwargs={}) ###quality=60)
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


    def plotdeathdiffs(self, statename, dates, deaths, textstr):
        nowdiffs = self.deathsdiff(deaths)
        ##print(nowdiffs)
        average = np.array(self.domap(nowdiffs, 14))
        fig = plt.figure(figsize=(12.0, 9.0))
        ax = fig.add_subplot(111)
        xlabels = self.getxaxislabels(dates)
        ax.xaxis.set_major_locator(matplotlib.dates.DayLocator(bymonthday=[1, 15]))
        ax.bar(xlabels['ticks'], nowdiffs, label='deaths per day ' + self.getCountyFixed() + ' county, '+ statename + '\n' + textstr)
        ax.plot(xlabels['ticks'], average, 'r', label='Covid deaths in ' + self.getCountyFixed() + ' county, ' + statename + ' - fourteen day running average', linewidth=2.0)

        # Placement is either high, low or not at all...
       ## plt.text(5, 16, 'OompaLoompa') ##getTodaysInfo())
        
        
        plt.xticks(xlabels['ticks'], xlabels['labels'], rotation=45)
        ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(), interval=2))
        ax.xaxis.set_minor_locator(mdates.MonthLocator())
        #plt.locator_params(axis='x', nbins=len(xlabels['labels'])/28)
        plt.legend()

        self.scale_y(plt)

        plt.tight_layout()
        plt.xticks(rotation=45)
#        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
#        ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
#                verticalalignment='top', bbox=props)
        #before showing, save image
        imgname = self.getimagename(statename, dates, 'deaths')
        fig.savefig('images/' + imgname, pil_kwargs={} ) ##quality=60)
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
