import os



# func to make a python buid order
 
def printAndBuildCounty(**kwargs):
    pyfile = 'counties.py'
    state = kwargs['state'].title()
    cnty = kwargs['county'].title()
    cmd = f"python {pyfile} -n -s \'{state}\' -c \'{cnty}\'"
    print(cmd)
    ##xx = str(input('Hit any key'))
    #print(f"os.system(python {pyfile} -n -s \'{state}\' -c \'{cnty}\')")
    os.system(cmd)

    

def printAndBuildState(**kwargs):
    pyfile = 'states.py'
    state = kwargs['state'].title()
    cmd = f"python {pyfile} -n -s \'{state}\'"
    print(cmd)
    ##xx = str(input('hit any key'))
    os.system(cmd)

def printAndBuildLastday(**kwargs):
    pyfile = 'lastday.py'
    state = kwargs['state'].title()
    cmd = f"python {pyfile} -n -s \'{state}\'"
    print(cmd)
    ##xx = str(input('Hit any key'))
    #print(f"os.system(python {pyfile} -n -s \'{state}\' -c \'{cnty}\')")
    os.system(cmd)    

# func to make a python buid order
def mkPyBuildOrder(**kwargs):
    cmdarg = f'{kwargs["file"]}'
    if cmdarg == 'states':
        printAndBuildState(**kwargs)
    elif cmdarg == 'counties':
        printAndBuildCounty(**kwargs)
    elif cmdarg == 'lastday':
        printAndBuildLastday(**kwargs)

    else:
        raise SomeError
        

#mkPyBuildOrder(file='counties',state='Washington', county='Snohomish')
buildData = [
    {'file': 'counties', 'state': 'Washington', 'county': 'Snohomish'},
    {'file': 'counties', 'state': 'Washington', 'county': 'Spokane'},
    {'file': 'counties', 'state': 'Oregon', 'county': 'Douglas'},
    {'file': 'counties', 'state': 'Oregon', 'county': 'Curry'},
    {'file': 'counties', 'state': 'Oregon', 'county': 'Josephine'},
    {'file': 'counties', 'state': 'Texas', 'county': 'Harris'},
    {'file': 'counties', 'state': 'California', 'county': 'Los Angeles'},
    {'file': 'counties', 'state': 'South Carolina', 'county': 'Charleston'},

    {'file': 'states', 'state': 'Mississippi'},
    {'file': 'states', 'state': 'california'},
    {'file': 'states', 'state': 'oregon'},
    {'file': 'states', 'state': 'idaho'},
    {'file': 'states', 'state': 'florida'},
    {'file': 'states', 'state': 'new york'},
    {'file': 'states', 'state': 'washington'},
    {'file': 'states', 'state': 'ohio'},
    {'file': 'states', 'state': 'missouri'},
    {'file': 'states', 'state': 'minnesota'},
    {'file': 'states', 'state': 'wisconsin'},
    {'file': 'states', 'state': 'new jersey'},
    {'file': 'states', 'state': 'south carolina'},
    {'file': 'states', 'state': 'arizona'},
    {'file': 'states', 'state': 'alaska'},
    {'file': 'states', 'state': 'illinois'},
    {'file': 'states', 'state': 'Massachusetts'},
    {'file': 'states', 'state': 'Texas'},

    
    {'file': 'lastday', 'state': 'illinois'},
    {'file': 'lastday', 'state': 'oregon'},
    {'file': 'lastday', 'state': 'new jersey'},
    {'file': 'lastday', 'state': 'california'},
    {'file': 'lastday', 'state': 'south carolina'},
    {'file': 'lastday', 'state': 'idaho'},
    {'file': 'lastday', 'state': 'washington'},

 ]



def doBuild():
    for line in buildData:
        mkPyBuildOrder(**line)
    # One more straggler:
    print('os.system("python us.py -n")')
    os.system("python us.py -n")

def main():
    doBuild()

    
if __name__ == '__main__':
    main()
