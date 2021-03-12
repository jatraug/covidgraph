#!/usr/bin/env python
# coding: utf-8

# 
# 

# # Counties - iterate state data and learn counties
# 

# In[36]:


import pandas as pd
import numpy as np


# In[37]:


##df = pd.read_csv('~/work/covid/nyt/datasets/us-counties.csv')
df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')


# In[38]:


theState = df.loc[df['state'] == 'Washington'] ## and 'county' == County]


# In[39]:


theCounty = theState.loc[theState['county']== 'Snohomish']


# In[40]:


## Return a lisist of counties in th state:
def arrCounty(theState):
    dictcounty = {}
    for i, c in theState.iterrows():
        county = c['county']
        try:
            dictcounty[county] += 1
        except KeyError:
            dictcounty[county] = 1
            
    return(np.sort(list(dictcounty.keys())))

#print(arrCounty(theState))


# In[52]:


def getCases(theState):
    cases = {}
    deaths = {}
    ratio = {}
    
    for county in arrCounty(theState):
        print(county, end=', ')
        for i, c in theState.iterrows():
            if c['county'] == county:
              date = c['date']
              try:
                  cases[date] += c['cases']
              except KeyError:
                  cases[date] = 0
                  cases[date] += c['cases'] 
              finally:
                    pass
              try:
                  deaths[date] += c['deaths']
              except KeyError:
                  deaths[date] = c['deaths']

                  
                    
    for date in np.sort(list(cases.keys())):
        print(date, ': ',cases[date], '   ', deaths[date], '  ', deaths[date]/cases[date])
    ##print('Cases: ', cases) 
    
    return cases, deaths


# In[ ]:





# In[53]:


import matplotlib.pyplot as plt
#plot deaths/cases ratio:
def plotRatio(theState):
    dates = []
    ratio = []
    cases, deaths = getCases(theState)
    for date in np.sort(list(cases.keys())):
        dates.append(date)
        ratio.append(deaths[date]/cases[date])
    plt.plot(dates, ratio)


# In[54]:


plotRatio(theState)


# In[55]:


plt.show()


# In[ ]:




