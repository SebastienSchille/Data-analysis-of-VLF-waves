import numpy as np
from matplotlib import pyplot as plt
import os

os.chdir("./Dst Data")
months = ['JAN','FEB','MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
months_len = np.array([0,31,59,90,120,151,181,212,243,273,304,334])
months_len_2004 = np.array([0,31,60,91,121,152,182,213,244,274,305,335])

file_name = 'DST_' + 'NOV' + '2004' + '.txt'
Dst_values = np.genfromtxt(file_name, usecols=(range(1,25)))
Dst_values = Dst_values.flatten()


#----------Geomagnetic data plot--------------------
plt.rcParams['font.size'] = '18'
ax = plt.subplot(3,1,1)
time = range(len(Dst_values))
threshold = []
for i in range(len(Dst_values)):
    threshold.append(-100)
plt.plot(time, Dst_values)
plt.plot(time, threshold, color='red', linestyle='--')
ax.set_title('Geomagnetic activity in 2004')
ax.set_xticks(range(0,748,48))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Month',labelpad=10)
plt.ylabel('Dst', labelpad=10)
plt.show()
#-------------------------------------------------------------------