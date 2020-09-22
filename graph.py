from motion import df
from bokeh.plotting import figure, show, output_file

p=figure(x_axis_type="datetime", height=100, width=500, title="Motion Graph")
q=p.quad(left=df["start"], right=df["end"], top=1, bottom=0, color="green")

output_file("Graph.html")
show(p)
