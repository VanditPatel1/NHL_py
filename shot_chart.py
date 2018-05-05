import plotly.graph_objs as pplot
from plotly.offline import init_notebook_mode, plot
from rink import rink_shapes
import plotly.plotly as py
from database_connect import db_connect
import pandas as pd


db = db_connect()

id = db.get_player_id(full='Alex Ovechkin')[0][0]

all_shots = db.get_shots(id=id)


all_shots['x'] = all_shots['x'].apply(lambda x: x*5.7)
all_shots['y'] = all_shots['y'].apply(lambda y: y*5.7)

# Flip axis
for i, r in all_shots.iterrows():
    if all_shots.loc[i, 'x'] < 0:
        all_shots.loc[i, 'x'] *= -1
        all_shots.loc[i, 'y'] *= -1


goals = all_shots
no_goals = all_shots

#no_goals = no_goals[no_goals.x < 0]
#print (no_goals.period)

goals = goals[goals.goal == True]

no_goals = no_goals[no_goals.goal == False]

layout = pplot.Layout(
    shapes=rink_shapes
)


missed_shots = pplot.Scatter(
    x = no_goals['y'],
    y = no_goals['x'],
    name = 'Saved Shots',
    mode = 'markers',
    marker = dict(
        size=4,
        color='rgba(255, 25, 25, 1)'
    )
)

made_shots = pplot.Scatter(
    x = goals['y'],
    y = goals['x'],
    name = 'Goals',
    mode = 'markers',
    marker = dict(
        size=4,
        color='rgba(25, 255, 25, 1)'
    )
)

fig = pplot.Figure(data=[missed_shots, made_shots], layout=layout)

#py.image.save_as(fig, filename='test.png')

#from IPython.display import Image
#Image('test.png')
plot(fig), #image='png', image_filename='test', output_type='file')
