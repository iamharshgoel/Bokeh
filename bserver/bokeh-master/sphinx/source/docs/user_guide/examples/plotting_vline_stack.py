from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show

output_file("vline_stack.html")

source = ColumnDataSource(data=dict(
    x=[1, 2, 3, 4, 5],
    y1=[1, 2, 4, 3, 4],
    y2=[1, 4, 2, 2, 3],
))
p = figure(plot_width=400, plot_height=400)

p.vline_stack(['y1', 'y2'], x='x', source=source)

show(p)
