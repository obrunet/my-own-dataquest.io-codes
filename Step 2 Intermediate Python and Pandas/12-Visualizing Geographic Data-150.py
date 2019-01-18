## 1. Geographic Data ##

# In this mission, we'll explore the fundamentals of geographic coordinate systems and how to work with the basemap library to plot geographic data points on maps. 

import pandas as pd

airlines = pd.read_csv('airlines.csv')
airports = pd.read_csv('airports.csv')
routes = pd.read_csv('routes.csv')

print(airlines.iloc[0])
print(airports.iloc[0])
print(routes.iloc[0])

## 4. Workflow With Basemap ##

# general workflow:
# - Create a new basemap instance with the specific map projection we want to use and how much of the map we want included.
# - Convert spherical coordinates to Cartesian coordinates using the basemap instance.
# - Use the matplotlib and basemap methods to customize the map.
# - Display the map.

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Create a new basemap instance
m = Basemap(projection="merc", llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)

# projection: the map projection.
# llcrnrlat: latitude of lower left hand corner of the desired map domain
# urcrnrlat: latitude of upper right hand corner of the desired map domain
# llcrnrlon: longitude of lower left hand corner of the desired map domain
# urcrnrlon: longitude of upper right hand corner of the desired map domain



                                 
                                 
                                 
# ---------- Side note ---------- 
# Latitude and longitude values describe points on a sphere, which is three-dimensional. To plot the values on a two-dimensional plane, we need to convert the coordinates to the Cartesian coordinate system using a map projection.

# A map projection transforms points on a sphere to a two-dimensional plane. When projecting down to the two-dimensional plane, some properties are distorted. Each map projection makes trade-offs in what properties to preserve and you can read about the different trade-offs here. We'll use the Mercator projection, because it is commonly used by popular mapping software.







# Basemap is an extension to Matplotlib that makes it easier to work with geographic data. The documentation for basemap provides a good high-level overview of what the library does:

#The matplotlib basemap toolkit is a library for plotting 2D data on maps in Python. Basemap does not do any plotting on it’s own, but provides the facilities to transform coordinates to one of 25 different map projections.

#Basemap makes it easy to convert from the spherical coordinate system (latitudes & longitudes) to the Mercator projection. While basemap uses Matplotlib to actually draw and control the map, the library provides many methods that enable us to work with maps quickly. Before we dive into how basemap works, let's get familiar with how to install it.

#The easiest way to install basemap is through Anaconda. If you're new to Anaconda, we recommend checking out the installation documentation:
# conda install basemap

#If the above code does not work for you, you can install Basemap through the Linux command line using the following code:
# conda install -c conda-forge basemap

# The Basemap library has some external dependencies that Anaconda handles the installation for. To test the installation, run the following import code:
#from mpl_toolkits.basemap import Basemap

# If an error is returned, we recommend searching for similar errors on StackOverflow to help debug the issue. Because basemap uses matplotlib, you'll want to import matplotlib.pyplot into your environment when you use Basemap.

## 5. Converting From Spherical to Cartesian Coordinates ##

# Convertion of latitude and longitude values to Cartesian coordinates to display them on a two-dimensional map

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)

# The constructor only accepts list values, so we'll need to use Series.tolist()
x, y = m(airports['longitude'].tolist(), airports['latitude'].tolist())

#The basemap object return 2 list objects x and y

## 6. Generating A Scatter Plot ##

# Now that the data is in the right format, we can plot the coordinates on a map. A scatter plot is the simplest way to plot points on a map

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
x, y = m(longitudes, latitudes)

# The basemap.scatter() method has similar parameters to the pyplot.scatter().
m.scatter(x,y,s=1)

# customize the size of each marker using the s parameters

plt.show()

## 7. Customizing The Plot Using Basemap ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)

#Use basemap.drawcoastlines() to enable the coast lines to be displayed
m.drawcoastlines()
plt.show()

## 8. Customizing The Plot Using Matplotlib ##

# Because basemap uses matplotlib under the hood, we can interact with the matplotlib classes that basemap uses directly to customize the appearance of the map


# Added code here, before creating the Basemap instance.
#fig, ax = plt.subplots()
fig = plt.figure(figsize=(20, 15))
ax = fig.add_subplot(1, 1, 1)
ax.set_title("Scaled Up Earth With Coastlines")

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()
plt.show()

## 9. Introduction to Great Circles ##

# To better understand the flight routes, we can draw great circles to connect starting and ending locations on a map. A great circle is the shortest circle connecting 2 points on a sphere. On a two-dimensional map, the great circle is demonstrated as a line because it is projected from three-dimensional down to two-dimensional using the map projection. We can use these to visualize the flight routes.

geo_routes = pd.read_csv('geo_routes.csv')

geo_routes.info()
geo_routes.head()

## 10. Displaying Great Circles ##

# We use the basemap.drawgreatcircle() method to display a great circle between 2 points. 


# draws a great circle for each route of a df only if
# the latitude and longitude absolute difference values less than 180
def create_great_circles(df):
    # Iterate over the rows in the df
    for i, row in df.iterrows():
        # Absolute value conditions
        if abs(row['end_lat'] - row['start_lat']) < 180 and abs(row['end_lon'] - row['start_lon']) < 180:
            # Draw a great circle using the four geographic coordinates
            m.drawgreatcircle(row['start_lon'], row['start_lat'], row['end_lon'], row['end_lat'])



# filtered dataframe with the routes that start at the DFW airport. 
dfw = geo_routes[geo_routes['source']=='DFW']

fig, ax = plt.subplots(figsize=(15,20))
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()

# Pass dfw into create_great_circles() and display the plot using the pyplot.show() function
create_great_circles(dfw)
plt.show()




# Basemap struggles to create great circles for routes that have an absolute difference of larger than 180 degrees for either the latitude or longitude values. This method isn't able to create great circles properly when they go outside of the map boundaries.