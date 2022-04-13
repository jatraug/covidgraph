import re

## Assumptions
## Lines are always in this order:
"""
"Average Deaths for Los_Angeles county, California on 2022-03-28: 21",
"Average Cases for Los_Angeles county, California on 2022-03-28: 1243",
i.e. Deaths bedore Cases (and Cases always immediately following Deaths)
"""
## we'll make lines like this:
"""
Average Cases/Deaths  for Los_Angeles county, California on 2022-03-30: :  1237   20
"""


class LineHelper():
    def __init__(self):
        self.lDict = {}
        self.linemax = 0
        self.linedictarr = []
        self.linedict = {}
        self.line0 = "\nAverage Cases/Deaths"
        self.line1 = ''
        self.cases = ''
        self.deaths = ''
        ## Constants!!
        self.MAXLEN = 80
        self.TOPTEXT = 'Cases     Deaths'

    def maxChars(self, lines):
        newlist = []
        for line in lines:
            #print(f'==>{len(line)}')
            newlist.append(len(line))
        #print(newlist)
        self.linemax = max(newlist)
        #print(f'linemax: {self.linemax}')
        return self.linemax


    def changeLine(self, line):
        #print(line)
        ##exp = re.compile('(.* on /n{4}-\n{2}-\n{2}\:)\s+(\n+)') ## ([{Cases|Deaths}])
        retval = ''
        exp = re.compile(r'A.*\s(Cases|Deaths)(.* on\s+\d{4}-\d{2}-\d{2}\:\s+)(\d+)') ## ([{Cases|Deaths}])
        matchObj = re.search(exp, line)
        spc = '          '
        if matchObj:
            #[print(m) for m in matchObj]
            #print(matchObj.groups())
            grp = matchObj.groups()
            #print(f'0: {grp[0]}')
            self.line1 = grp[1]
            if grp[0]== 'Deaths':
                self.deaths = grp[2]
            elif grp[0] == 'Cases':
                self.cases = grp[2]
                retval = self.mkoutputLine()
                self.emptyGroups()
                return retval
            
            else:
                assert False
                




    
    def emptyGroups(self):
        self.cases = ''
        self.deaths = ''
        self.line1  = ''

    def mkoutputLine(self):
        line = f'{self.line0} {self.line1}'
        line += strOfSpaces(self.linemax - len(line) + 6+ 5 - len(self.cases))
        line += f'{self.cases}' ##
        line += strOfSpaces(8 - len(str(self.deaths)))
        line += f'{self.deaths}\n'
##  {self.cases}   {self.deaths}\n'
        return line


    def mkTopLine(self):
        length = self.linemax + 6
        topline = strOfSpaces(length)
        ##line = mkTopLine(self.linemax - len(self.toptext))
        print(f'<pre>{topline}{self.TOPTEXT}')

    def runner(self):
        """
        First read the file
        """
        with open('/Users/jimt/work/covid/nyt/html/Covid_Status_2022-04-11.txt', 'r') as fs:
            self.lines = fs.read().split('\n')

        print(self.maxChars(self.lines))
        self.mkTopLine(self.linemax + 6) ## len(self.TOPTEXT))



        for line in self.lines:
            self.changeLine(line)

###=============== End of Class =======================

def strOfSpaces(count, ch = ' '):
    return (ch * count)


## Testing ###
def main():
    cl = LineHelper()
    cl.runner()
    aa = [
        'one two three, four',
        'five six seven eight',
        'nine, ten, eleven, twelve',
    ]


    cl = LineHelper()
    print(cl.maxChars(aa))

if __name__ == '__main__':
    main()
