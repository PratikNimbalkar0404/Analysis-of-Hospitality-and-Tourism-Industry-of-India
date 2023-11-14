import pandas as pd
import geopandas as gpd
import folium
import geocoder  
from folium.plugins import HeatMap
from time import sleep

# Load the Excel file with hotel data into a DataFrame
df = pd.read_excel("2017.xlsx")


# Assuming your Excel column with city names is named 'City' (change to the actual column name)
# You may need to clean and preprocess the data to ensure the 'City' column is consistent and accurate.
city_counts = df['City'].value_counts()
for x in city_counts.keys():
    print(x,city_counts[x])



g = geocoder.bing('Delhi', key='AsGXdjL7aL-H4vZdjl5m7BnlELyKTMi4_-CFrr7W4s4LQAkIWmkLZaO6cAD4iqAh')
results = g.json
print(results['lat'], results['lng'])
locations=[]
for x in city_counts.keys():
    g = geocoder.bing(x, key='AsGXdjL7aL-H4vZdjl5m7BnlELyKTMi4_-CFrr7W4s4LQAkIWmkLZaO6cAD4iqAh')
    results = g.json
    if(results==None):
        break
    # print(results['lat'], results['lng'])
    locations.append((x,results['lat'], results['lng']))
    

print(locations)

# m=folium.Map([48,5],zoom_start=5)
# HeatMap(locations )

# # Download India's shapefile (for plotting boundaries)
# india_map = gpd.read_file('indiashp')

# # Merge hotel counts with India's shapefile based on city name
# india_hotels = india_map.merge(city_counts, left_on='id', right_index=True,)

# print(india_hotels)

# india_hotels['geometry'] = india_hotels['geometry'].centroid
# india_hotels['LAT'] = india_hotels['geometry'].y
# india_hotels['LON'] = india_hotels['geometry'].x


# print("\n\n")
# for _,y in india_hotels.iterrows():
#     print(y) 
# print("\n\n")


# Create a base map centered around India
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Create a heatmap using the hotel counts
heat_data = [(row[1], row[2], int(city_counts[row[0]])) for row in locations]
print(heat_data)
HeatMap(heat_data, radius=15).add_to(m)

# Save the map to an HTML file or display it
m.save('heatmap.html')

