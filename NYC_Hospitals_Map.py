"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""
import geopandas as gpd
import pandas as pd
import plotly.express as px


csvFile = input("Enter CSV file name: ")
outputFile = input("Enter output file: ")
hospital_df = pd.read_csv(csvFile)
print(hospital_df.columns)

fig = px.scatter_map(hospital_df, lat="Latitude", lon="Longitude", hover_name="Facility Name", title="Facility Type", zoom=10)
fig.show()
fig.write_html(outputFile)
df = pd.read_csv(csvFile)
site_lat = df.lat
site_lon = df.lon
locations_name = df.text

fig = go.Figure()

fig.add_trace(go.Scattermap(
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=go.scattermap.Marker(
            size=17,
            color='rgb(255, 0, 0)',
            opacity=0.7
        ),
        text=locations_name,
        hoverinfo='text'
    ))

fig.add_trace(go.Scattermap(
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=go.scattermap.Marker(
            size=8,
            color='rgb(242, 177, 172)',
            opacity=0.7
        ),
        hoverinfo='none'
    ))

fig.update_layout(
    title=dict(text='NYC Health Facilities'),
    autosize=True,
    hovermode='closest',
    showlegend=False,
    map=dict(
        bearing=0,
        center=dict(
            lat=38,
            lon=-94
        ),
        pitch=0,
        zoom=3,
        style='light'
    ),
)

fig.show()