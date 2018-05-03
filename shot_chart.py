import plotly.graph_objs as pplot
from plotly.offline import init_notebook_mode, plot
from rink import rink_shape


layout = pplot.Layout(
    shapes=rink_shape
)

xx = [1, 2, 3]
yy = [5, 10, 15]

point_trace = pplot.Scatter(
    x = xx,
    y = yy,
    mode = 'markers',
    marker = dict(
        size = 4
    )
)

fig = pplot.Figure(data=point_trace, layout=layout)

plot(fig)
