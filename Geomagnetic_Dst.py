import numpy as np
from matplotlib import pyplot as plt
import os

os.chdir("./Dst Data")
months = ['JAN','FEB','MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
months_len = np.array([0,31,59,90,120,151,181,212,243,273,304,334])
months_len_2004 = np.array([0,31,60,91,121,152,182,213,244,274,305,335])
years = [2004, 2005, 2006, 2007]
Dst_events = np.empty(3)
Dst_year = np.array([])

for a in range(1):
    for b in range(len(months)):
        file_name = 'DST_' + months[b] + str(years[a]) + '.txt'
        Dst_values = np.genfromtxt(file_name, usecols=(range(1,25)))
        Dst_year = np.append(Dst_year, Dst_values.flatten())
        print(file_name)

        for i in range(np.shape(Dst_values)[0]):
            event_counter = 0
            for z in range(np.shape(Dst_values)[1]):
                if Dst_values[i,z] < -100:
                    event_counter += 1
            if event_counter > 0:
                Dst_avg = np.round(np.mean(Dst_values[i,:], axis=0))
                Dst_min = np.min(Dst_values[i,:])
                Dst_events = np.vstack((Dst_events, [(str(i)+months[b]+str(years[a])), Dst_avg, Dst_min]))

Dst_events = np.delete(Dst_events, 0, axis=0)
print(Dst_events)

#----------Geomagnetic data plot--------------------
plt.rcParams['font.size'] = '22'
ax = plt.subplot(1,1,1)
time = range(len(Dst_year))
threshold = []
for i in range(len(Dst_year)):
    threshold.append(-100)
plt.plot(time, Dst_year)
plt.plot(time, threshold, color='red', linestyle='--')
ax.set_title('Geomagnetic activity in 2004')
ax.set_xticks(months_len_2004*24)
ax.set_xticklabels(months)
plt.xlabel('Month',labelpad=15)
plt.ylabel('Dst', labelpad=15)
plt.show()
#-------------------------------------------------------------------