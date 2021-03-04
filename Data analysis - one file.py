import numpy as np
from matplotlib import pyplot as plt

#Creating a numpy array from the text file
vlf_data = np.genfromtxt('DHO20140601.txt', dtype=float, comments='%')

#Calculating the magnitude of the amplitude and phase
vlf_data_amplitutde = ((vlf_data[:,1]**2)+(vlf_data[:,2]**2))**0.5
vlf_data_phase = ((vlf_data[:,3]**2)+(vlf_data[:,2]**4))**0.5

#Converting magnitude to decibels
vlf_data_amplitutde_db = (20*np.log(vlf_data_amplitutde))
vlf_data_phase_db = (20*np.log(vlf_data_phase))

#Creating a new numpy array with the calculated data
vlf_data_mag = np.column_stack((vlf_data[:,0],vlf_data_amplitutde_db,vlf_data_phase_db))

#Asigning variables to plot
time = vlf_data_mag[:,0]/3600
amplitude = vlf_data_mag[:,1]
phase = vlf_data_mag[:,2]

#Setting a general font size for matplotlib
plt.rcParams['font.size'] = '16'

#Graphing subplot 1
ax = plt.subplot(1,2,1)
plt.plot(time, amplitude, color='blue')
plt.xlim([0,24])
ax.set_xticks(list(range(0,25,2)))
plt.title('Amplitude')
plt.xlabel('Time UTC')
plt.ylabel('Magnitude (db)')

#Setting axis font size for subplot 1
for label in ax.get_xticklabels():
	label.set_fontsize(16)

#Graphing subplot 2
ax_1 = plt.subplot(1,2,2)
plt.plot(time, phase, color='red')
plt.xlim([0,24])
ax_1.set_xticks(list(range(0,25,2)))
plt.title('Phase')
plt.xlabel('Time UTC')
plt.ylabel('Magnitude (db)')

#Setting axis font size for subplot 2
for label in ax_1.get_xticklabels():
	label.set_fontsize(16)

plt.show()