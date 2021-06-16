from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

# convert from datetime to string and save in new columns to be used by hovertool
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

# create column data source which is an internal column parser for bokeh
cds=ColumnDataSource(df)

p=figure(x_axis_type="datetime",plot_height=300, plot_width=1000, title="Motion Graph")
hover=HoverTool(tooltips=[("Start","@Start_string"), ("End","@End_string")])
p.add_tools(hover)

p.yaxis.minor_tick_line_color=None
p.ygrid.grid_line_color=None
p.quad(left="Start",right="End",bottom=0,top=1,color="green",source=cds)


output_file("viewmotion.html")
show(p)

