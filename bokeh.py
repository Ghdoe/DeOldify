#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 00:46:02 2019

@author: jaykim
"""

from bokeh.plotting import figure
from bokeh.io import output_file, show
x = [1, 2, 3, 4, 5]
y = [6, 7, 4, 3, 5]
p = figure(title="simple line example", 
           x_axis_label = 'x', 
           y_axis_label = 'y')

p.line(x, y, legend="temp.", line_width=2)
output_file("lines.html")
show(p)




### Data 

import numpy as np
import pandas as pd
df = pd.DataFrame(np.array([[33.9, 4, 65, 'US'], 
                            [32.4, 4, 66, 'Asia'], 
                            [21.4, 4, 109, 'Europe']]),
                  columns=['mpg', 'cyl', 'hp', 'origin'], 
                  index = ['Toyota', 'Flat', 'Volvo']) 


from bokeh.models import ColumnDataSource
cds_df = ColumnDataSource(df)



from bokeh.plotting import figure
p1 = figure(plot_width=300, tools='pan, box_zoom')
p2 = figure(plot_width=300, plot_height=300, 
            x_range=(0, 8), y_range=(0, 8))

p3 = figure()

p1.circle(np.array([1, 2, 3]), np.array([3, 2, 1]), 
          fill_color='white')

p2.square(np.array([1.5, 3.5, 5.5]), [1, 4, 3], 
          color='blue', size=1)


p1.line([1, 2, 3, 4], [3, 4, 5, 6], line_width=2)
p2.multi_line(pd.DataFrame([[1, 2, 3], [5, 6, 7]]), 
              pd.DataFrame([[3, 4, 5], [3, 2, 1]]), 
              color="blue")




p = figure(tools='box_select')
p.circle('mpg', 'cyl', source=cds_df, 
         selection_color='red',
         nonselection_slpha=0.1)

from bokeh.models import HoverTool
hover = HoverTool(tooltips=None, mode='vline')
p3.add_tools(hover)


from bokeh.models import CategoricalColorMapper
color_mapper = CategoricalColorMapper(
               factors = ['US', 'Asia', 'Europe'],
               palette=['blue', 'red', 'green'])


p3.circle('mpg', 'cyl', source_cds_df, color=dict(filed='origin', 
                                                  transform=color_mapper),
                                           legend='Origin') 




p.legend.location = 'bottom_left'

from bokeh.models import Legend
r1 = p2.asterisk(np.array([1, 2, 3]), np.array([3, 2, 1]))
r2 = p2.line([1, 2, 3, 4], [3, 4, 5, 4])
legend = Legend(items=[("One", [p1, r1]), ("Two", [r2])],
                       location = (0, -30))

p.add_layout(legend, 'right')

p.legend.orientation = "horizontal"
p.legend.orientation = "vertical"

p.legend.border_line_color = "navy"
p.legend.background_fill_color = "white"


from bokeh.layouts import row
layout = row(p1, p2, p3)

from bokeh.layouts import columns
layout = column(p1, p2, p3)

layout = row(column(p1, p2), p3)


from bokeh.layouts import gridplot
row1 = [p1, p2]
row2 = [p3]

layout = gridplot([[p1, p2], [p3]])

from bokeh.models.widgets import Panel, Tabs
tab1 = Panel(child=p1, title="tab1")
tab2 = Panel(child=p2, title="tab2")
layout = Tabs(tabs=[tab1, tab2])


p2.x_range = p1.x_range
p2.y_range = p1.y_range

p4 = figure(plot_width = 100, 
            tools='box_select, lasso_select')

p4.circle('mpg', 'cyl', source=cds_df)

p5 = figure(plot_width = 200, 
            tools='box_select, lasso_select')

p5.circle('mpg', 'hp', source=cds_df)

layout = row(p4, p5) 



from bokeh.io import output_notebook, show
output_notebook()

from bokeh.embed import file_html
from bokeh.resources import CDN

html = file_html(p, CDN, "my_plot")


from bokeh.io import output_file, show
output_file('my_bar_chart.html', mode='cdn')

from bokeh.embed import components 
script, div = components(p)



from bokeh.io import export_png
export_png(p, filename="plot.png")


from bokeh.io import export_svgs
p.output_backend = "svg"
export_svgs(p, filename="plot.svg")
















