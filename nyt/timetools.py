from datetime import datetime, timedelta
import re

def early_date(beforetime):
    ini_time_for_now = datetime.now()
    new_final_time = ini_time_for_now + timedelta(days = beforetime)
    rx = re.compile('\d{4}-\d{2}-\d{2}')
    matchobj = re.search(rx, wholetime)

    if (matchobj):
        print(matchobj[0])
   ## print ("new_final_time", str(new_final_time))





def testit():
    early_date(int(-84))


if __name__ == '__main__':
    testit()
