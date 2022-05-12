"""
million.py - graph the last part of us.csv as it reaches 1 million deaths.
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU
daylist = [MO, TU, WE, TH, FR, SA, SU]
from datetime import datetime


file = '/Users/jimt/work/covid/nyt/datasets/us.csv' ###recdeaths.csv'

df = pd.read_csv(file)

dfSmall = df.iloc[-75:]

def getWeekDay():
    wInd = datetime.today().weekday()
    return daylist[wInd]

print(dfSmall)

dates = dfSmall['date']
deaths = dfSmall['deaths']


fig = plt.figure(figsize=(12.0, 9.0))
ax = fig.add_subplot(111)
plt.xticks(rotation=45)
l2 = plt.plot(dates, deaths)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=getWeekDay()))
##ax.xaxis.set_major_locator(interval=2)
fig.savefig('images/to_a_million')
plt.show()
