import sys
from graphgenerator import bargenerator as gb
from graphgenerator import linegenerator as gl
from graphgenerator import mapgenerator as gm
from analysis import dateanalyser
from analysis import targetanalyser
from database import dbaccessor

def generateDayCount():
    db = dbaccessor.DatabaseAccessor("terrordb", "globalattacks")
    analyser = dateanalyser.DateAnalyser(db)
    dayCount = analyser.getDayCount()
    days = range(1, 32)
    gb.generate(
        days,
        dayCount,
        'v',
        'Terror Attack By Days of the Week',
        'Days',
        'Terror Attack Count',
        'terror-attack-by-days.html'
    )
    return dayCount

def generateMonthCount():
    db = dbaccessor.DatabaseAccessor("terrordb", "globalattacks")
    analyser = dateanalyser.DateAnalyser(db)
    monthCount = analyser.getMonthCount()
    months = [
        'January',
        'Febuary',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    gb.generate(
        months,
        monthCount,
        'v',
        'Terror Attacks By Months of the Year',
        'Months',
        'Terror Attack Count',
        'terror-attack-by-months.html'
    )
    return monthCount

def generateYearCount():
    db = dbaccessor.DatabaseAccessor("terrordb", "globalattacks")
    analyser = dateanalyser.DateAnalyser(db)
    yearCount = analyser.getYearCount()
    values = [value for key, value in yearCount.items()]
    gl.generate(
        yearCount.keys(),
        values,
        'Terror Attacks By Year',
        'Year',
        'Terror Attack Count',
        'terror-attack-by-year.html')
    return yearCount

def generateKillsWithWeaponByRegionAndYear():
    db = dbaccessor.DatabaseAccessor("terrordb", "globalattacks")
    analyser = targetanalyser.TargetAnalyser(db)
    regionKills = analyser.getLocationWithKills()
    gm.generate(
        regionKills,
        'Deaths by Location for Attacks',
        'terror-attack-weapon-kills-region.html')
    return

def generateGraphs():
    #generateDayCount()
    #generateMonthCount()
    #generateYearCount()
    generateKillsWithWeaponByRegionAndYear()
    return

if __name__ == '__main__':
    sys.exit(generateGraphs())
