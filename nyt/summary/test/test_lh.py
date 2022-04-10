import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.append(f"{os.environ['COVWORK']}/summary")

import linehelp as lh


def test_one():
    cl = lh.LineHelper()
    cl.runner()

def test_space():
    sp = lh.strOfSpaces(5)
    assert sp == '     '
    assert lh.strOfSpaces(26, ch='s') == 'ssssssssssssssssssssssssss'

def test_max():
    aa = [
        'one two theree, four',
        'five, six, seven. eight',
        'nine, ten, eleven, twelve',
        ]

        
    cl = lh.LineHelper()
    assert cl.maxChars(aa) == 25
