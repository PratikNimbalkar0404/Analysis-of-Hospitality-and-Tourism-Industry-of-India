import os
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


df = pd.read_csv('../Datasets/makemytrip_com-travel_sample.csv',error_bad_lines=False)


df.describe()



cities = ['Agra','Lucknow','NewDelhiAndNCR', 'Chandigarh', 'Jammu', 'Shimla', 'Varanasi']

newdf = df.loc[df['city'].isin(cities)]