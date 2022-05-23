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

fig = plt.figure(figsize=(12.0, 9.0))
plt.plot(dates, cases)

#ax = fig.add_subplot(111)
#plt.legend()
plt.xticks(rotation=45)
plt.show()
