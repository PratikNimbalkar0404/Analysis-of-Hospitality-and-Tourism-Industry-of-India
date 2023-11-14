import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import random
from wordcloud import WordCloud

data = pd.read_csv("../Datasets/zomato_restaurants_in_India.csv")

data.describe()

data.drop_duplicates(["res_id"],keep='first',inplace=True)
data.shape

outlets = data["name"].value_counts()

chains = outlets[outlets >= 2]
single = outlets[outlets == 1]


print("Total Restaurants = ", data.shape[0])
print("Total Restaurants that are part of some chain = ", data.shape[0] - single.shape[0])
print("Percentage of Restaurants that are part of a chain = ", np.round((data.shape[0] - single.shape[0]) / data.shape[0],2)*100, "%")

top10_chains = data["name"].value_counts()[:10].sort_values(ascending=True)




#######################################Top chains Number wise 
height = top10_chains.values
bars = top10_chains.index
y_pos = range(len(bars))

fig = plt.figure(figsize=(11, 7))
ax = fig.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_color("black")

# Create a gradient of green shades
n_bars = len(bars)
colors = plt.cm.Greens(np.linspace(0.2, 1, n_bars))

plt.barh(y_pos, height, color=colors)

plt.yticks(y_pos, bars, color="black", fontsize=16)
plt.xticks(color="black", fontsize=16)
plt.xlabel("Number of outlets", color="black", fontsize=16)
plt.title("No. of Outlets of Top Restaurant Chains in India", color="black", fontsize=18)

for i, v in enumerate(height):
    ax.text(v + 3, i, str(v), color="black", fontsize=16)

plt.show()




############################## Top Chains ratins wise


outlets = data["name"].value_counts()
atleast_5_outlets = outlets[outlets > 4]
top10_chains2 = data[data["name"].isin(atleast_5_outlets.index)].groupby("name").mean()["aggregate_rating"].sort_values(ascending=False)[:10].sort_values(ascending=True)


height = pd.Series(top10_chains2.values).map(lambda x: np.round(x, 2))
bars = top10_chains2.index
y_pos = np.arange(len(bars))

fig = plt.figure(figsize=(11, 7), frameon=False)
ax = fig.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_color("black")

colors = ["lightgreen"] * len(bars)

plt.barh(y_pos, height, color=colors)

plt.xlim(3)
plt.xticks(color="black", fontsize=16)
plt.yticks(y_pos, bars, color="black", fontsize=16)
plt.xlabel("Number of outlets", color="black", fontsize=16)
plt.title("No. of Outlets of Highest Rated Restaurant Chains in India", color="black", fontsize=18)

for i, v in enumerate(height):
    ax.text(v + 0.01, i, str(v), color="black", fontsize=16)

plt.show()




################################ Establishments Types 

est_count = data.groupby("establishment").count()["res_id"].sort_values(ascending=False)[:5]

fig = plt.figure(figsize=(8, 5), frameon=False)
ax = fig.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_color("black")

colors = ['#4c3430', '#b04829', '#ec8c41', '#f7c65d', '#fded86']

plt.bar(est_count.index, est_count.values, color=colors)

plt.xticks(range(0, 6), color="black", fontsize=12)
plt.yticks(range(0, 25000, 5000), color="black", fontsize=12)
plt.xlabel("Establishment types", color="black", fontsize=16)
plt.ylabel("Number of restaurants", color="black", fontsize=16)


for i, v in enumerate(est_count):
    ax.text(i - 0.2, v + 500, str(v), color='black', fontsize=16)
plt.title("Types of Restaurants", color="black", fontsize=18)

plt.show()




######################################## City wise Restaurant count 


city_counts = data.groupby("city").count()["res_id"].sort_values(ascending=True)[-10:]

width = pd.Series(city_counts.values)
bars = city_counts.index
x_pos = np.arange(len(bars))

fig = plt.figure(figsize=[13, 7], frameon=False)
ax = fig.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible("black")
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_color("black")

colors = ['#f7c65d', '#f7c65d', '#f7c65d', '#f7c65d', '#f7c65d', '#f7c65d', '#f7c65d', '#f7c65d', '#f7c65d', '#f7c65d']

plt.bar(x_pos, width, color=colors)

plt.ylim(3)
plt.yticks(color="black", fontsize=12)
plt.xticks(x_pos, bars, color="black", fontsize=12)
plt.xlabel("City", fontsize=16)
plt.ylabel("Number of outlets", fontsize=16)

for i, v in enumerate(width):
    ax.text(i, v + 20, str(v), color='black')
plt.title("Number of restaurants (by city)", fontsize=18)

plt.show()




################################# Cuisines type

print("Total number of unique cuisines = ", cuisines.nunique())

c_count = cuisines.value_counts()[:5]

fig = plt.figure(figsize=(8, 5), frameon=False)
ax = fig.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_color("black")

colors = ['#4c3430', '#b04829', '#ec8c41', '#f7c65d', '#fded86']

plt.bar(c_count.index, c_count.values, color=colors)

plt.xticks(range(0, 6), color="black", fontsize=12)
plt.yticks(range(0, 30000, 5000), color="black", fontsize=12)
plt.xlabel("Top 5 cuisines", color="black", fontsize=16)
plt.ylabel("No. of Restaurants", color="black", fontsize=16)


for i, v in enumerate(c_count):
    ax.text(i - 0.2, v + 500, str(v), color='black', fontsize=16)
plt.title("Cuisine Types Analysis", color="black", fontsize=18)

plt.show()



############################################# Average price for 2



pr_count = data.groupby("price_range").count()["name"]

fig = plt.figure(figsize=(8, 5), frameon=False)
ax = fig.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_color("black")

colors = ['#4c3430', '#b04829', '#ec8c41', '#f7c65d']
plt.bar(pr_count.index, pr_count.values, color=colors)

# Custom x-axis labels
custom_labels = ['0', '0-1000', '1000-2000', '2000-3000', '>3000']
plt.xticks(range(0, 5), custom_labels, color="black", fontsize=12)  # Set custom labels

plt.yticks(range(0, 40000, 5000), color="black", fontsize=12)
plt.xlabel("Price Ranges", color="black", fontsize=16)

for i, v in enumerate(pr_count):
    ax.text(i + 0.85, v + 700, str(v), color='black', fontsize=12)
plt.title("Number of restaurants (by price ranges for two)", color="black", fontsize=18)

plt.show()



