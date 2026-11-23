"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""

import pandas as pd
import plotly.express as px


csvFile = input("Enter CSV file name: ")
bedrooms = int(input("Enter number of bedrooms (0 for studio, 1 for one bedroom,...): "))
outputFile = input("Enter output file: ")

housing_df = pd.read_csv(csvFile)
bedroom_cols = {0: "Studio Units", 1: "1-BR Units", 2: "2-BR Units", 3: "3-BR Units", 4: "4-BR Units", 5: "5-BR Units", 6: "6-BR+ Units"}
col = bedroom_cols.get(bedrooms, f"{bedrooms}-BR Units")

housing_df = housing_df[housing_df["Project Name"] != "Confidential"]
df = housing_df[housing_df[col].notnull() & (housing_df[col] > 0)]

fig = px.scatter_map(df, lat="Latitude", lon="Longitude", size=col, hover_name="Project Name", title=f"Housing: {col}", zoom=10)

fig.write_html(outputFile)
fig.show