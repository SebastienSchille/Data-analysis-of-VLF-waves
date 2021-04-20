from UTM_proj import xPTK,yPTK,xJJY,yJJY,xJJI,yJJI,xNWC,yNWC,xeq,yeq,JJY_PTK_distance,JJI_PTK_distance,NWC_PTK_distance
from Prep_zone import prep_zone_radius
from Fresnel_zone import fresnelzones

import numpy as np
from math import atan, pi
from shapely.geometry.point import Point
from shapely import affinity
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon

def fresnelcentre (xtrans, ytrans):
    dx = (xPTK - xtrans)/1000
    dy = (yPTK - ytrans)/1000
    anglefres = atan(dy/dx) * (180/pi)
    xfres = (xtrans/1000) + dx/2
    yfres = (ytrans/1000) + dy/2
    return anglefres,xfres,yfres

def create_ellipse(centre, a, b, angle):
    circle = Point(centre).buffer(1)
    ellipse = affinity.scale(circle, int(a), int(b))
    ellipser = affinity.rotate(ellipse, angle)
    return ellipser

#fig setup
fig,ax = plt.subplots()
ax.set_xlim([-3000,4000])
ax.set_ylim([-3000,7000])
ax.set_aspect('equal')

#Fresnel zone ellipses in blue
anglefres,xfres,yfres = fresnelcentre(xJJY, yJJY)
fresnel_ellipse_JJY = create_ellipse((xfres,yfres), (JJY_PTK_distance/2), fresnelzones[3], anglefres)
verts1 = np.array(fresnel_ellipse_JJY.exterior.coords.xy)
patch1 = Polygon(verts1.T, color = 'blue', alpha = 0.5)
ax.add_patch(patch1)

anglefres,xfres,yfres = fresnelcentre(xJJI, yJJI)
fresnel_ellipse_JJI = create_ellipse((xfres,yfres), (JJI_PTK_distance/2), fresnelzones[4], anglefres)
verts2 = np.array(fresnel_ellipse_JJI.exterior.coords.xy)
patch2 = Polygon(verts2.T, color = 'blue', alpha = 0.5)
ax.add_patch(patch2)

anglefres,xfres,yfres = fresnelcentre(xNWC, yNWC)
fresnel_ellipse_NWC = create_ellipse((xfres,yfres), (NWC_PTK_distance/2), fresnelzones[5], anglefres)
verts3 = np.array(fresnel_ellipse_NWC.exterior.coords.xy)
patch3 = Polygon(verts3.T, color = 'blue', alpha = 0.5)
ax.add_patch(patch3)

#Preperation zone circle in red
overlap_area_JJY = np.empty(4)
overlap_area_JJI = np.array([])
overlap_area_NWC = np.array([])
for i in range(len(prep_zone_radius)):   
    prepzone_circle = create_ellipse(((xeq[i]/1000),(yeq[i]/1000)), prep_zone_radius[i], prep_zone_radius[i], 0)
    verts4 = np.array(prepzone_circle.exterior.coords.xy)
    patch4 = Polygon(verts4.T,color = 'red', alpha = 0.5)
    ax.add_patch(patch4)
    intersect_JJY = fresnel_ellipse_JJY.intersection(prepzone_circle)
    intersect_JJI = fresnel_ellipse_JJI.intersection(prepzone_circle)
    intersect_NWC = fresnel_ellipse_NWC.intersection(prepzone_circle)
    overlap_JJY = intersect_JJY.area/fresnel_ellipse_JJY.area*100
    overlap_JJI = intersect_JJI.area/fresnel_ellipse_JJI.area*100
    overlap_NWC = intersect_NWC.area/fresnel_ellipse_NWC.area*100
    eq_date = np.genfromtxt('Seismic data.csv', dtype=str, skip_header=1, usecols=(0), delimiter=',')
    eq_mag = np.genfromtxt('Seismic data.csv', dtype=float, skip_header=1, usecols=(4), delimiter=',')
    eq_depth = np.genfromtxt('Seismic data.csv', dtype=float, skip_header=1, usecols=(3), delimiter=',')
    if overlap_JJY != 0:
        overlap_area_JJY = np.vstack((overlap_area_JJY, [str(eq_date[i]), str(eq_mag[i]), str(eq_depth[i]), overlap_JJY]))
    if overlap_JJI !=0:
        overlap_area_JJI = np.append(overlap_area_JJI, overlap_JJI)
    if overlap_NWC !=0:
        overlap_area_NWC = np.append(overlap_area_NWC, overlap_NWC)
overlap_area_JJY = np.delete(overlap_area_JJY, 0, axis=0)
"""
#Filter overlap results
overlap_area_JJY = overlap_area_JJY[overlap_area_JJY != 0]
overlap_area_JJY = overlap_area_JJY*100
overlap_area_JJI = overlap_area_JJI[overlap_area_JJI != 0]
overlap_area_JJI = overlap_area_JJI*100
overlap_area_NWC = overlap_area_NWC[overlap_area_NWC != 0]
overlap_area_NWC = overlap_area_NWC*100
"""
print("These are the eq overlaps with transmitter JJY", overlap_area_JJY)
print("There are a total of:", len(overlap_area_JJY), "earthquakes that overlap with JJY's signal")
print("These are the eq overlaps with transmitter JJI", overlap_area_JJI)
print("There are a total of:", len(overlap_area_JJI), "earthquakes that overlap with JJI's signal")
print("These are the eq overlaps with transmitter NWC", overlap_area_NWC)
print("There are a total of:", len(overlap_area_NWC), "earthquakes that overlap with NWC's signal")
plt.show()

#----------MKII code----------------------------



#DEMO CODE BELLOW
#--------------------------------------------------
"""
from matplotlib import pyplot as plt
from shapely.geometry.point import Point
from shapely import affinity
from matplotlib.patches import Polygon
import numpy as np

def create_ellipse(centre, a, b, angle):
    circle = Point(centre).buffer(1)
    ellipse = affinity.scale(circle, a, b)
    ellipser = affinity.rotate(ellipse, angle)
    return ellipser

#fig setup
fig,ax = plt.subplots()
ax.set_xlim([0,1000000])
ax.set_ylim([0,1000000])
ax.set_aspect('equal')

#Fresnel zone ellipse in blue
ellipse1 = create_ellipse((xfres,yfres), JJY_PTK_distance, (fresnelzones[0]/2), anglefres)
verts1 = np.array(ellipse1.exterior.coords.xy)
patch1 = Polygon(verts1.T, color = 'blue', alpha = 0.5)
ax.add_patch(patch1)

#Preperation zone circle in red    
prepzone_circle = create_ellipse((xeq[2],yeq[2]), prep_zone_radius[2], prep_zone_radius[2], 0)
verts2 = np.array(prepzone_circle.exterior.coords.xy)
patch2 = Polygon(verts2.T,color = 'red', alpha = 0.5)
ax.add_patch(patch2)

##the intersect will be outlined in black
intersect = ellipse1.intersection(prepzone_circle)
#verts3 = np.array(intersect.exterior.coords.xy)
#patch3 = Polygon(verts3.T, facecolor = 'none', edgecolor = 'black')
#ax.add_patch(patch3)

##compute areas and ratios 
print('area of ellipse 1:',ellipse1.area)
print('area of ellipse 2:',prepzone_circle.area)
print('area of intersect:',intersect.area)
print('intersect/ellipse1:', intersect.area/ellipse1.area)
print('intersect/ellipse2:', intersect.area/prepzone_circle.area)

plt.show()
"""