import numpy as np
from matplotlib import pyplot as plt
import os

os.chdir("./EPS Data")
months = ['JAN','FEB','MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
years = [2004, 2005, 2006, 2007]
EPS_events_electron = np.empty(3)
EPS_events_proton = np.empty(3)
EPS_2004 = np.array([0,0])

for a in range(1):
    for b in range(len(months)):
        event_counter_electron = 0
        event_counter_proton = 0
        file_name = 'EPS data ' + months[b] +'2004.csv'
        EPS_values = np.genfromtxt(file_name, skip_header=1, delimiter=',')
        EPS_2004 = np.vstack((EPS_2004, EPS_values))

        for i in range(np.shape(EPS_values)[0]):
            if i % 287 == 0 and event_counter_electron > 0 and i !=0:
                EPS_avg = np.round(np.mean(EPS_values[i-287:i,0]))
                EPS_max = np.max(EPS_values[i-287:i,0])
                EPS_events_electron = np.vstack((EPS_events_electron, [(str(int(i/287))+months[b]+'2004'), EPS_avg, EPS_max]))
                event_counter_electron = 0
            if i % 287 == 0 and event_counter_proton > 0 and i !=0:
                EPS_avg = np.round(np.mean(EPS_values[i-287:i,1]))
                EPS_max = np.max(EPS_values[i-287:i,1])
                EPS_events_proton = np.vstack((EPS_events_proton, [(str(int(i/287))+months[b]+'2004'), EPS_avg, EPS_max]))
                event_counter_proton = 0
            if EPS_values[i,0] > 1E+05:
                event_counter_electron += 1
            if EPS_values[i,1] > 1E+04:
                event_counter_proton += 1

EPS_events_electron = np.delete(EPS_events_electron, 0, axis=0)
EPS_events_proton = np.delete(EPS_events_proton, 0, axis=0)
print(EPS_events_proton)

"""
#electron_flux = EPS_values[:,0][EPS_values[:,0] > 0]
#time = range(len(electron_flux))
#plt.plot(time, electron_flux)
"""
#------Electron plot---------------------------------------
plt.subplots_adjust(hspace=0.5)
plt.rcParams['font.size'] = '15'
ax = plt.subplot(2,1,1)
electron_flux = EPS_2004[:,0][EPS_2004[:,0] > 0]
time = range(len(electron_flux))
plt.plot(time, electron_flux)
ax.set_title('Electron flux >2Mev')
ax.set_xticks(list(range(0,103680,8640)))
ax.set_xticklabels(months)
#ax.set_yticklabels(["{:.2e}".format(t) for t in ax.get_yticks()])
plt.xlabel('Month',labelpad=15)
plt.ylabel('Particles / cm^2 s^1 sr^1', labelpad=15)

#------------Proton plot-----------------------------------

plt.rcParams['font.size'] = '15'
ax = plt.subplot(2,1,2)
proton_flux = EPS_2004[:,1][EPS_2004[:,1] > 0]
time = range(len(proton_flux))
plt.plot(time, proton_flux)
ax.set_title('Proton flux 0.6MeV - 4.0MeV')
ax.set_xticks(list(range(0,103680,8640)))
ax.set_xticklabels(months)
#ax.set_yticklabels(["{:.2e}".format(t) for t in ax.get_yticks()])
plt.xlabel('Month',labelpad=15)
plt.ylabel('Particles / cm^2 s^1 sr^1', labelpad=15)
plt.show()