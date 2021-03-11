import pyproj
from Prep_zone import prepzone_data

#JJY, JJI, NWC, PTK
longitudes = [140.849007, 130.829095, 114.16546, 158.550]
latitudes = [37.372557, 32.092247, -21.816325, 53.090] 
#------------------------------------------------------------------------------------

xy_projection = pyproj.Proj(proj='utm', zone=54, ellps='WGS84', preserve_units=False)
xPTK,yPTK = xy_projection(158.550, 53.090)
xJJY,yJJY = xy_projection(140.849007, 37.372557)
xeq,yeq = xy_projection(prepzone_data[:,1], prepzone_data[:,0])


#-----------------------------------------------------------------------------------------
#Distance calc
JJY_PTK_distance = ((((xPTK-xJJY)**2) + ((yPTK-yJJY)**2))**0.5)/1000

## xy to long lat calc
#lat,longi = xy_projection(x,y, inverse=True)