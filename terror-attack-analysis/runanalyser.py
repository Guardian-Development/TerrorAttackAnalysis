import sys
from analysis import dateanalyser
from database import dbaccessor

def runDayCount():
    db = dbaccessor.DatabaseAccessor("terrordb", "globalattacks")
    analyser = dateanalyser.DateAnalyser(db)
    count = analyser.getDayCount()
    print(count)
    return

def runMonthCount():
    db = dbaccessor.DatabaseAccessor("terrordb", "globalattacks")
    analyser = dateanalyser.DateAnalyser(db)
    count = analyser.getMonthCount()
    print(count)
    return

def runYearCount():
    db = dbaccessor.DatabaseAccessor("terrordb", "globalattacks")
    analyser = dateanalyser.DateAnalyser(db)
    count = analyser.getYearCount()
    print(count)
    return

if __name__ == '__main__':
    sys.exit(runYearCount())
