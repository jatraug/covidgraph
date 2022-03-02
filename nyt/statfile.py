'''
Write a status file with cases/deaths
'''

import os
from dotenv import load_dotenv
load_dotenv()

import pandas as pd


class Statfile():
    def __init__(self):
        pass

    def makeName(self):
        filename = f'{os.environ["STATFILE_BASE"]}_{Statfile.getLastDate()}.txt'
        return filename

    @staticmethod
    def getLastDate():
        df = pd.read_csv(os.environ['US_CSV'])
        
        date = df.loc[:,'date'].iloc[-1]
        #print(date)
        return date

def main():
    sf = Statfile()
    print(sf.makeName())
    #print (os.environ.get('STATFILE_BASE'))
    dt = Statfile.getLastDate()

if __name__ == '__main__':
    main()
