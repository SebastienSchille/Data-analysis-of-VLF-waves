import pyproj
from Prep_zone import prepzone_data

#JJY, JJI, NWC, PTK
longitudes = [140.849007, 130.829095, 114.16546, 158.550]
latitudes = [37.372557, 32.092247, -21.816325, 53.090]

#------------------------------------------------------------------------------------

xy_projection = pyproj.Proj(proj='utm', zone=54, ellps='WGS84', preserve_units=False)
xPTK,yPTK = xy_projection(158.550, 53.090)
xJJY,yJJY = xy_projection(140.849007, 37.372557)
xJJI,yJJI = xy_projection(130.829095, 32.092247)
xNWC,yNWC = xy_projection(114.16546, -21.816325)
xeq,yeq = xy_projection(prepzone_data[:,1], prepzone_data[:,0])

#Distance calculation
JJY_PTK_distance = ((((xPTK-xJJY)**2) + ((yPTK-yJJY)**2))**0.5)/1000
JJI_PTK_distance = ((((xPTK-xJJI)**2) + ((yPTK-yJJI)**2))**0.5)/1000
NWC_PTK_distance = ((((xPTK-xNWC)**2) + ((yPTK-yNWC)**2))**0.5)/1000


#Projections on multiple UTM planes
#------------------------------------------------------------------------------------
"""
JJY_projection = pyproj.Proj(proj='utm', zone=53, ellps='WGS84', preserve_units=False)
xPTK_JJYproj,yPTK_JJYproj = JJY_projection(158.550, 53.090)
xJJY,yJJY = JJY_projection(140.849007, 37.372557)
xeq_JJIproj,yeq_JJIproj = JJY_projection(prepzone_data[:,1], prepzone_data[:,0])

JJI_projection = pyproj.Proj(proj='utm', zone=54, ellps='WGS84', preserve_units=False)
xPTK_JJIproj,yPTK_JJIproj = JJI_projection(158.550, 53.090)
xJJI,yJJI = JJI_projection(130.829095, 32.092247)
xeq_JJIproj,yeq_JJIproj = JJI_projection(prepzone_data[:,1], prepzone_data[:,0])

NWC_projection = pyproj.Proj(proj='utm', zone=52, ellps='WGS84', preserve_units=False)
xPTK_NWCproj,yPTK_NWCproj = NWC_projection(158.550, 53.090)
xNWC,yNWC = NWC_projection(114.16546, -21.816325)
xeq_NWCproj,yeq_NWCproj = JJI_projection(prepzone_data[:,1], prepzone_data[:,0])

#Distance calc
JJY_PTK_distance = ((((xPTK_JJYproj-xJJY)**2) + ((yPTK_JJYproj-yJJY)**2))**0.5)/1000
JJI_PTK_distance = ((((xPTK_JJIproj-xJJI)**2) + ((yPTK_JJIproj-yJJI)**2))**0.5)/1000
NWC_PTK_distance = ((((xPTK_NWCproj-xNWC)**2) + ((yPTK_NWCproj-yNWC)**2))**0.5)/1000
"""
#-----------------------------------------------------------------------------------------

## xy to long lat calc
#lat,longi = xy_projection(x,y, inverse=True)