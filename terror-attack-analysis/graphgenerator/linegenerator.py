import plotly as py
import plotly.graph_objs as go

def generate(xData, yData, name, xLabel, yLabel, filename):
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
    link = py.offline.plot(fig, filename=filename)
    return link
