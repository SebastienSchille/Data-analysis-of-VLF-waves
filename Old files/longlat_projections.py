import pandas as pd
import geopandas
from math import pi,cos
from geopandas import GeoSeries
import shapely
from matplotlib import pyplot as plt
from Fresnel_zone import fresnelzones_JJY, fresnelzones_JJI, fresnelzones_NWC
from Prep_zone import prep_zone_area

df = pd.DataFrame({'VLF code': ['PTK', 'JJY', 'JJI', 'NWC'], 'Latitude': [53.090, 37.372557, 32.092247, -21.816325], 'Longitude': [158.550, 140.849007, 130.829095, 114.16546]})

def fresnaldistance(fresnelr, phi):
    earthr = 6357
    latitude_deg = fresnelr / 111
    longitude_deg = fresnelr / ((pi/180) * earthr * cos(phi))
    print(latitude_deg)
    print(longitude_deg)
    return longitude_deg


fresnaldistance(fresnelzones_JJY, df.Longitude[1])
fresnaldistance(fresnelzones_JJI, df.Longitude[2])
fresnaldistance(fresnelzones_NWC, df.Longitude[3])

#Working code-------------------------------------------------------------
geodf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
print(geodf)

#Scalar distances
distances_xy = geodf.distance(geodf.geometry[0])
print(distances_xy)

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
# World plot
ax = world.plot(color='white', edgecolor='black')

import shapely.affinity
from shapely.geometry import Point

circle = Point(geodf.Longitude[1], geodf.Latitude[1]).buffer(1)  # type(circle)=polygon
ellipse = shapely.affinity.scale(circle, fresnaldistance(fresnelzones_JJY, df.Longitude[1]), (23.67/2))
ellipser = shapely.affinity.rotate(ellipse, -40)
line = shapely.geometry.LineString([(geodf.geometry[0]), (geodf.geometry[1])])
ellipsedf = GeoSeries([ellipser])
print(ellipsedf)
ellipsedf.plot(ax=ax)
geodf.plot(ax=ax, color='red')
plt.show()
#Working code-----------------------------------------------

