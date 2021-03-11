from UTM_proj import xPTK,yPTK,xJJY,yJJY,xeq,yeq,JJY_PTK_distance
from Prep_zone import prep_zone_radius
from Fresnel_zone import fresnelzones

import numpy as np
from math import atan, pi
from shapely.geometry.point import Point
from shapely import affinity
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon

#Fresnel zone centre point
dy = (yPTK - yJJY)/1000
dx = (xPTK - xJJY)/1000
anglefres = atan(dy/dx) * (180/pi)
xfres = dx + dx/2
yfres = dy + dy/2

def create_ellipse(centre, a, b, angle):
    circle = Point(centre).buffer(1)
    ellipse = affinity.scale(circle, int(a), int(b))
    ellipser = affinity.rotate(ellipse, angle)
    return ellipser

#fig setup
fig,ax = plt.subplots()
ax.set_xlim([-3000,6000])
ax.set_ylim([-3000,6000])
ax.set_aspect('equal')

#Fresnel zone ellipse in blue
fresnel_ellipse = create_ellipse((xfres,yfres), JJY_PTK_distance, fresnelzones[0], anglefres)
verts1 = np.array(fresnel_ellipse.exterior.coords.xy)
patch1 = Polygon(verts1.T, color = 'blue', alpha = 0.5)
ax.add_patch(patch1)

#Preperation zone circle in red
overlap_area = []
for i in range(len(prep_zone_radius)):   
    prepzone_circle = create_ellipse(((xeq[i]/1000),(yeq[i]/1000)), prep_zone_radius[i], prep_zone_radius[i], 0)
    verts2 = np.array(prepzone_circle.exterior.coords.xy)
    patch2 = Polygon(verts2.T,color = 'red', alpha = 0.5)
    ax.add_patch(patch2)
    intersect = fresnel_ellipse.intersection(prepzone_circle)
    overlap_area.append(intersect.area/fresnel_ellipse.area)


print(max(overlap_area))
plt.show()


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