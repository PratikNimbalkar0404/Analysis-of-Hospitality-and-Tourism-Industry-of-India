import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()

import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls

pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 999

import matplotlib.pyplot as plt
import matplotlib.cm

from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize


df = pd.read_csv('../Datasets/zomato_restaurants_in_India.csv',error_bad_lines=False)


df.describe()



# selected top cities to create a new Dataframe
#Hyderabad,Kolkata,Guwahati,Mumbai,NewDelhiAndNCR,Bangalore,Vijaywada,Chennai

#cities = [ 'Lucknow', 'New Delhi', 'Agra', 'Ludhiana', 'Dehradun', 'Kanpur', 'Jammu', 'Varanasi', 'Meerut', 'Amritsar', 'Jalandhar', 'Gorakhpur',  'Chandigarh', 'Dharamshala' ]
#cities = ['Chennai', 'Bangalore', 'Kochi', 'Coimbatore', 'Puducherry', 'Vizag', 'Trivandrum', 'Mysore', 'Madurai', 'Mangalore', 'Trichy', 'Vellore', 'Vijayawada']

cities=[
'Mumbai',
'Pune',
'Nashik',
'Aurangabad',
'Nagpur',
'Goa',
'Amravati',
'Kolhapur'

]

newdf = df.loc[df['city'].isin(cities)]




# Create the crosstab DataFrame
s = pd.crosstab(index=newdf['city'], columns=newdf['Ratings'])

# Specify custom colors for each bar
colors = ['blue', 'red', 'green', 'orange', 'purple']  # Set the colors for the bars

# Plot the DataFrame with custom colors
bar = s.plot(kind='bar', figsize=(12, 4), title='Count of Ratings based on Cities (Maharshtra and Goa)', fontsize=15, color=colors)
bar.set_ylabel("Number of Restaurants", fontsize=15)
bar.set_xlabel("Cities", fontsize=15)  # Increase the font size of x-axis label

# Customize the legend to specify the colors for each rating category
legend_labels = [0, 2, 3, 4, 5]
bar.legend(legend_labels, title='Ratings', fontsize=15)
bar.title.set_fontsize(20)

plt.show()



