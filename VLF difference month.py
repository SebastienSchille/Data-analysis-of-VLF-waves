import numpy as np
from matplotlib import pyplot as plt
import os

os.chdir("./VLF Data raw")
months_len_day = [31,28,31,30,31,30,31,31,30,31,30,31]
months_len_day_2004 = [31,29,31,30,31,30,31,31,30,31,30,31]
months_len = np.array([0,31,59,90,120,151,181,212,243,273,304,334])
months_len_2004 = np.array([0,31,60,91,121,152,182,213,244,274,305,335])
months = ['JAN','FEB','MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
vlf_data_avg = np.empty(8)

def average (day, month, bmonth, bmonth_len, year, station_amp, station_phase):
    for i in range((day-5), day+1):
        if i < 1:
            amp = np.genfromtxt(f'T{bmonth_len+i}{bmonth}{year}A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T{bmonth_len+i}{bmonth}{year}A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        elif i > 0 and i < 10:
            amp = np.genfromtxt(f'T0{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T0{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        else:
            amp = np.genfromtxt(f'T{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        if i == (day-5):
            vlf_amp = amp
            vlf_phase = phase
        else:
            vlf_amp = np.column_stack((vlf_amp, amp))
            vlf_phase = np.column_stack((vlf_phase, phase))
    vlf_amp[vlf_amp == 0] = float('nan')
    vlf_phase[vlf_phase == 211.00] = float('nan')
    vlf_amp_avg = np.nanmean(vlf_amp, axis=1)
    vlf_phase_avg = np.nanmean(vlf_phase, axis=1)
    return vlf_amp_avg, vlf_phase_avg

def difference (month, month_len, bmonth, bmonth_len, year, station_amp, station_phase):
    x_axis= [0]
    for i in range(1,(month_len+1)):
        if i < 10:
            amp = np.genfromtxt(f'T0{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T0{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        else:
            amp = np.genfromtxt(f'T{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        amp[amp == 0] = float('nan')
        phase[phase == 211.00] = float('nan')
        vlf_amp_avg, vlf_phase_avg = average(i, month, bmonth, bmonth_len, year, station_amp, station_phase)
        amp_diff = amp - vlf_amp_avg
        phase_diff = phase - vlf_phase_avg
        if i == 1:
            vlf_amp_diff = amp_diff
            vlf_phase_diff = phase_diff
        else:
            vlf_amp_diff = np.append(vlf_amp_diff, amp_diff)
            vlf_phase_diff = np.append(vlf_phase_diff, phase_diff)
    x_axis = np.cumsum(x_axis)
    return vlf_amp_diff, vlf_phase_diff, x_axis

def std (vlf_amp_night, vlf_phase_night):
    vlf_amp_std = np.nanstd(vlf_amp_night)*2
    vlf_phase_std = np.nanstd(vlf_phase_night)*2
    return vlf_amp_std, vlf_phase_std

#-------------------Main code-----------------------------------------------------

vlf_amp_diff_NWC, vlf_phase_diff_NWC, x_axis_NWC = difference(months[10], months_len_day_2004[10], months[9], months_len_day_2004[9], 4, 0, 1)
vlf_amp_diff_JJI, vlf_phase_diff_JJI, x_axis_JJI = difference(months[10], months_len_day_2004[10], months[9], months_len_day_2004[9], 4, 4, 5)
vlf_amp_diff_JJY, vlf_phase_diff_JJY, x_axis_JJY = difference(months[10], months_len_day_2004[10], months[9], months_len_day_2004[9], 4, 6, 7)

#------------------------Magnitude plot difference-------------------------------------------

#Asigning variables to plot
time = range(len(vlf_amp_diff_NWC))

#Setting a general font size for matplotlib
plt.rcParams['font.size'] = '18'
plt.subplots_adjust(hspace=0.6)

#Graphing parameters
ax = plt.subplot(3,1,1)
plt.plot(time, vlf_amp_diff_NWC, color='blue')
ax.set_title('VLF month NWC-PTK')
ax.set_xticks(list(range(0,133920,8640)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Month', labelpad=10)
plt.ylabel('Magnitude', labelpad=10)

#Graphing parameters
ax = plt.subplot(3,1,2)
plt.plot(time, vlf_amp_diff_JJI, color='blue')
ax.set_title('VLF month JJI-PTK')
ax.set_xticks(list(range(0,133920,8640)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Month', labelpad=10)
plt.ylabel('Magnitude', labelpad=10)

#Graphing parameters
ax = plt.subplot(3,1,3)
plt.plot(time, vlf_amp_diff_JJY, color='blue')
ax.set_title('VLF month JJY-PTK')
ax.set_xticks(list(range(0,133920,8640)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Month', labelpad=10)
plt.ylabel('Magnitude', labelpad=10)
plt.show()

#------------------------Phase plot difference-------------------------------------------

#Asigning variables to plot
time = range(len(vlf_amp_diff_NWC))

#Setting a general font size for matplotlib
plt.rcParams['font.size'] = '18'
plt.subplots_adjust(wspace=0.3, hspace=0.3)

#Graphing parameters
ax = plt.subplot(3,1,1)
plt.plot(time, vlf_phase_diff_NWC, color='blue')
ax.set_title('VLF month NWC-PTK')
ax.set_xticks(list(range(0,133920,8640)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Days', labelpad=10)
plt.ylabel('Degrees', labelpad=10)

#Graphing parameters
ax = plt.subplot(3,1,2)
plt.plot(time, vlf_phase_diff_JJI, color='blue')
ax.set_title('VLF month JJI-PTK')
ax.set_xticks(list(range(0,133920,8640)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Days', labelpad=10)
plt.ylabel('Degrees', labelpad=10)

#Graphing parameters
ax = plt.subplot(3,1,3)
plt.plot(time, vlf_phase_diff_JJY, color='blue')
ax.set_title('VLF month JJY-PTK')
ax.set_xticks(list(range(0,133920,8640)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Days', labelpad=10)
plt.ylabel('Degrees', labelpad=10)
plt.show()