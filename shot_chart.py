import plotly.graph_objs as pplot
from plotly.offline import init_notebook_mode, plot
from rink import rink_shapes
import plotly.plotly as py


layout = pplot.Layout(
    shapes=rink_shapes
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

fig = pplot.Figure(data=[point_trace], layout=layout)

#py.image.save_as(fig, filename='test.png')

#from IPython.display import Image
#Image('test.png')
plot(fig), #image='png', image_filename='test', output_type='file')
