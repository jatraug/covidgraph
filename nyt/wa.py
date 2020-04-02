## Process nyt data for Washington

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import sklearn
from sklearn.cluster import KMeans

##from: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

df = pd.read_csv('datasets/us-states.csv' )
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

for i, j in df.iterrows(): 
    if(j['state'] == 'Washington'):
        print(j['date'],j['cases'], j['deaths'])
        cases.append(j['cases'])
        dates.append(j['date'])
        deaths.append(j['deaths'])

        
fig =plt.figure(figsize=(12.0,8.0))
ax = fig.add_subplot(111)
ax.plot(matplotlib.dates.num2date(matplotlib.dates.datestr2num(dates)),cases,'b')
ax.plot(matplotlib.dates.num2date(matplotlib.dates.datestr2num(dates)),deaths,'b')
plt.xticks(rotation = 45)


plt.show()
        
