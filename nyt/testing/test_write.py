import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.append(os.environ['COVWORK'])

import writefile as wf
from statfile import Statfile as sf


def test_one():

    tname = sf.makeName()
    writer = wf.fWrite()

    writer.write('This Is The First Test of Writer')
    writer.append('This Is second line of The First Test of Writer')


def test_name():
    #nameroot = 'WfTest'

    tname = sf.makeName()
    assert('202' in tname)

def main():
    test_name() # Must be first
    test_one()


if __name__ == '__main__':
    main()
