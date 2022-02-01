## Process nyt data for Washington

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os
import sys
sys.path.append('/Users/jimt/work/python/pytools')
import avg
from options import Options
from dotenv import load_dotenv
load_dotenv()

import getopt
sys.path.append('/users/jimt/work/wrfile')
import writefile as wf

##from: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

class ourOpts(Options):
    def __init__(self, argv, exename):
        super().__init__(argv, exename)
        self.state = 'NoState'
        self.doplot = True # Plot the graph
        self.exename = exename

        try:
            opts, args = getopt.getopt(argv, "hs:nv")
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

    def printHelpAndExit(self):
        print(f'usage: {self.exename} [-n  (noplot)] [-s State] -v)')
        sys.exit('Exiting')



class covGraph:
    def __init__(self, argv):
        self.opts = ourOpts(argv, os.path.basename(__file__))
        self.writer = wf.fWrite('/Users/jimt/work/covid/nyt/html/testfile.txt')   
    def getimagename(self, state, dates, ttype):
        final = state + '_' + ttype + '_' + dates[-1] +'.jpg'
        #print(final)
        return final

    def getState(self):
        return self.opts.getState()

    def doShow(self):
        if(True == self.opts.getDoplot()):
            plt.show()

    def getCsv(self):
        if 'LOCALCSV' in os.environ:
#            df = pd.read_csv('datasets/us-states.csv')
          ##  print(os.environ.get('LOCAL_STATES_CSV'))
            df = pd.read_csv(os.environ.get('LOCAL_STATES_CSV'))
        else:
            #df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
            df = pd.read_csv(os.environ.get('NYTIMES_STATES_CSV'))
        return df
                
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



    def writeAverage(self, CorD: str, statename:str, date , average:float):
        text = f'''
Average {CorD} for {statename} on {date}: {int(average)}
'''
        self.writer.append(text)

        


    def scale_y(self, plt):
        ybottom, ytop = plt.ylim()
        ##print('CD bottom, top: ', ybottom, ytop)
        ## if ytop > 8000:
        plt.ylim(ybottom, ytop * 0.75) 
        return None
        
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

        
    def plotcasediffs(self, statename, dates, cases):
        nowdiffs = self.casesdiff(cases)
        average = np.array(self.domap(nowdiffs, 14))
        fig = plt.figure(figsize=(12.0, 9.0))
        ax = fig.add_subplot(111)
        xlabels = self.getxaxislabels(dates)
        ax.bar(xlabels['ticks'], nowdiffs, label='cases by day ' + statename)
        ax.plot(xlabels['ticks'], average, 'r', label='Covid cases in ' + statename + ' - fourteen day running average',  linewidth=2.0)
        plt.xticks(xlabels['ticks'], xlabels['labels'], rotation=45)
        plt.locator_params(axis='x', nbins=len(xlabels['labels'])/20)
        plt.legend()
        self.scale_y(plt)
        plt.tight_layout()
        plt.xticks(rotation=45)
        #before showing, save image
        imgname = self.getimagename(statename, dates, 'cases')
        fig.savefig('images/' + imgname)
        ## write average cases to file:
        self.writeAverage('Cases', statename, dates[-1], average[-1])
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


    def plotdeathdiffs(self, statename, dates, deaths):
        nowdiffs = self.deathsdiff(deaths)
        average = np.array(self.domap(nowdiffs, 14))
        fig = plt.figure(figsize=(14.0, 9.0))
        ax = fig.add_subplot(111)
        xlabels = self.getxaxislabels(dates)
        ax.bar(xlabels['ticks'], nowdiffs, label='deaths per day ' + statename)
        ax.plot(xlabels['ticks'], average, 'r', label='Covid deaths in ' + statename + ' - fourteen day running average',  linewidth=2.0)
        plt.xticks(xlabels['ticks'], xlabels['labels'], rotation=45)
        plt.locator_params(axis='x', nbins=len(xlabels['labels'])/20)
        plt.legend()
        self.scale_y(plt)
        plt.tight_layout()
        plt.xticks(rotation=45)
        #before showing, save image
        imgname = self.getimagename(statename, dates, 'deaths')
        fig.savefig('images/' + imgname)
        self.writeAverage('Deaths', statename, dates[-1], average[-1])
        self.doShow()
    
    def SetupAndRun(self):
        matplotlib.style.use('fivethirtyeight')
        df = self.getCsv()
        #df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
        #df = pd.read_csv('datasets/us-states.csv' )
        #print(df.head())
        #print(df.describe())
        #print(df.dtypes)
        
        #print(df['state'][3])
        dates = []
        cases = []
        deaths = []
    
        #### Change statename for another state: 
        statename = self.getState() ##'Washington'
            
        for i, j in df.iterrows(): 
            if(j['state'] == statename):
##                print(j['date'], j['cases'], j['deaths'])
                cases.append(j['cases'])
#                print('Date: ', 'date')
                dates.append(j['date'])
                deaths.append(j['deaths'])

        

        self.plotdeathdiffs(statename, dates, deaths)
        self.plotcasediffs(statename, dates, cases)
            


def main(argv):
    dograph = covGraph(argv)
    dograph.SetupAndRun()
    
    
if __name__ == "__main__":
    main(sys.argv[1:])
