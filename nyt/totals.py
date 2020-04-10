## Process nyt data for Washington

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import sklearn
from sklearn.cluster import KMeans

##from: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv' )
#df = pd.read_csv('datasets/us-states.csv' )
print (df.head())
print (df.describe())
print (df.dtypes)

wash = df['state']
print (wash)

print ('\n\nNow...')


class storlast:
    def __init__(self):
        self.date = '2020-01-21'
        self.cases = 0
        self.deaths = 0
        
    def storecases(self, cases):
        self.cases += cases

    def storedeaths(self, deaths):
        self.deaths += deaths

    def getcases(self):
        return self.cases

    def getdeaths(self):
        return self.deaths 
                    


        
def gettotal(olddate, totdeaths, totcases, item):
    totdeaths += item['deaths']
    totcases += item['cases']
    if(item['date'] != olddate):        
        olddate = item['date']
    return olddate, totdeaths, totcases
    



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

        
fig =plt.figure(figsize=(12.0,8.0))
ax = fig.add_subplot(111)
ax.plot(matplotlib.dates.num2date(matplotlib.dates.datestr2num(dates)),cases,'b', label = 'Covid cases in ' + statename)
ax.plot(matplotlib.dates.num2date(matplotlib.dates.datestr2num(dates)),deaths,'r', label = 'Covid deaths in ' + statename)
plt.xticks(rotation = 45)

plt.legend()
plt.show()
        
