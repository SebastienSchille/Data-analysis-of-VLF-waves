import numpy as np
from matplotlib import pyplot as plt
import os

os.chdir("./EPS Data")
months = ['JAN','FEB','MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

file_name = 'EPS data ' + 'NOV' + '2004.csv'
electron_values = np.genfromtxt(file_name, skip_header=1, delimiter=',', usecols=(0))
proton_values = np.genfromtxt(file_name, skip_header=1, delimiter=',', usecols=(1))
electron_values[electron_values < 0] = float('nan')
proton_values[proton_values < 0] = float('nan')

#------Electron plot---------------------------------------
plt.subplots_adjust(hspace=0.4)
plt.rcParams['font.size'] = '18'

ax = plt.subplot(3,1,1)
time = range(len(electron_values))
plt.plot(time, electron_values)
ax.set_title('Electron flux >2Mev')
ax.set_xticks(list(range(0,8928,576)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
#ax.set_yticklabels(["{:.2e}".format(t) for t in ax.get_yticks()])
#plt.xlabel('Day',labelpad=15)
plt.ylabel('e / cm^2 s sr', labelpad=15)

#------------Proton plot-----------------------------------
ax = plt.subplot(3,1,2)
time = range(len(proton_values))
plt.plot(time, proton_values)
ax.set_title('Proton flux 0.6MeV - 4.0MeV')
ax.set_xticks(list(range(0,8928,576)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
#ax.set_yticklabels(["{:.2e}".format(t) for t in ax.get_yticks()])
#plt.xlabel('Day',labelpad=15)
plt.ylabel('ion / cm^2 s sr Mev', labelpad=15)
plt.show()