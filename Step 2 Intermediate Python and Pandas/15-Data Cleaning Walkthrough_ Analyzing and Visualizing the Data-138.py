## 3. Finding Correlations With the r Value ##

correlations = combined.corr()
print(correlations['sat_score'])
print(correlations)


## 5. Plotting Enrollment With the Plot() Accessor ##

import matplotlib.pyplot as plt

combined.plot.scatter(x="total_enrollment", y="sat_score")
plt.show()

## 6. Exploring Schools With Low SAT Scores and Enrollment ##

low_enrollment = combined[combined['total_enrollment'] < 1000]
low_enrollment = low_enrollment[low_enrollment['sat_score'] < 1000]

low_enrollment['School Name']

## 7. Plotting Language Learning Percentage ##

# Create a scatterplot of ell_percent versus sat_score
combined.plot.scatter(x="ell_percent", y="sat_score")
plt.show()

## 9. Mapping the Schools With Basemap ##

#create a map that centers on New York City (llcrnrlat, urcrnrlat, llcrnrlon, and urcrnrlon define the corners of the geographic area the map depicts). 
from mpl_toolkits.basemap import Basemap
m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)         # draw coastlines and rivers accordingly.
m.drawrivers(color='#6D5F47', linewidth=.4)

# Convert the lon & lat columns of combined to a list, and assign it to the longitudes variable
lon = combined['lon'].tolist()
lat = combined['lat'].tolist()

# Call the Basemap.scatter() method on m, and pass in longitudes and latitudes as arguments.
m.scatter(lon, lat, latlon=True, s=20, zorder=2)
# s=20  to increase the size of the points in the scatterplot.
# zorder=2 to plot the points on top of the rest of the map
# latlon=True to indicate that we're passing in latitude and longitude coordinates, rather than axis coordinates.

# Show the plot
plt.show()

## 10. Plotting Out Statistics ##

from mpl_toolkits.basemap import Basemap
m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)         
m.drawrivers(color='#6D5F47', linewidth=.4)

lon = combined['lon'].tolist()
lat = combined['lat'].tolist()


m.scatter(lon, lat, latlon=True, s=20, zorder=2, c=combined['ell_percent'], cmap='summer')
plt.show()

## 11. Calculating District-Level Statistics ##

import numpy

# aggregate by district & calculate the average of each group
districts = combined.groupby('school_dist').agg(numpy.mean)
districts.reset_index(inplace=True)
districts.head()

## 12. Plotting Percent Of English Learners by District ##

from mpl_toolkits.basemap import Basemap
m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)         
m.drawrivers(color='#6D5F47', linewidth=.4)

lon = districts['lon'].tolist()
lat = districts['lat'].tolist()

m.scatter(lon, lat, latlon=True, s=50, zorder=2, c=districts['ell_percent'], cmap='summer')
plt.show()