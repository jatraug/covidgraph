

class DfParse:
    def __init__():
        self.dbase =[]
        self.date = '00-00-00'
        self.date2 = '00-00-00'
        self.state = state1
        
    def state1(self, line):
        self.date = line['date']
        self.dbase.append({'county': line['county'], 'cases': line['cases'], 'deaths': line['deaths']})
        self.state = self.state2
 
    def state2(self, line):
        if(self.date == line['date']):
            self.dbase.append({'county': line['county'], 'cases': line['cases'], 'deaths': line['deaths']})
        else:
            self.date2 = line['date']
            self.getdiffs(line)
            self.state = state3

    def state3(self, line):
        if(self.date2 == line['date']):
            self.getdiffs(line)
            

    def getdiffs(self, line):
        db = self.dbase
        for i in db:
            if(i{'state'} == line['state']):
                i{'casediffs'} = line['cases'] - i{'cases'}
                i{'deathdiffs'} = line['deaths'] - i{'deaths'}
                 
        
        
