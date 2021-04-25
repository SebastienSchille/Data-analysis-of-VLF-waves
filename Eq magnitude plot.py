import numpy as np
from matplotlib import pyplot as plt
#from Intersection import overlap_area_JJY, overlap_area_JJI, overlap_area_NWC, eq_num_JJY, eq_num_JJI, eq_num_NWC

"""
['2004-11-04' '5.9' '61.8' '36.80135424653744']
 ['2004-11-11' '6.1' '32.8' '40.3595004825859']
 ['2004-11-14' '5.5' '25.0' '21.616977094849183']
 ['2004-11-26' '5.7' '58.0' '22.265193348894023']
 ['2004-11-28' '7.0' '39.0' '83.8204142887901']
 ['2004-11-28' '5.9' '39.5' '35.16639758211826']

 for i in range (len(eq_num_JJY)):
    eq_mag = np.genfromtxt('Seismic data.csv', dtype=float, skip_header=1, usecols=(4), delimiter=',')
    eq_depth = np.genfromtxt('Seismic data.csv', dtype=float, skip_header=1, usecols=(3), delimiter=',')
    mag = np.append(mag, eq_mag)
    depth = np.append(depth, eq_depth)
"""

mag = [0,0,0,5.9,0,0,0,0,0,0,6.1,0,0,5.5,0,0,0,0,0,0,0,0,0,0,0,5.7,0,7.0,0,0]
days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
 

#----------Magnitude data plot--------------------
plt.rcParams['font.size'] = '18'
ax = plt.subplot(3,1,1)
plt.bar(days, mag)
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.5)
ax.set_xticks(days)
ax.set_xticklabels(days)
ax.set_title('Seismic activity')
plt.xlabel('Day',labelpad=10)
plt.ylabel('Magnitude', labelpad=10)
plt.show()
#-------------------------------------------------------------------