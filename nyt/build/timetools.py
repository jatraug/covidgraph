from datetime import datetime, timedelta
import re
import time


def day_of_week():
    t = time.localtime().tm_wday
    return t

def is_weekend():
    dow = day_of_week()
    if dow == 5 or dow == 6: ## Sat. or Sun.
        return True
    return False

def early_date(endtime, daysbefore):
    """
starting with the end date(endtime), calculate and retun the start date daysbefore days before(pant, pant!)
    input: 
       -endtime - the end date of the series that we're finding the start date for.
       -daysbefore in days ( negative days to find the start date
      from the end date
    """
    new_final_time = endtime + timedelta(days = daysbefore)
    rx = re.compile('\d{4}-\d{2}-\d{2}')
    matchobj = re.search(rx, str(new_final_time))

    if (matchobj):
        ##print(matchobj[0])
        return matchobj[0]
    return None





def testit():
    edate = early_date(datetime.fromisoformat('2021-09-24'), int(-84))
    print(edate)
    assert edate == '2021-07-02'

    ## Thelast test. If this is a weekend, expoec the test to pass.
    ###  Othersise it'll fail!
    assert is_weekend() == True
    


if __name__ == '__main__':
    testit()
