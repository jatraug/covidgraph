

class DfParse:
    def __init__(self):
        self.dbase = []
        self.date = '00-00-00'
        self.date2 = '00-00-00'
        self.state = self.state1
        
    def state1(self, line):
        self.date = line['date']
        self.dbase.append({'county': line['county'], 'cases': line['cases'], 'deaths': line['deaths']})
        self.state = self.state2
        return True
 
    def state2(self, line):
        if(self.date == line['date']):
            self.dbase.append({'county': line['county'], 'cases': line['cases'], 'deaths': line['deaths']})
        else:
            self.date2 = line['date']
            self.getdiffs(line)
            self.state = self.state3
            return True

    def state3(self, line):
        if(self.date2 == line['date']):
            self.getdiffs(line)
        else:
            return False
            

    def getdiffs(self, line):
        db = self.dbase
        for i in db:
            if(i['county'] == line['county']):
                i['casediffs'] = i['cases'] - line['cases']
                i['deathdiffs'] = i['deaths'] - line['deaths']
                if(i['casediffs'] < 0):
                    i['casediffs'] = 0
                if(i['deathdiffs'] < 0):
                    i['deathdiffs'] = 0
                 
    def getDB(self):
        return self.dbase
        
