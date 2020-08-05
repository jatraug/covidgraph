## List latest for each county in Washington
import numpy as np
import pandas as pd
from pandas import DataFrame
import os
import sys
sys.path.append('/Users/jimt/work/python/pytools')
import matplotlib.pyplot as plt
from options import Options
sys.path.append('/Users/jimt/work/covid/nyt')
import dfparse


class countyList:
    def __init__(self):
        self.list = [{'date': '00-00-00', 'county': 'aaa', 'cases': 0, 'deaths':0}] ## DataFrame(columns = ['date', 'county', 'cases', 'deaths'])
                                            

    def insert(self, line):
        #print(line.date, '  ', line.county, '  ', line.cases, '  ', line.deaths)

        self.list.append({'date':line.date, 'county': line.county, 'cases': line.cases, 'deaths': line.deaths})
            
    def sortkey(self, k):
        return k['date']
        
    def getlist(self):
        #print('sorting')
        ##        df = self.list.sort_values(by=['county'], inplace=False)
        self.list.sort(reverse=True, key=self.sortkey)
        return self.list

    def getLatestDate(self):
        pass
    
class countyInfo:
    def __init__(self):
        pass

    def SetupAndRun(self):
        clist = countyList()

        df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')

        dates = []
        cases = []
        deaths = []

                #### Change statename for another state: 
        statename = self.getState() ##'Washington'

        for i, j in df.iterrows(): 
            if(j['state'] == statename):
                clist.insert(j)
                #print(j['date'],j['cases'], j['deaths'])
                cases.append(j['cases'])
#                print('Date: ', 'date')
                dates.append(j['date'])
                deaths.append(j['deaths'])

        
        theList = clist.getlist()
        #print(theList)

        df = DataFrame(data=theList, columns=['date', 'county', 'cases', 'deaths'])

        self.getcountybydate(df)


        #Get the two top dates from sorted(by date) df:
    def getcountybydate(self, df):
        dparse = dfparse.DfParse()
        df.to_csv('datasets/partcounty.csv')
        for i, j in df.iterrows():
            if(False == dparse.state(j)):
                break
        db = dparse.getDB()
        #for i in db:'
        #    print(i)
        self.printCountyInfo(db)
        self.plotcounties(db)

    def makespace(self, name):
        totalsp = 12
        spaces = '             '
        #print('1:', len(name))
        return(spaces[0: totalsp - len(name)])



    def printCountyInfo(self, db):
        #print('123456789012345678901234567890123456789012345678901234567890')
        print('County        cases         deaths        new cases     new deaths')
        for i in db:
            sp = self.makespace(i['county'])
            print(i['county'], sp, i['cases'], self.makespace(str(i['cases'])), i['deaths'], self.makespace(str(i['deaths'])), i['casediffs'], self.makespace(str(i['casediffs'])), i['deathdiffs'])

    def autolabel(self, rects, ax):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

            
    def plotcounties(self, db):
        counties = []
        cases = []
        deaths = []
        newcases = []
        newdeaths = []
        width = .40
        
        for i in db:
            counties.append(i['county'])
            cases.append(float(i['cases']))
            deaths.append(i['deaths'])
            newcases.append(i['casediffs'])
            newdeaths.append(i['deathdiffs'])
            
        x = np.arange(len(counties))  # the label locations
        fig = plt.figure(figsize=(12.0, 9.0))
        ax = fig.add_subplot(111)
        rects1 = ax.bar(x-width/4, cases, width, label='cases', color='green')
        # rects2 = ax.bar(x-width/4, deaths, width, label='deaths', color='red')
        # rects3 = ax.bar(x-width/4, newcases, width, label='new cases', color='orange')
        #rects4 = ax.bar(x-width/4, newdeaths, width, label='new deaths', color='black')
##        ax.set_xticks(x)
        ax.set_xticklabels(counties)
        plt.xticks(x, rotation=90)

        self.autolabel(rects1, ax)
 #       self.autolabel(rects2, ax)
##        self.autolabel(rects3, ax)
##        self.autolabel(rects4, ax)
        fig.tight_layout()
        plt.show()
        
    def getState(self):
        return 'Washington'

def main(argv):
    cinfo = countyInfo()
    cinfo.SetupAndRun()


    
if __name__ == "__main__":
    main(sys.argv[1:])
