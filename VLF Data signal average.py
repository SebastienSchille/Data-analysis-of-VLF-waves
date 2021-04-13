import numpy as np
from matplotlib import pyplot as plt
import os
from VLF_Data_nighttime import daylight_times

os.chdir("./VLF Data raw")
vlf_data_avg = np.empty(8)

def init_average (day, station_amp, station_phase):
    for i in range((day-5), day+1):
        amp = np.genfromtxt(f'T{i}OCT4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
        phase = np.genfromtxt(f'T{i}OCT4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
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
            amp = np.genfromtxt(f'T{31+i}OCT4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T{31+i}OCT4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        elif i > 0 and i < 10:
            amp = np.genfromtxt(f'T0{i}NOV4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T0{i}NOV4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        else:
            amp = np.genfromtxt(f'T{i}NOV4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T{i}NOV4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        if i == (day-5):
            vlf_amp = amp
            vlf_phase = phase
        else:
            vlf_amp = np.column_stack((vlf_amp, amp))
            vlf_phase = np.column_stack((vlf_phase, phase))
    vlf_amp_avg = np.mean(vlf_amp, axis=1)
    vlf_phase_avg = np.mean(vlf_phase, axis=1)
    return vlf_amp_avg, vlf_phase_avg

def init_difference (vlf_amp_diff, vlf_phase_diff, day, loc, station_amp, station_phase, counter):
    amp = np.genfromtxt(f'T{day}OCT4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
    phase = np.genfromtxt(f'T{day}OCT4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
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
        amp = np.genfromtxt(f'T0{day}NOV4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
        phase = np.genfromtxt(f'T0{day}NOV4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
    else:
        amp = np.genfromtxt(f'T{day}NOV4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
        phase = np.genfromtxt(f'T{day}NOV4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
    vlf_amp_avg, vlf_phase_avg = average(day, station_amp, station_phase)
    amp_diff = amp - vlf_amp_avg
    phase_diff = phase - vlf_phase_avg
    vlf_amp_diff = np.column_stack((vlf_amp_diff, amp_diff))
    vlf_phase_diff = np.column_stack((vlf_phase_diff, phase_diff))
    return vlf_amp_diff, vlf_phase_diff, vlf_amp_avg, amp

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
for i in range(25,32):
    vlf_amp_diff, vlf_phase_diff = init_difference(vlf_amp_diff, vlf_phase_diff, i, (loc_oct+i), 6, 7, counter)
    counter += 1

for i in range(1,27):
    vlf_amp_diff, vlf_phase_diff, vlf_amp_avg, amp = difference(vlf_amp_diff, vlf_phase_diff, i, (loc_nov+i), 6, 7)
    vlf_amp_night, vlf_phase_night = nighttime(vlf_amp_diff, vlf_phase_diff, (loc_nov+i))
    vlf_amp_std, vlf_phase_std = std(vlf_amp_night, vlf_phase_night)

#----------------------------------------------------

print(vlf_amp_diff)
print(np.shape(vlf_amp_diff))
print(vlf_amp_night)
print(np.shape(vlf_amp_night))
print(vlf_amp_std)
print(np.shape(vlf_amp_std))
print(np.min(vlf_amp_night[:,6]))
#np.savetxt('vlf_amp_night.txt', vlf_amp_night, delimiter=',')
print(daylight_times[323,0], daylight_times[323,1])

time = range(np.shape(vlf_amp_night)[0])
signal = amp
signal_diff = vlf_amp_night[:,6]
avg = vlf_amp_avg

#plt.plot(time, signal, color='blue')
#plt.plot(time, avg, linestyle='--', color='red')
plt.plot(time, signal_diff, color='blue')
plt.show()


