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
        pass

    @staticmethod
    def getLastDate():
        df = pd.read_csv('datasets/us.csv')
        
        date = df.loc[:,'date']
        print(date.iloc[-1])

def main():
    print (os.environ.get('STATFILE_BASE'))
    dt = Statfile.getLastDate()

if __name__ == '__main__':
    main()
