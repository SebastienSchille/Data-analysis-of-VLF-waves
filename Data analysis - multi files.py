import numpy as np
from matplotlib import pyplot as plt

#Initialising varriables
num_of_files = 9
counter = 0
i = 1

#Setting a general font size for matplotlib
plt.rcParams['font.size'] = '14'

while i < (num_of_files+1):
    file_name = 'DHO2014060' + str(i) + '.txt'
    vlf_data = np.genfromtxt(file_name, dtype=float, comments='%')

    #Calculating the magnitude of the amplitude and phase
    vlf_data_amplitutde = ((vlf_data[:,1]**2)+(vlf_data[:,2]**2))**0.5
    vlf_data_phase = ((vlf_data[:,3]**2)+(vlf_data[:,2]**4))**0.5

    #Converting magnitude to decibels
    vlf_data_amplitutde_db = (20*np.log(vlf_data_amplitutde))
    vlf_data_phase_db = (20*np.log(vlf_data_phase))
    
    #Storring the proccesed values into their respective arrays
    if i == 1:
        vlf_data_times = vlf_data[:,0]
        vlf_data_amps = vlf_data_amplitutde_db
        vlf_data_phases = vlf_data_phase_db

    else:
        vlf_data_times = np.column_stack((vlf_data_times,vlf_data[:,0]))
        vlf_data_amps = np.column_stack((vlf_data_amps,vlf_data_amplitutde_db))
        vlf_data_phases = np.column_stack((vlf_data_phases,vlf_data_phase_db))
    
    i = i+1


#Calculating the signal average
amplitude_avg = np.mean(vlf_data_amps, axis = 1)
phase_avg = np.mean(vlf_data_phases, axis = 1)


for i in range(num_of_files):
    #Asigning variables to plot
    time = vlf_data_times[:,i]/3600
    amplitude = vlf_data_amps[:,i]
    phase = vlf_data_phases[:,i]
    
    #Setting a general font size for matplotlib
    plt.rcParams['font.size'] = '14'

    #Graphing parameters
    x = i + 1
    ax = plt.subplot(3,3,x)
    plt.plot(time, amplitude, color='blue')
    plt.plot(time, amplitude_avg, linestyle='--', color='red')
    plt.xlim([0,24])
    ax.set_xticks(list(range(0,25,2)))
    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    plt.xlabel('Time UTC')
    plt.ylabel('Magnitude (db)')

plt.show()

"""
def plot(a,b):
    counter = 0
    plt.figure()
    for i in range(a,b):
        #Asigning variable to plot
        time = vlf_data_times[:,i]/3600
        amplitude = vlf_data_amps[:,i]
        phase = vlf_data_phases[:,i]

        counter = counter + 1
        ax = plt.subplot(2,2,counter)
        plt.plot(time, amplitude, color='blue')
        plt.plot(time, amplitude_avg, linestyle='--', color='red')
        plt.xlim([0,24])
        ax.set_xticks(list(range(0,25,2)))
        plt.xlabel('Time UTC')
        plt.ylabel('Magnitude (db)')

plot(0,4)
plot(4,8)
plot(8,9)
"""





  