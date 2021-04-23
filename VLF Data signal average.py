import numpy as np
from matplotlib import pyplot as plt
import os
#from Nighttime_UTC import nighttime_times

os.chdir("./VLF Data Raw")
months_len = np.array([0,31,59,90,120,151,181,212,243,273,304,334])
months_len_2004 = np.array([0,31,60,91,121,152,182,213,244,274,305,335])
vlf_data_avg = np.empty(8)

def init_average (day, station_amp, station_phase):
    for i in range((day-5), day+5):
        amp = np.genfromtxt(f'T{i}FEB4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
        phase = np.genfromtxt(f'T{i}FEB4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        if i == (day-5):
            vlf_amp = amp
            vlf_phase = phase
        else:
            vlf_amp = np.column_stack((vlf_amp, amp))
            vlf_phase = np.column_stack((vlf_phase, phase))
    vlf_amp_avg = np.mean(vlf_amp, axis=1)
    vlf_phase_avg = np.mean(vlf_phase, axis=1)
    return vlf_amp_avg, vlf_phase_avg

def average (day, station_amp, station_phase):
    for i in range((day-5), day+1):
        if i < 1:
            amp = np.genfromtxt(f'T{30+i}JUN4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T{30+i}JUN4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        elif i > 0 and i < 10:
            amp = np.genfromtxt(f'T0{i}JUL4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T0{i}JUL4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        else:
            amp = np.genfromtxt(f'T{i}JUL4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T{i}JUL4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        if i == (day-5):
            vlf_amp = amp
            vlf_phase = phase
        else:
            vlf_amp = np.column_stack((vlf_amp, amp))
            vlf_phase = np.column_stack((vlf_phase, phase))
    vlf_amp_avg = np.mean(vlf_amp, axis=1)
    vlf_phase_avg = np.mean(vlf_phase, axis=1)
    return vlf_amp_avg, vlf_phase_avg, amp, phase

def init_difference (vlf_amp_diff, vlf_phase_diff, day, loc, station_amp, station_phase, counter):
    amp = np.genfromtxt(f'T{day}OCT5A.kam', dtype=float, skip_header=1, usecols=(station_amp))
    phase = np.genfromtxt(f'T{day}OCT5A.kam', dtype=float, skip_header=1, usecols=(station_phase))
    vlf_amp_avg, vlf_phase_avg = init_average(day, station_amp, station_phase)
    amp_diff = amp - vlf_amp_avg
    phase_diff = phase - vlf_phase_avg
    if counter == 0:
        vlf_amp_diff = amp_diff
        vlf_phase_diff = phase_diff
    else:
        vlf_amp_diff = np.column_stack((vlf_amp_diff, amp_diff))
        vlf_phase_diff = np.column_stack((vlf_phase_diff, phase_diff))
    return vlf_amp_diff, vlf_phase_diff

def difference (vlf_amp_diff, vlf_phase_diff, day, loc, station_amp, station_phase):
    vlf_amp_diff = np.delete(vlf_amp_diff, 0, axis=1)
    vlf_phase_diff = np.delete(vlf_phase_diff, 0, axis=1)
    print(day)
    if day < 10:
        amp = np.genfromtxt(f'T0{day}NOV5A.kam', dtype=float, skip_header=1, usecols=(station_amp))
        phase = np.genfromtxt(f'T0{day}NOV5A.kam', dtype=float, skip_header=1, usecols=(station_phase))
    else:
        amp = np.genfromtxt(f'T{day}NOV5A.kam', dtype=float, skip_header=1, usecols=(station_amp))
        phase = np.genfromtxt(f'T{day}NOV5A.kam', dtype=float, skip_header=1, usecols=(station_phase))
    vlf_amp_avg, vlf_phase_avg = average(day, station_amp, station_phase)
    amp_diff = amp - vlf_amp_avg
    phase_diff = phase - vlf_phase_avg
    vlf_amp_diff = np.column_stack((vlf_amp_diff, amp_diff))
    vlf_phase_diff = np.column_stack((vlf_phase_diff, phase_diff))
    return vlf_amp_diff, vlf_phase_diff

def std (vlf_amp_night, vlf_phase_night):
    vlf_amp_std = np.std(vlf_amp_night)
    vlf_phase_std = np.std(vlf_phase_night)
    return vlf_amp_std, vlf_phase_std

def nighttime (vlf_amp_diff, vlf_phase_diff, loc):
    if daylight_times[loc-6,0] < daylight_times[loc,0]:
        start = daylight_times[loc-6,0]
    else:
        start = daylight_times[loc,0]
    if daylight_times[loc-6,1] > daylight_times[loc,1]:
        end = daylight_times[loc-6,1]
    elif daylight_times[loc-6,1] == 0:
        end = daylight_times[loc-6,1]
    elif daylight_times[loc,1] == 0:
        end = daylight_times[loc,1]
    else:
        end = daylight_times[loc,1]
    
    delete_rows = list(range(int(start), int(end)))
    vlf_amp_diff = np.delete(vlf_amp_diff, delete_rows, axis=0)
    vlf_data_avg = np.delete(vlf_phase_diff, delete_rows, axis=0)
    return vlf_amp_diff, vlf_phase_diff

#------------------------------------------------
vlf_amp_diff = np.array([])
vlf_phase_diff = np.array([])
loc_oct = 273
loc_nov = 304
counter = 0

avg_amp_NWC, avg_phase_NWC, amp_NWC, phase_NWC = average(1, 0, 1)
avg_amp_JJI, avg_phase_JJI, amp_JJI, phase_JJI = average(1, 4, 5)
avg_amp_JJY, avg_phase_JJY, amp_JJY, phase_JJY = average(1, 6, 7)




#----------------------------------------------------

#Asigning variables to plot
time = range(np.shape(avg_amp_NWC)[0])

#Setting a general font size for matplotlib
plt.rcParams['font.size'] = '15'
plt.subplots_adjust(wspace=0.3, hspace=0.3)

#Graphing parameters
ax = plt.subplot(2,3,1)
plt.plot(time, amp_NWC, color='blue')
plt.plot(time, avg_amp_NWC, linestyle='--', color='red')
ax.set_title('NWC-PTK')
ax.set_xticks(list(range(0,4500,360)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24'])
plt.xlabel('Time UTC+12')
plt.ylabel('Magnitude')

ax = plt.subplot(2,3,2)
plt.plot(time, amp_JJI, color='blue')
plt.plot(time, avg_amp_JJI, linestyle='--', color='red')
ax.set_title('JJI-PTK')
#ax.set_xticks(list(range(0,4500,360)))
#ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24'])
plt.xlabel('Time UTC+12')
plt.ylabel('Magnitude')

ax = plt.subplot(2,3,3)
plt.plot(time, amp_JJY, color='blue')
plt.plot(time, avg_amp_JJY, linestyle='--', color='red')
ax.set_title('JJY-PTK')
ax.set_xticks(list(range(0,4500,360)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24'])
plt.xlabel('Time UTC+12')
plt.ylabel('Magnitude')

ax = plt.subplot(2,3,4)
plt.plot(time, phase_NWC, color='blue')
plt.plot(time, avg_phase_NWC, linestyle='--', color='red')
ax.set_title('NWC-PTK')
ax.set_xticks(list(range(0,4500,360)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24'])
plt.xlabel('Time UTC+12')
plt.ylabel('Phase (deg)')

ax = plt.subplot(2,3,5)
plt.plot(time, phase_JJI, color='blue')
plt.plot(time, avg_phase_JJI, linestyle='--', color='red')
ax.set_title('JJI-PTK')
ax.set_xticks(list(range(0,4500,360)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24'])
plt.xlabel('Time UTC+12')
plt.ylabel('Phase (deg)')

ax = plt.subplot(2,3,6)
plt.plot(time, phase_JJY, color='blue')
plt.plot(time, avg_phase_JJY, linestyle='--', color='red')
ax.set_title('JJY-PTK')
ax.set_xticks(list(range(0,4500,360)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24'])
plt.xlabel('Time UTC+12')
plt.ylabel('Phase (deg)')

plt.show()


