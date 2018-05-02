import plotly.graph_objs as plot
from plotly.offline import init_notebook_mode, iplot
from rink import rink_shape

init_notebook_mode()

layout = plot.Layout(
    shapes=rink_shapes
)

fig = plot.Figure(layout=layout)
iplot(fig)
