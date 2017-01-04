import sys
import plotly as py
import plotly.graph_objs as go
from analysis import dateanalyser
from database import dbaccessor

def generateDayCount():
    db = dbaccessor.DatabaseAccessor("terrordb", "globalattacks")
    analyser = dateanalyser.DateAnalyser(db)
    dayCount = analyser.getDayCount()
    days = range(1, 32)
    barGraphGenerator(
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
    barGraphGenerator(
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
    lineGraphGenerator(
        yearCount.keys(),
        values,
        'Terror Attacks By Year',
        'Year',
        'Terror Attack Count',
        'terror-attack-by-year.html')
    return yearCount

def generateGraphs():
    generateDayCount()
    generateMonthCount()
    generateYearCount()
    return

#helper method to build a bar graph
def barGraphGenerator(xData, yData, orientation, name, xLabel, yLabel, filename):
    data = [go.Bar(x=xData, y=yData, orientation=orientation, name=name)]
    layout = go.Layout(
        title=name,
        xaxis=dict(
            title=xLabel,
        ),
        yaxis=dict(
            title=yLabel,
        )
    )
    fig = go.Figure(data=data, layout=layout)
    py.offline.plot(fig, filename=filename)
    return

def lineGraphGenerator(xData, yData, name, xLabel, yLabel, filename):
    data = [go.Scatter(
        x = xData,
        y = yData,
        name = 'name',
        line = dict(
            color = ('rgb(205, 12, 24)'),
            width = 4)
    )]
    layout = dict(
            title = name,
            xaxis = dict(title = xLabel),
            yaxis = dict(title = yLabel),
        )

    fig = dict(data=data, layout=layout)
    py.offline.plot(fig, filename=filename)

if __name__ == '__main__':
    sys.exit(generateGraphs())
