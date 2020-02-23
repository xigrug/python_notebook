#https://www.kesci.com/home/workspace/project?tab=public
from plotly.graph_objs import *
import plotly.plotly as py
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
# mapbox_access_token = 'ADD_YOUR_TOKEN_HERE'
mapbox_access_token = 'pk.eyJ1IjoieGlncnVnIiwiYSI6ImNqZm8ycXMxejAwOXYyenM3Z2twOWJvb2EifQ.lSikTXoOmtTjHutewtCe9A'

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df=pd.read_table("allsum-0.5-NaN.csv",sep=',',na_values=[-9999])
print(df.head())

#df['text'] = df['latbin'] + '' + df['lonbin'] + ', ' + df['CCN_1.0_cm3'] +','+ df['SS_1.0_mg']
df=df[df["CCN_1.0_cm3"]<10000]
df=df[df["CCN_1.0_cm3"]>0]
site_lat = df.lat_bin
site_lon = df.lon_bin
locations_name = df['CCN_1.0_cm3']

l0_name = df['SS_1.0_mg']

data = Data([
    Scattermapbox(
        # 绘制散点的经纬度
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=Marker(
            size=20,
            #color=['#00ffee','#eeff00']
            colorscale='YlGnBu'
        ),
        # 散点对应的文本
        text=locations_name,
        customdata=l0_name,
        name='CCN'
    )
])

layout = Layout(
    title='基于mapbox的地图标注',
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        # 地图中心坐标，不要远离绘制的散点坐标
        center=dict(
            lat=32,
            lon=118
        ),
        pitch=0,
        zoom=3
    ),
)

fig = dict(data=data, layout=layout)
app.layout  = html.Div([
    dcc.Graph(id='graph', figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
