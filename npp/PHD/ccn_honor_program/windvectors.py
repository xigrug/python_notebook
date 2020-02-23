# Get this figure: fig = py.get_figure("https://plot.ly/~ToniBois/3421/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~ToniBois/3421/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="wind vectors 1", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~ToniBois/3421/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "line": {"width": 1}, 
  "mode": "lines", 
  "type": "scatter", 
  "x": [34.5, 34.975,]
  "y": [-90.0, -91.447],
  "marker": {
    "size": 1, 
    "color": "rgb(255, 255, 255)"
  }
}
trace2 = {
  "line": {
    "color": "rgb(255, 255, 255)", 
    "shape": "linear", 
    "width": 1.0
  }, 
  "name": "Coast", 
  "type": "scatter", 
  "x": ["0", "0.672866"],
  "y": ["-71.4927", "-71.2167"],
  "connectgaps": False
}
trace3 = {
  "line": {
    "color": "rgb(31, 119, 180)", 
    "width": 0.5
  }, 
  "name": "Rivers", 
  "type": "scatter", 
  "x": ["", ""] 
  "y": ["", ""],
  "visible": True
}
trace4 = {
  "line": {
    "dash": "solid", 
    "color": "rgb(0, 0, 0)", 
    "width": 0.5
  }, 
  "name": "Countries", 
  "type": "scatter", 
  "x": ["Country", "cn"],
  "y": ["City", "shanghai"]
}
trace5 = {
  "uid": "3d7d18", 
  "mode": "markers+text", 
  "name": "Cities", 
  "type": "scatter", 
  "x": ["139.751389", "121.399722"],
  "y": ["35.685", "31.045556"],
  "marker": {
    "size": 2, 
    "color": "rgb(255, 0, 0)"
  }, 
  "text": ["tokyo", "shanghai"],
  "visible": "legendonly", 
  "textfont": {"size": 10}
}
trace6 = {
  "line": {
    "color": "rgb(31, 119, 180)", 
    "width": 0.5
  }, 
  "name": "Rivers2", 
  "type": "scatter", 
  "x": ["", ""],
  "y": ["", ""]
}
trace7 = {
  "name": "Wind Speed (km/h)", 
  "type": "heatmap", 
  "x": [0.0, 1.0],
  "y": [-90.0, -90.0],
  "zmax": 135, 
  "zmin": 0, 
  "z": [15.23, 15.23],
  "zauto": True, 
  "colorscale": [
    [0, "rgb(0,0,131)"], [0.125, "rgb(0,60,170)"], [0.375, "rgb(5,255,255)"], [0.625, "rgb(255,255,0)"], [0.875, "rgb(250,0,0)"], [1, "rgb(128,0,0)], 
    "autocolorscale": False
}
data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7])
layout = {
  "title": "Predicted Surface Wind Speed(km/h) at for 18/05/2018 at 12 UTC (GFS 0.5deg)<br><a href=\"https://sites.google.com/site/meteopina/\">By Meteopina</a>", 
  "width": 1200, 
  "xaxis": {
    "type": "linear", 
    "range": [-180, 180], 
    "ticks": "", 
    "showgrid": False, 
    "zeroline": False, 
    "autorange": True, 
    "showticklabels": False
  }, 
  "yaxis": {
    "type": "linear", 
    "range": [-90, 90], 
    "ticks": "", 
    "showgrid": False, 
    "zeroline": False, 
    "autorange": True, 
    "showticklabels": False
  }, 
  "height": 788, 
  "legend": {
    "x": 0.8610315186246418, 
    "y": 1.1956155143338953
  }, 
  "autosize": True
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)