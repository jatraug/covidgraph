import os



# func to make a python buid order
 
def printAndBuildCounty(**kwargs):
    pyfile = 'counties.py'
    state = kwargs['state'].title()
    cnty = kwargs['county'].title()
    cmd = f"python {pyfile} -n -s \'{state}\' -c \'{cnty}\'"
    print(cmd)
    #print(f"os.system(python {pyfile} -n -s \'{state}\' -c \'{cnty}\')")
    os.system(cmd)

    

def printAndBuildState(**kwargs):
    pyfile = 'states.py'
    state = kwargs['state'].title()
    cmd = f"python {pyfile} -n -s \'{state}\'"
    print(cmd)
    os.system(cmd)

# func to make a python buid order
def mkPyBuildOrder(**kwargs):
    cmdarg = f'{kwargs["file"]}'
    if cmdarg == 'states':
        printAndBuildState(**kwargs)
    elif cmdarg == 'counties':
        printAndBuildCounty(**kwargs)
    else:
        raise SomeError
        

#mkPyBuildOrder(file='counties',state='Washington', county='Snohomish')
buildData = [
    {'file': 'counties', 'state': 'Washington', 'county': 'Snohomish'},
    {'file': 'counties', 'state': 'Washingon', 'county': 'Spokane'},
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

 ]



def doBuild():
    for line in buildData:

        ##cmd = f"file = {line['file']}, state = {line['state']}, county = {line['county']}"
        #cmd = f"file=\'{line['file']}\', state=\'{line['state']}\', county=\'{line['county']}\'"
        #print(f'cmd: {cmd}')

       ## mkPyBuildOrder(file='counties', state='Washington', county='Snohomish')
        mkPyBuildOrder(**line)


def main():
    doBuild()

    
if __name__ == '__main__':
    main()
