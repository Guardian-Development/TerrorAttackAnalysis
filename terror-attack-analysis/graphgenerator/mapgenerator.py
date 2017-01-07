import plotly as py
import plotly.graph_objs as go

def generate(locationData, name, year, filename):
    attacks = []
    scale = 5

    #max amount to display on the graph
    locationsToDisplay = 50000
    count = 0;

    for locationAttack in locationData:
        if(year > 0 and int(locationAttack['year']) != year):
            continue
        if(locationAttack['kills'] == 0):
            continue
        count += 1
        attack = dict(
            type = 'scattergeo',
            lon = [locationAttack['longitude']],
            lat = [locationAttack['latitude']],
            text = 'City: {0} - Kills: {1}'.format(locationAttack['city'],locationAttack['kills']),
            marker = dict(
                size = locationAttack['kills']/2,
                color = getRGBFromString(locationAttack['region']),
                line = dict(width=0.5, color='rgb(40,40,40)'),
                sizemode = 'markers',
                opacity = getOpacityFromSize(locationAttack['kills'])
            ),
            name = 'City: {0} - Kills: {1}'.format(locationAttack['city'],locationAttack['kills']))
        attacks.append(attack)

        if(count > locationsToDisplay):
            break

    layout = dict(
        title = name,
        showlegend = False,
        geo = dict(
            showland = False,
            landcolor = 'rgb(217, 217, 217)',
            subunitwidth=1,
            countrywidth=1,
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)"
        ),
    )

    print('generating graph...')
    fig = dict(data=attacks, layout=layout)
    link = py.offline.plot(fig, filename=filename)
    return link

def getOpacityFromSize(size):
    value = 0.7 - float(float(size) / float(100))
    if(value < 0):
        return 0.1;
    return value

def getRGBFromString(string):
    hashvalue = str(abs(hash(string)))
    return "rbg({0},{1},{2}".format(hashvalue[:3], hashvalue[3:6], hashvalue[6:9])
