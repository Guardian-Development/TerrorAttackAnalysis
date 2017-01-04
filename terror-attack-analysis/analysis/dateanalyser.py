# a statistical look at the dates attacks were commited.
class DateAnalyser(object):

    dbaccessor = None
    
    def getDayCount(self):
        count = [0 for i in range(31)]
        attacks = self.dbaccessor.getAll()

        for attack in attacks:
            #remove 1 for 0 indexing
            day = int(attack["day"])

            #remove those we have no day for
            if(day == 0):
                continue
            # -1 account for 0 indexing
            count[day - 1] += 1

        return count

    def getMonthCount(self):
        count = [0 for i in range(12)]
        attacks = self.dbaccessor.getAll()

        for attack in attacks:
            month = int(attack["month"])

            if(month == 0):
                continue

            count[month - 1] += 1

        return count

    def getYearCount(self):
        count = {}
        attacks = self.dbaccessor.getAll()

        for attack in attacks:
            year = int(attack["year"])

            if(year == 0):
                continue

            #default value 0 if key doesnt exist, else get value of key
            count[year] = count.get(year, 0) + 1
        return count


    def __init__(self, dbaccessor):
        self.dbaccessor = dbaccessor
