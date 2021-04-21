import numpy as np
from matplotlib import pyplot as plt
import os
from VLF_Data_nighttime import daylight_times

os.chdir("./VLF Data raw")
months_len_day = [31,29,31,30,31,30,31,31,30,31,30,31]
months_len = np.array([0,31,59,90,120,151,181,212,243,273,304,334])
months_len_2004 = np.array([0,31,60,91,121,152,182,213,244,274,305,335])
months = ['JAN','FEB','MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
vlf_data_avg = np.empty(8)

def raw (month, year, station_amp, station_phase):
    for i in range(1,31):
        if i > 0 and i < 10:
            amp = np.genfromtxt(f'T0{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T0{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        else:
            amp = np.genfromtxt(f'T{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        if i == 1:
            vlf_amp_month = amp
            vlf_phase_month = phase
        else:
            vlf_amp_month = np.append(vlf_amp_month, amp)
            vlf_phase_month = np.append(vlf_phase_month, phase)
    vlf_amp_month[vlf_amp_month == 0] = float('nan')
    vlf_phase_month[vlf_phase_month == 211.00] = float('nan')
    return vlf_amp_month, vlf_phase_month
    

def average (station_amp, station_phase):
    for a in range(1,31):
        for i in range((a-5), a+1):
            if i != 7 or i != 8 or i != 9:
                if i < 1:
                    amp = np.genfromtxt(f'T{31+i}OCT4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
                    phase = np.genfromtxt(f'T{31+i}OCT4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
                elif i > 0 and i < 10:
                    amp = np.genfromtxt(f'T0{i}NOV4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
                    phase = np.genfromtxt(f'T0{i}NOV4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
                elif i > 30:
                    amp = np.genfromtxt(f'T0{i-30}DEC4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
                    phase = np.genfromtxt(f'T0{i-30}DEC4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
                else:
                    amp = np.genfromtxt(f'T{i}NOV4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
                    phase = np.genfromtxt(f'T{i}NOV4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
                if i==6 or i == 7 or i == 8 or i == 9:
                    amp[amp != float('nan')] = float('nan')
                    phase[phase != float('nan')] = float('nan')
                    print(amp)
                if i == (a-5):
                    vlf_amp = amp
                    vlf_phase = phase
                else:
                    vlf_amp = np.column_stack((vlf_amp, amp))
                    vlf_phase = np.column_stack((vlf_phase, phase))
        vlf_amp[vlf_amp == 0] = float('nan')
        vlf_phase[vlf_phase == 211.00] = float('nan')
        vlf_amp_a = np.nanmean(vlf_amp, axis=1)
        vlf_phase_a = np.nanmean(vlf_phase, axis=1)
        if a == 1:
            vlf_amp_avg = vlf_amp_a
            vlf_phase_avg = vlf_phase_a
        else:
            vlf_amp_avg = np.append(vlf_amp_avg, vlf_amp_a)
            vlf_phase_avg = np.append(vlf_phase_avg, vlf_phase_a)
    return vlf_amp_avg, vlf_phase_avg

#---------------Main code (Raw signal)-------------------------------------

# NWC (0,1) JJI (4,5) JJY(6,7)
vlf_amp_month_NWC, vlf_phase_month_NWC = raw('NOV', 4, 0, 1)
vlf_amp_month_JJI, vlf_phase_month_JJI = raw('NOV', 4, 4, 5) 
vlf_amp_month_JJY, vlf_phase_month_JJY = raw('NOV', 4, 6, 7) 

#------------Month plot (Raw signal)-----------------------------------
"""
#Asigning variables to plot
time = range(len(vlf_amp_month))

#Setting a general font size for matplotlib
plt.rcParams['font.size'] = '18'
plt.subplots_adjust(wspace=0.3, hspace=0.3)

#Graphing parameters
ax = plt.subplot(1,1,1)
plt.plot(time, vlf_amp_month, color='blue')
#plt.plot(time, vlf_phase_month, color='blue')
ax.set_title('VLF month')
ax.set_xticks(list(range(0,133920,8640)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Month')
plt.ylabel('Magnitude')
plt.show()
"""
#----------------Main code (Raw + average)------------------------

# NWC (0,1) JJI (4,5) JJY(6,7)
vlf_amp_avg_NWC, vlf_phase_avg_NWC = average(0,1)
vlf_amp_avg_JJI, vlf_phase_avg_JJI = average(4,5) 
vlf_amp_avg_JJY, vlf_phase_avg_JJY = average(6,7)  

#------------Amplitude plot (Raw + average signal)-----------------------------------

#Asigning variables to plot
time = range(len(vlf_amp_month_NWC))

#Setting a general font size for matplotlib
plt.rcParams['font.size'] = '18'
plt.subplots_adjust(hspace=0.6)

#Graphing parameters
ax = plt.subplot(3,1,1)
plt.plot(time, vlf_amp_month_NWC, color='blue')
plt.plot(time, vlf_amp_avg_NWC, linestyle='--', color='red')
#plt.plot(time, vlf_phase_month, color='blue')
#plt.plot(time, vlf_phase_avg, linestyle='--', color='red')
ax.set_title('VLF month NWC-PTK')
ax.set_xticks(list(range(0,133920,8640)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Day', labelpad=10)
plt.ylabel('Magnitude', labelpad=10)

#Graphing parameters
ax = plt.subplot(3,1,2)
plt.plot(time, vlf_amp_month_JJI, color='blue')
plt.plot(time, vlf_amp_avg_JJI, linestyle='--', color='red')
#plt.plot(time, vlf_phase_month, color='blue')
#plt.plot(time, vlf_phase_avg, linestyle='--', color='red')
ax.set_title('VLF month JJI-PTK')
ax.set_xticks(list(range(0,133920,8640)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Day', labelpad=10)
plt.ylabel('Magnitude', labelpad=10)

#Graphing parameters
ax = plt.subplot(3,1,3)
plt.plot(time, vlf_amp_month_JJY, color='blue')
plt.plot(time, vlf_amp_avg_JJY, linestyle='--', color='red')
#plt.plot(time, vlf_phase_month, color='blue')
#plt.plot(time, vlf_phase_avg, linestyle='--', color='red')
ax.set_title('VLF month JJY-PTK')
ax.set_xticks(list(range(0,133920,8640)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Day', labelpad=10)
plt.ylabel('Magnitude', labelpad=10)
plt.show()

#------------Phase plot (Raw + average signal)-----------------------------------

#Asigning variables to plot
time = range(len(vlf_amp_month_NWC))

#Setting a general font size for matplotlib
plt.rcParams['font.size'] = '18'
plt.subplots_adjust(hspace=0.6)

#Graphing parameters
ax = plt.subplot(3,1,1)
plt.plot(time, vlf_phase_month_NWC, color='blue')
plt.plot(time, vlf_phase_avg_NWC, linestyle='--', color='red')
ax.set_title('VLF month NWC-PTK')
ax.set_xticks(list(range(0,133920,8640)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Degrees', labelpad=10)
plt.ylabel('Magnitude', labelpad=10)

#Graphing parameters
ax = plt.subplot(3,1,2)
plt.plot(time, vlf_phase_month_JJI, color='blue')
plt.plot(time, vlf_phase_avg_JJI, linestyle='--', color='red')
ax.set_title('VLF month JJI-PTK')
ax.set_xticks(list(range(0,133920,8640)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Day', labelpad=10)
plt.ylabel('Degrees', labelpad=10)

#Graphing parameters
ax = plt.subplot(3,1,3)
plt.plot(time, vlf_phase_month_JJY, color='blue')
plt.plot(time, vlf_phase_avg_JJY, linestyle='--', color='red')
ax.set_title('VLF month JJY-PTK')
ax.set_xticks(list(range(0,133920,8640)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Day', labelpad=10)
plt.ylabel('Degrees', labelpad=10)
plt.show()

