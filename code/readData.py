from PIL import Image
import math
import os
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import PowerNorm

# input
threshold = 5
year = 2020

x_bins, y_bins = 100, 100
lon_min, lon_max = 1.67, 7.34         #1.67-7.34
lat_min, lat_max = 49.1, 51.95        #49.1-51.95

# constants
x_0, lon_0 = 2, 1.67
y_0, lat_0 = 2, 51.95

x_per_lon = 133.157
y_per_lat = 207.458

delta_x = (lon_max-lon_min)/x_bins
delta_y = (lat_max-lat_min)/y_bins

models = ["harmonie", "swisseu", "ezswiss"]

colors = [(255, 255, 255), (248, 248, 248), (220, 220, 250), (170, 170, 200), (117, 186, 255), (53, 154, 255), (4, 130, 255), (0, 105, 210), (0, 79, 157), (0, 50, 127), (75, 0, 127), (100, 0, 127), (145, 0, 187), (194, 0, 251)]
color_values = [None, 0, 0.25, 0.75, 1.5, 2.5, 3.5, 4.5, 6, 8.5, 12.5, 17.5, 25, 35]

def calculate_coordinates():
  for x_bin in range(x_bins):
    for y_bin in range(y_bins):
      lon = lon_min + x_bin*delta_x
      lat = lat_min + y_bin*delta_y
      lons.append(lon)
      lats.append(lat)

lons, lats = [], []
calculate_coordinates()

def value_from_color(color):
  if color not in colors:
    return -1
  index = colors.index(color)
  return color_values[index]

def read_values(pixels):
  values = []
  for x_bin in range(x_bins):
    for y_bin in range(y_bins):
      lon = lon_min + x_bin*delta_x
      lat = lat_min + y_bin*delta_y
      x = math.floor((lon-lon_0)*x_per_lon + x_0)
      y = math.floor((lat_0-lat)*y_per_lat + y_0)

      color = pixels[x,y]
      value = value_from_color(color)
      while value == -1:
        y -= 1
        color = pixels[x,y]
        value = value_from_color(color)

      if(value and value > threshold): values.append(1)
      else: values.append(0)
  return values


data = pd.DataFrame(list(zip(lons, lats)), columns=["longitude", "latitude"])

for model in models:
  days = [0] * (x_bins*y_bins)
  dir = f"./data/{year}/{model}"

  for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    if os.path.isfile(f):
      im = Image.open(f)
      pixels = im.load()
      res = read_values(pixels)
      for i in range(len(days)):
        days[i] += res[i]
        
  print(model + " finished")
  data[model] = days

data["mean"] = data[models].mean(axis=1)
data.to_csv(f"./out/data_{year}_{threshold}cm.txt", index=False)

# plotting
x = np.arange(lon_min, lon_max, delta_x)
y = np.arange(lat_min, lat_max, delta_y)
z = data["mean"].to_numpy().reshape(x_bins, y_bins).transpose()

gdf = gpd.read_file("./shapefile/provinces_L08.shp")
fig, ax = plt.subplots(figsize=(8, 8))
ax = gdf.to_crs(epsg=4326).plot(ax=ax, color="lightgrey", edgecolor="black")
c = ax.pcolormesh(x, y, z, alpha=0.7, shading="auto", cmap=cm.jet, norm=PowerNorm(gamma=0.6))
plt.colorbar(c)

ax.set_title(f"Days with >{threshold}cm snow in winter {year}-{year+1}")
plt.xlabel("lon(°)")
plt.ylabel("lat(°)")

plt.show()