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


def readfile(file):

    with open(file, 'r') as av:
        lines = av.read().split('\n')
    return lines

def getDatesAndCases(lines):
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
            #print(f'{matchObj[1]}  -  {matchObj[2]}')   

    return dates,cases

def plotCases(dates, cases):
    fig = plt.figure(figsize=(11.0, 8.5))
    ax = plt.gca()
    #ax.set_xlim([xmin, xmax])
    #ax.set_ybound(lower=500.0)
    #foo, ax = plt.subplots()
    plt.ylabel('Average Covid cases')
    plt.xlabel('Date')
    ax.locator_params(axis='x', nbins=5)
    ##ax.locator_params(axis='y', nbins=10)
    plotlbl='Washington Covid cases 14-day average'
    plt.plot(dates, cases, 'bo-', label=plotlbl)
    plt.legend()
    #ax.xaxis_date()
    
    xticks = ax.get_xticks()
    ax.set_xticks(xticks[::len(xticks) //10]) # set new tick positions
    ax.tick_params(axis='x', rotation=30) # set tick rotation
    ax.margins(x=0) # set tight margins

    imgname='washavgcases.jpg'
    fig.savefig('images/' + imgname)

    #fig.autofmt_xdate()
    #plt.xticks(rotation=45)
    plt.show()



def main():
    lines = readfile(file)
    dates, cases = getDatesAndCases(lines)
    plotCases(dates, cases)


if __name__ == '__main__':
    main()
