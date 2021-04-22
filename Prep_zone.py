#Import Python libraries
import math as math
import numpy as np

#Read the csv data into a Numpy array
seismic_data = np.genfromtxt('Seismic data.csv', delimiter=',', skip_header=1)
latitude_eq = seismic_data[:, 1]
longitude_eq = seismic_data[:, 2]
magnitude = seismic_data[:, 4]

#Calculate the preparation zone using the Dobrovolsky equation
prep_zone_radius = 10**(0.43*magnitude)
prep_zone_area = math.pi*(prep_zone_radius**2)

#Store the values into a new Numpy array to be used other programs
prepzone_data = np.column_stack((latitude_eq, longitude_eq, prep_zone_radius, prep_zone_area))


#-----Report visuals---------------------------------------------------------
"""
vis_data = np.column_stack((magnitude, prep_zone_radius))
np.set_printoptions(edgeitems=5)
"""
