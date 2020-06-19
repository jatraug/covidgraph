import sys
sys.path.append('/Users/jimt/work/covid/nyt')
import dfparse
import pandas as pd
from pandas import DataFrame

dparse = dfparse.DfParse()

df = pd.read_csv('datasets/partcounty.csv' )

for i, j in df.iterrows():
    if(False == dparse.state(j)):
        break
db = dparse.getDB()
for i in db:
    print(i)



