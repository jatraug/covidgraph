## Process nyt data for Washington

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import sklearn
from sklearn.cluster import KMeans

import sys
sys.path.append('/Users/jimt/work/python/pytools')
import avg as avg
from options import Options


class countyGraph:
    def __init__(self, argv):
        self.opts = Options(argv)


    def getimagename(self, state, dates, type):
        final = state + '_' + self.getCounty() + '_' + type + '_' + dates[-1] +'.png'
        print(final)
        return final

    def getState(self):
        return self.opts.getState()

    def getCounty(self):
        return self.opts.getCounty()

    def doShow(self):
        if(True == self.opts.getDoplot()):
            plt.show()


    ## now do n day average:

    def domap(self,arr, ndays):
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
    
        for i in range (0, len(dtarr)):
            tickstr = str(dtarr[i].date().__str__() + '\n' + dtarr[i].time().__str__())
        
            #        print(tickstr)
            ticks.append(tickcount)
            tickcount +=1
#            print('tickstr: ', tickstr)
            labels.append (tickstr)
        return({'ticks': ticks, 'labels': labels})

            
    def SetupAndRun(self):
        matplotlib.style.use('fivethirtyeight')
        
        df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv' )
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
        county = self.getCounty()
            
        for i, j in df.iterrows(): 
            if(j['state'] == statename and j['county'] == county):
                print(j['date'],j['cases'], j['deaths'])
                cases.append(j['cases'])
#                print('Date: ', 'date')
                dates.append(j['date'])
                deaths.append(j['deaths'])

        self.plotdeathdiffs(statename, dates, deaths)
        self.plotcasediffs(statename, dates, cases)
            

    def casesdiff(self, arrcases):
        diffs = []
        yestercases = 0
        for tocase in arrcases:
            Ddiffs = (int(tocase - yestercases))
            if(Ddiffs < 0): #Makes up for errors in reporting
                Ddiffs = 0
            diffs.append (Ddiffs)
            yestercases = tocase
            #        print(list(diffs))
        return diffs

        
    def plotcasediffs(self, statename, dates, cases):
        nowdiffs = self.casesdiff(cases)
        average = np.array(self.domap(nowdiffs, 7))
        fig =plt.figure(figsize=(12.0,9.0))
        ax = fig.add_subplot(111)
        xlabels = self.getxaxislabels(dates)
        ax.bar(xlabels['ticks'],nowdiffs, label = 'cases by day ' + statename)
        ax.plot(xlabels['ticks'], average,'g', label = 'Covid cases in ' + self.getCounty() + ' county, ' + statename + ' - seven day running average')
        plt.xticks(xlabels['ticks'],xlabels['labels'][::8], rotation = 45)
        plt.locator_params(axis = 'x', nbins = len(xlabels['labels'])/8)
        plt.legend()
        plt.tight_layout()
        plt.xticks(rotation = 45)
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
            diff =  (todeath - yesterdeaths)
            if(diff < 0): #Makes up for errors in reporting
                diff = 0
            ##print('diff: ', diff)
            diffs.append(diff)
            yesterdeaths = todeath
            #        print(list(diffs))
        return diffs


    def plotdeathdiffs(self, statename, dates, deaths):
        nowdiffs = self.deathsdiff(deaths)
        ##print(nowdiffs)
        average = np.array(self.domap(nowdiffs, 7))
        fig =plt.figure(figsize=(12.0,9.0))
        ax = fig.add_subplot(111)
        xlabels = self.getxaxislabels(dates)
        ax.bar(xlabels['ticks'],nowdiffs, label = 'deaths per day ' + statename)
        ax.plot(xlabels['ticks'], average,'g', label = 'Covid deaths in ' + self.getCounty() + ' county, ' + statename + ' - seven day running average')
        plt.xticks(xlabels['ticks'],xlabels['labels'][::8], rotation = 45)
        plt.locator_params(axis = 'x', nbins = len(xlabels['labels'])/8)
        plt.legend()
        plt.tight_layout()
        plt.xticks(rotation = 45)
        #before showing, save image
        imgname = self.getimagename(statename, dates, 'deathdiffs')
        fig.savefig('images/' + imgname)
        self.doShow()
    


def main(argv):
    dograph = countyGraph(argv)
    dograph.SetupAndRun()


    
if __name__ == "__main__":
    main(sys.argv[1:])
