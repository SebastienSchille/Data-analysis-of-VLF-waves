#Import python libraries
import math as math
import numpy as np

#Read the csv data into a numpy array
seismic_data = np.genfromtxt('Seismic data.csv', delimiter=',', skip_header=1)
latitude_eq = seismic_data[:, 1]
longitude_eq = seismic_data[:, 2]
magnitude = seismic_data[:, 4]

#Calculate the preparation zone using the Dobrovolsky equation
prep_zone_radius = 10**(0.43*magnitude)
prep_zone_area = math.pi*(prep_zone_radius**2)

prepzone_data = np.column_stack((latitude_eq, longitude_eq, prep_zone_radius, prep_zone_area))
#REPORT VISUALS
#--------------------------------------------------------------
"""
vis_data = np.column_stack((magnitude, prep_zone_radius))
np.set_printoptions(edgeitems=5)
"""
