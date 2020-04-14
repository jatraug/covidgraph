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

matplotlib.style.use('fivethirtyeight')

df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv' )
#df = pd.read_csv('datasets/us-states.csv' )
print (df.head())
print (df.describe())
print (df.dtypes)

wash = df['state']
print (wash)

print ('\n\nNow...')

#print(df['state'][3])
dates = []
cases = []
deaths = []

#### Change statename for another state: 
statename  = 'Washington'

for i, j in df.iterrows(): 
    if(j['state'] == statename):
        print(j['date'],j['cases'], j['deaths'])
        cases.append(j['cases'])
        dates.append(j['date'])
        deaths.append(j['deaths'])

        



## now do 5 day average:

def domap(arr):
    Avg = avg.avg(5)
    average = []
    for i in range(0, len(arr)):
#        print("elem: ", arr[i])
        average.append(Avg.addelemandGetaverage(arr[i]))

    return average

def getxdates(rawdates):
    xdates = matplotlib.dates.num2date(matplotlib.dates.datestr2num(dates))
    return xdates

def plotcases(dates, cases):
    average = np.array(domap(cases))
    #print (len(average))

    fig =plt.figure(figsize=(12.0,9.0))
    ax = fig.add_subplot(111)
    ax.plot(getxdates(dates),cases,'b', label = 'Covid cases in ' + statename)

    ax.plot(getxdates(dates),average,'g', label = 'Covid cases in ' + statename + ' - five day running average')
    plt.legend()
    plt.xticks(rotation = 45)
    plt.show()

def plotdeaths(dates, deaths):
    average = np.array(domap(deaths))
    ## plot deaths separately:
    fig =plt.figure(figsize=(12.0,9.0))
    ax = fig.add_subplot(111)
    plt.xticks(rotation = 45)

    ax.plot(getxdates(dates),deaths,'r', label = 'Covid deaths in ' + statename)
    ax.plot(getxdates(dates),average,'g', label = 'Covid deaths in ' + statename + ' - five day running average')
    plt.xticks(rotation = 45)
    plt.legend()
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


def plotdeathdiffs(dates, deaths):
    nowdiffs = deathsdiff(deaths)
    fig =plt.figure(figsize=(12.0,9.0))
    ax = fig.add_subplot(111)
    ax .bar(getxdates(dates),nowdiffs, label = 'deaths differences ' + statename)
    plt.legend()
    plt.xticks(rotation = 45)
    plt.show()


plotcases(dates, cases)
plotdeaths(dates, deaths)        
plotdeathdiffs(dates, deaths)

