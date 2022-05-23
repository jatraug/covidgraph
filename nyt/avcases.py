import re
import matplotlib.pyplot as plt
'''
## typical line:
## Covid_Status_2022-03-11.txt:Average Cases for Washington on 2022-03-11: 1448

##  matchObj = re.search(rx, arr[i])
#       if (matchObj):
#            return i
### grep Washington Co* | sort > avcases.txt

Copied from avcases.ipynb


'''
file = '/Users/jimt/work/covid/nyt/html/avcases.txt'

with open(file, 'r') as av:
    lines = av.read().split('\n')



dates = []
cases = []
rgx = re.compile(r'.*Average Cases for.*on (\d\d\d\d-\d\d-\d\d).*(\d{4})$')
for line in lines:
    #print(line)
    matchObj = re.search(rgx, line)
    if (matchObj):
        #print(f'{matchObj[1]} { matchObj[2]}')
        dates.append(matchObj[1])
        cases.append(matchObj[2])

fig = plt.figure(figsize=(11.0, 8.5))
ax = plt.gca()
#ax.set_xlim([xmin, xmax])
#ax.set_ybound(lower=500.0)
#foo, ax = plt.subplots()
plt.ylabel('Average Covid cases')
plt.xlabel('Date')
plt.locator_params(axis='x', nbins=15)
plotlbl='Washington Covid cases 14-day average'
plt.plot(dates, cases, label=plotlbl)
plt.legend()
#ax.xaxis_date()
fig.autofmt_xdate()
plt.xticks(rotation=45)
plt.show()
