import numpy as np
from matplotlib import pyplot as plt
import os

os.chdir("./Dst Data")
months = ['JAN','FEB','MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
months_len = np.array([0,31,59,90,120,151,181,212,243,273,304,334])
months_len_2004 = np.array([0,31,60,91,121,152,182,213,244,274,305,335])
Dst_year = np.array([])

for a in range(len(months)):
    file_name = 'DST_' + months[a] + '2004' + '.txt'
    Dst_values = np.genfromtxt(file_name, usecols=(range(1,25)))
    Dst_year = np.append(Dst_year, Dst_values.flatten())


#----------Geomagnetic data plot--------------------
plt.rcParams['font.size'] = '18'
ax = plt.subplot(2,1,1)
time = range(len(Dst_year))
threshold = []
for i in range(len(Dst_year)):
    threshold.append(-100)
plt.plot(time, Dst_year)
plt.plot(time, threshold, color='red', linestyle='--')
ax.set_title('Geomagnetic activity')
ax.set_xticks(months_len_2004*24)
ax.set_xticklabels(months)
plt.xlabel('Month',labelpad=10)
plt.ylabel('Dst (nT)', labelpad=10)
plt.show()
#-------------------------------------------------------------------