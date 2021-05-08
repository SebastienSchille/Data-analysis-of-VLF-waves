import numpy as np
from matplotlib import pyplot as plt
import os

os.chdir("./EPS Data")
months = ['JAN','FEB','MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
electron_year = np.array([])
proton_year = np.array([])

for i in range(len(months)):
    file_name = 'EPS data ' + months[i] + '2004.csv'
    electron_values = np.genfromtxt(file_name, skip_header=1, delimiter=',', usecols=(0))
    proton_values = np.genfromtxt(file_name, skip_header=1, delimiter=',', usecols=(1))
    electron_values[electron_values < 0] = float('nan')
    proton_values[proton_values < 0] = float('nan')
    electron_year = np.append(electron_year, electron_values)
    proton_year = np.append(proton_year, proton_values)

#------Electron plot---------------------------------------
plt.subplots_adjust(hspace=0.4)
plt.rcParams['font.size'] = '18'

ax = plt.subplot(2,1,1)
time = range(len(electron_year))
plt.plot(time, electron_year)
ax.set_title('Electron flux >2Mev (2004)')
ax.set_xticks(list(range(0,103680,8640)))
ax.set_xticklabels(months)
#ax.set_yticklabels(["{:.2e}".format(t) for t in ax.get_yticks()])
plt.xlabel('Month',labelpad=15)
plt.ylabel('e / cm^2 s sr', labelpad=15)

#------------Proton plot-----------------------------------
ax = plt.subplot(2,1,2)
time = range(len(proton_year))
plt.plot(time, proton_year)
ax.set_title('Proton flux 0.6MeV - 4.0MeV (2004)')
ax.set_xticks(list(range(0,103680,8640)))
ax.set_xticklabels(months)
#ax.set_yticklabels(["{:.2e}".format(t) for t in ax.get_yticks()])
plt.xlabel('Month',labelpad=15)
plt.ylabel('ion / cm^2 s sr Mev', labelpad=15)
plt.show()