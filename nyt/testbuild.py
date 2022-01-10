import os



# func to make a python buid order
def WWXXmkPyBuildOrder(**kwargs):
    pyfile = f'{kwargs["file"]}.py'
    state = kwargs['state'].title()
    cnty = kwargs['county'].title()
    cmd = f"python {pyfile} -n -s {state} -c {cnty}"
    print(cmd)
    print(f"os.system(python {pyfile} -n -s \'{state}\' -c \'{cnty}\')")
  ##  os.system(cmd)

def printAndBuildCounty(**kwargs):
    pyfile = 'counties.py'
    state = kwargs['state'].title()
    cnty = kwargs['county'].title()
    cmd = f"python {pyfile} -n -s {state} -c {cnty}"
    print(cmd)
    print(f"os.system(python {pyfile} -n -s \'{state}\' -c \'{cnty}\')")
   # os.system(cmd)

    

def printAndBuildState(**kwargs):
    pyfile = 'states.py'
    state = kwargs['state'].title()
    cmd = f"python {pyfile} -n -s {state}"
    print(cmd)
##    os.system(cmd)

# func to make a python buid order
def mkPyBuildOrder(*args, **kwargs):
    cmdarg = f'{kwargs["file"]}'
    if cmdarg == 'states':
        printAndBuildState(**kwargs)
    elif cmdarg == 'counties':
        printAndBuildCounty(**kwargs)
    else:
        raise SomeError
        

#mkPyBuildOrder(file='counties',state='Washington', county='Snohomish')
buildData = [
    {'file': 'counties', 'state': 'Washington', 'county': 'Snohomish'}
 ]

def doBuild():
    for line in buildData:

        ##cmd = f"file = {line['file']}, state = {line['state']}, county = {line['county']}"
        cmd = f"file=\'{line['file']}\', state=\'{line['state']}\', county=\'{line['county']}\'"
        print(f'cmd: {cmd}')
        mkPyBuildOrder(file='counties', state='Washington', county='Snohomish')
        mkPyBuildOrder(cmd)


def main():
    doBuild()

    
if __name__ == '__main__':
    main()
