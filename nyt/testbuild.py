import os



# func to make a python buid order

def printAndBuildCounty(**kwargs):
    pyfile = 'counties.py'
    state = kwargs['state'].title()
    cnty = kwargs['county'].title()
    cmd = f"python {pyfile} -n -s {state} -c {cnty}"
    print(cmd)
    print(f"os.system(python {pyfile} -n -s \'{state}\' -c \'{cnty}\')")
    os.system(cmd)

    

def printAndBuildState(**kwargs):
    pyfile = 'states.py'
    state = kwargs['state'].title()
    cmd = f"python {pyfile} -n -s {state}"
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
    {'file': 'states', 'state': 'Mississippi'}
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
