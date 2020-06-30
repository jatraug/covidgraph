import sys
sys.path.append('/Users/jimt/work/covid/nyt')
import dfparse
import pandas as pd
from pandas import DataFrame

dparse = dfparse.DfParse()


def makespace(name):
    totalsp = 12
    spaces = '             '
    #print('1:', len(name))
    return(spaces[0: totalsp - len(name)])



def printCountyInfo( db):
    print('123456789012345678901234567890123456789012345678901234567890')
    print('County        cases         deaths        new cases     new deaths')
    for i in db:
        sp = makespace(i['county'])
        print(i['county'], sp, i['cases'], makespace(str(i['cases'])), i['deaths'], makespace(str(i['deaths'])), i['casediffs'], makespace(str(i['casediffs'])), i['deathdiffs'])
    


df = pd.read_csv('datasets/partcounty.csv' )

for i, j in df.iterrows():
    if(False == dparse.state(j)):
        break
db = dparse.getDB()
#for i in db:
#    print(i)

printCountyInfo(db)

sp = makespace('qwerty')
print('->', sp, '<--')

