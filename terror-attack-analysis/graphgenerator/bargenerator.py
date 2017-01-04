import plotly as py
import plotly.graph_objs as go

def generate(xData, yData, orientation, name, xLabel, yLabel, filename):
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
    link = py.offline.plot(fig, filename=filename)
    return link
