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

##from: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

        
def getState(argv):
    if(len(argv)!=0) :
        print(argv[0])
        return argv[0]
    return 'Washington' ## defaut


## now do 5 day average:

def domap(arr):
    Avg = avg.avg(5)
    average = []
    for i in range(0, len(arr)):
#        print("elem: ", arr[i])
        average.append(Avg.addelemandGetaverage(arr[i]))

    return average

def getxdates(rawdates):
    xdates = matplotlib.dates.num2date(matplotlib.dates.datestr2num(rawdates))
    return xdates

def getxaxislabels(datearr):
    tickcount = 0
    ticks = []
    labels = []
    dtarr = getxdates(datearr)
    
    for i in range (0, len(dtarr)):
        tickstr = str(dtarr[i].date().__str__() + '\n' + dtarr[i].time().__str__())
        
        print(tickstr)
        ticks.append(tickcount)
        tickcount +=1
        labels.append (tickstr)
    return({'ticks': ticks, 'labels': labels})

def plotcases(statename, dates, cases):
    average = np.array(domap(cases))
    #print (len(average))

    fig =plt.figure(figsize=(12.0,9.0))
    ax = fig.add_subplot(111)

    xlabels = getxaxislabels(dates)
    
    ax.plot(xlabels['ticks'],cases,'b', label = 'Covid cases in ' + statename)
    ax.plot(xlabels['ticks'], average,'g', label = 'Covid cases in ' + statename + ' - five day running average')
    plt.xticks(xlabels['ticks'],xlabels['labels'][::8], rotation = 30)
    plt.locator_params(axis = 'x', nbins = len(xlabels['labels'])/8)
    plt.legend()
    plt.tight_layout()
    plt.xticks(rotation = 45)
    plt.show()

def plotdeaths(statename, dates, deaths):
    average = np.array(domap(deaths))
    ## plot deaths separately:
    fig =plt.figure(figsize=(12.0,9.0))
    ax = fig.add_subplot(111)
    plt.xticks(rotation = 45)
    xlabels = getxaxislabels(dates)
    
    ax.plot(xlabels['ticks'],deaths,'r', label = 'Covid deaths in ' + statename)
    ax.plot(xlabels['ticks'],average,'g', label = 'Covid deaths in ' + statename + ' - five day running average')
    plt.xticks(xlabels['ticks'],xlabels['labels'][::8], rotation = 45)
    plt.locator_params(axis = 'x', nbins = len(xlabels['labels'])/8)
    plt.xticks(rotation = 45)
    plt.legend()
    plt.tight_layout()
    plt.xticks(rotation = 45)
    plt.show()



## make a bar chart of diffs of deaths by day;
def deathsdiff(arrdeaths):
    diffs = []
    yesterdeaths = 0
    for todeath in arrdeaths:
        diffs.append(int(todeath - yesterdeaths))
        yesterdeaths = todeath
        print(list(diffs))
    return diffs


def plotdeathdiffs(statename, dates, deaths):
    nowdiffs = deathsdiff(deaths)
    fig =plt.figure(figsize=(12.0,9.0))
    ax = fig.add_subplot(111)
    xlabels = getxaxislabels(dates)
    ax .bar(xlabels['ticks'],nowdiffs, label = 'deaths differences ' + statename)
    plt.xticks(xlabels['ticks'],xlabels['labels'][::8], rotation = 45)
    plt.locator_params(axis = 'x', nbins = len(xlabels['labels'])/8)
    plt.legend()
    plt.tight_layout()
    plt.xticks(rotation = 45)
    plt.show()


def main(argv):
    
    matplotlib.style.use('fivethirtyeight')

    df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv' )
    #df = pd.read_csv('datasets/us-states.csv' )
    print (df.head())
    print (df.describe())
    print (df.dtypes)

    #print(df['state'][3])
    dates = []
    cases = []
    deaths = []

    #### Change statename for another state: 
    statename  = getState(argv) ##'Washington'

    for i, j in df.iterrows(): 
        if(j['state'] == statename):
            print(j['date'],j['cases'], j['deaths'])
            cases.append(j['cases'])
            dates.append(j['date'])
            deaths.append(j['deaths'])

        
    plotcases(statename, dates, cases)
    plotdeaths(statename,dates, deaths)        
    plotdeathdiffs(statename, dates, deaths)

if __name__ == "__main__":
    main(sys.argv[1:])
