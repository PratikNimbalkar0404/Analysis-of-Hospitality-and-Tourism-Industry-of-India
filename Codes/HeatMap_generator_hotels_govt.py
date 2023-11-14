import pandas as pd
import geopandas as gpd
import folium
import geocoder  
from folium.plugins import HeatMap
from time import sleep

# Load the Excel file with hotel data into a DataFrame
df = pd.read_excel('../Datasets/2016_final.xlsx')

city_counts = df['City'].value_counts()

locations=[]
for x in city_counts.keys():
    g = geocoder.bing(x, key='AsGXdjL7aL-H4vZdjl5m7BnlELyKTMi4_-CFrr7W4s4LQAkIWmkLZaO6cAD4iqAh')
    results = g.json
    if(results==None):
        break
    # print(results['lat'], results['lng'])
    locations.append((x,results['lat'], results['lng']))
    


m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Create a heatmap using the hotel counts
heat_data = [(row[1], row[2], int(city_counts[row[0]])) for row in locations]
HeatMap(heat_data, radius=15).add_to(m)

# Save the map to an HTML file or display it
m.save('heatmap_2016_mmt.html')

df = pd.read_excel('../Datasets/2017_final.xlsx')

city_counts = df['City'].value_counts()

locations=[]
for x in city_counts.keys():
    g = geocoder.bing(x, key='AsGXdjL7aL-H4vZdjl5m7BnlELyKTMi4_-CFrr7W4s4LQAkIWmkLZaO6cAD4iqAh')
    results = g.json
    if(results==None):
        break
    # print(results['lat'], results['lng'])
    locations.append((x,results['lat'], results['lng']))
    

m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Create a heatmap using the hotel counts
heat_data = [(row[1], row[2], int(city_counts[row[0]])) for row in locations]
HeatMap(heat_data, radius=15).add_to(m)

# Save the map to an HTML file or display it
m.save('heatmap_2017_mmt.html')




df = pd.read_excel('../Datasets/2018_final.xlsx')

city_counts = df['City'].value_counts()

locations=[]
for x in city_counts.keys():
    g = geocoder.bing(x, key='AsGXdjL7aL-H4vZdjl5m7BnlELyKTMi4_-CFrr7W4s4LQAkIWmkLZaO6cAD4iqAh')
    results = g.json
    if(results==None):
        break
    # print(results['lat'], results['lng'])
    locations.append((x,results['lat'], results['lng']))

m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Create a heatmap using the hotel counts
heat_data = [(row[1], row[2], int(city_counts[row[0]])) for row in locations]
HeatMap(heat_data, radius=15).add_to(m)

# Save the map to an HTML file or display it
m.save('heatmap_2018_mmt.html')







df = pd.read_excel('../Datasets/2019_final.xlsx')

city_counts = df['City'].value_counts()

locations=[]
for x in city_counts.keys():
    g = geocoder.bing(x, key='AsGXdjL7aL-H4vZdjl5m7BnlELyKTMi4_-CFrr7W4s4LQAkIWmkLZaO6cAD4iqAh')
    results = g.json
    if(results==None):
        break
    # print(results['lat'], results['lng'])
    locations.append((x,results['lat'], results['lng']))


m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Create a heatmap using the hotel counts
heat_data = [(row[1], row[2], int(city_counts[row[0]])) for row in locations]
HeatMap(heat_data, radius=15).add_to(m)

# Save the map to an HTML file or display it
m.save('heatmap_2019_mmt.html')







df = pd.read_excel('../Datasets/2020_final.xlsx')

city_counts = df['City'].value_counts()

locations=[]
for x in city_counts.keys():
    g = geocoder.bing(x, key='AsGXdjL7aL-H4vZdjl5m7BnlELyKTMi4_-CFrr7W4s4LQAkIWmkLZaO6cAD4iqAh')
    results = g.json
    if(results==None):
        break
    # print(results['lat'], results['lng'])
    locations.append((x,results['lat'], results['lng']))

m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Create a heatmap using the hotel counts
heat_data = [(row[1], row[2], int(city_counts[row[0]])) for row in locations]
HeatMap(heat_data, radius=15).add_to(m)

# Save the map to an HTML file or display it
m.save('heatmap_2020_mmt.html')







df = pd.read_excel('../Datasets/2021_final.xlsx')

city_counts = df['City'].value_counts()

locations=[]
for x in city_counts.keys():
    g = geocoder.bing(x, key='AsGXdjL7aL-H4vZdjl5m7BnlELyKTMi4_-CFrr7W4s4LQAkIWmkLZaO6cAD4iqAh')
    results = g.json
    if(results==None):
        break
    # print(results['lat'], results['lng'])
    locations.append((x,results['lat'], results['lng']))
    


m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Create a heatmap using the hotel counts
heat_data = [(row[1], row[2], int(city_counts[row[0]])) for row in locations]
HeatMap(heat_data, radius=15).add_to(m)

# Save the map to an HTML file or display it
m.save('heatmap_2021_mmt.html')







df = pd.read_excel('../Datasets/2022_final.xlsx')

city_counts = df['City'].value_counts()

locations=[]
for x in city_counts.keys():
    g = geocoder.bing(x, key='AsGXdjL7aL-H4vZdjl5m7BnlELyKTMi4_-CFrr7W4s4LQAkIWmkLZaO6cAD4iqAh')
    results = g.json
    if(results==None):
        break
    # print(results['lat'], results['lng'])
    locations.append((x,results['lat'], results['lng']))


m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Create a heatmap using the hotel counts
heat_data = [(row[1], row[2], int(city_counts[row[0]])) for row in locations]
HeatMap(heat_data, radius=15).add_to(m)

# Save the map to an HTML file or display it
m.save('heatmap_2022_mmt.html')







df = pd.read_excel('../Datasets/2023_final.xlsx')

city_counts = df['City'].value_counts()

locations=[]
for x in city_counts.keys():
    g = geocoder.bing(x, key='AsGXdjL7aL-H4vZdjl5m7BnlELyKTMi4_-CFrr7W4s4LQAkIWmkLZaO6cAD4iqAh')
    results = g.json
    if(results==None):
        break
    # print(results['lat'], results['lng'])
    locations.append((x,results['lat'], results['lng']))
    

m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Create a heatmap using the hotel counts
heat_data = [(row[1], row[2], int(city_counts[row[0]])) for row in locations]
HeatMap(heat_data, radius=15).add_to(m)

# Save the map to an HTML file or display it
m.save('heatmap_2023_mmt.html')