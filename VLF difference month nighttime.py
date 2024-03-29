import numpy as np
from matplotlib import pyplot as plt
import os
from Nighttime_UTC import nighttime_2004, nighttime_2005, nighttime_2006, nighttime_2007

os.chdir("./VLF Data raw")
months_len_day = [31,28,31,30,31,30,31,31,30,31,30,31]
months_len_day_2004 = [31,29,31,30,31,30,31,31,30,31,30,31]
months_len = np.array([0,31,59,90,120,151,181,212,243,273,304,334])
months_len_2004 = np.array([0,31,60,91,121,152,182,213,244,274,305,335])
months = ['JAN','FEB','MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
vlf_data_avg = np.empty(8)

def average (day, month, bmonth, bmonth_len, year, station_amp, station_phase):
    for i in range((day-5), day+1):
        if i < 1: #Load data
            amp = np.genfromtxt(f'T{bmonth_len+i}{bmonth}{year}A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T{bmonth_len+i}{bmonth}{year}A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        elif i > 0 and i < 10: #Load data
            amp = np.genfromtxt(f'T0{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T0{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        else: #Load data
            amp = np.genfromtxt(f'T{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        #if i==7 or i==8 or i==9 or i==10: #Ignore non quiet days
        #       amp[amp != float('nan')] = float('nan')
        #       phase[phase != float('nan')] = float('nan')
        if i == (day-5): #Initialisation of the first array element
            vlf_amp = amp
            vlf_phase = phase
        else: #Additionally days added to the array
            vlf_amp = np.column_stack((vlf_amp, amp))
            vlf_phase = np.column_stack((vlf_phase, phase))
    vlf_amp[vlf_amp == 0] = float('nan') #Zero values neglected
    vlf_phase[vlf_phase == 0] = float('nan')
    vlf_amp_avg = np.nanmean(vlf_amp, axis=1) #Average calculated
    vlf_phase_avg = np.nanmean(vlf_phase, axis=1)
    return vlf_amp_avg, vlf_phase_avg

def difference (month, month_len, bmonth, bmonth_len, year, station_amp, station_phase, loc):
    x_axis= [0]
    for i in range(1,(month_len+1)):
        if i < 10: #Load data
            amp = np.genfromtxt(f'T0{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T0{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        else: #Load data
            amp = np.genfromtxt(f'T{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_amp))
            phase = np.genfromtxt(f'T{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        amp[amp == 0] = float('nan') #Zero values neglected
        phase[phase == 0] = float('nan')
        vlf_amp_avg, vlf_phase_avg = average(i, month, bmonth, bmonth_len, year, station_amp, station_phase) #Calling the average function for a single day
        amp_diff = amp - vlf_amp_avg #The signal difference calculated
        phase_diff = phase - vlf_phase_avg
        #nighttime-------------------------
        start = nighttime_2006[loc+i,0]
        end = nighttime_2006[loc+i,1]
        delete_rows1 = list(range(int(end), 4320))
        delete_rows2 = list(range(0, int(start)))
        amp_diff = np.delete(amp_diff, delete_rows1, axis=0)
        amp_diff = np.delete(amp_diff, delete_rows2, axis=0)
        phase_diff = np.delete(phase_diff, delete_rows1, axis=0)
        phase_diff = np.delete(phase_diff, delete_rows2, axis=0)
        x_axis.append(len(amp_diff))
        if i == 1: #Initialisation of the first array element
            vlf_amp_diff = amp_diff
            vlf_phase_diff = phase_diff
        else: #Additionally days added to the array
            vlf_amp_diff = np.append(vlf_amp_diff, amp_diff)
            vlf_phase_diff = np.append(vlf_phase_diff, phase_diff)
    x_axis = np.cumsum(x_axis)
    x_axis = x_axis[0:len(x_axis):2]
    return vlf_amp_diff, vlf_phase_diff, x_axis

def std (vlf_amp_night, vlf_phase_night):
    vlf_amp_std = np.nanstd(vlf_amp_night)*2
    vlf_phase_std = np.nanstd(vlf_phase_night)*2
    return vlf_amp_std, vlf_phase_std

#-------------------Main code-----------------------------------------------------

vlf_amp_diff_NWC, vlf_phase_diff_NWC, x_axis_NWC = difference(months[10], months_len_day[10], months[9], months_len_day[9],6,0,1, months_len_2004[10]-1)
vlf_amp_std_NWC, vlf_phase_std_NWC = std(vlf_amp_diff_NWC, vlf_phase_diff_NWC)
vlf_amp_diff_JJI, vlf_phase_diff_JJI, x_axis_JJI = difference(months[10], months_len_day[10], months[9], months_len_day[9],6,4,5, months_len_2004[10]-1)
vlf_amp_std_JJI, vlf_phase_std_JJI = std(vlf_amp_diff_JJI, vlf_phase_diff_JJI)
vlf_amp_diff_JJY, vlf_phase_diff_JJY, x_axis_JJY = difference(months[10], months_len_day[10], months[9], months_len_day[9],6,6,7, months_len_2004[10]-1)
vlf_amp_std_JJY, vlf_phase_std_JJY = std(vlf_amp_diff_JJY, vlf_phase_diff_JJY)

#------------------------Magnitude plot difference-------------------------------------------

#Setting a general font size for matplotlib
plt.rcParams['font.size'] = '18'
plt.subplots_adjust(hspace=0.4)

#Graphing parameters
time = range(len(vlf_amp_diff_NWC))
std_amp_NWC = np.array([])
for i in range(len(time)):
    std_amp_NWC = np.append(std_amp_NWC, vlf_amp_std_NWC)
ax = plt.subplot(3,1,1)
plt.plot(time, vlf_amp_diff_NWC, color='blue')
plt.plot(time, std_amp_NWC, linestyle='--', color='red')
plt.plot(time, (std_amp_NWC-(2*std_amp_NWC)), linestyle='--', color='red')
ax.set_title('VLF dA NWC-PTK')
ax.set_xticks(x_axis_NWC)
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
#plt.xlabel('Month', labelpad=10)
plt.ylabel('dB', labelpad=10)

#Graphing parameters
time = range(len(vlf_amp_diff_JJI))
std_amp_JJI = np.array([])
for i in range(len(time)):
    std_amp_JJI = np.append(std_amp_JJI, vlf_amp_std_JJI)
ax = plt.subplot(3,1,2)
plt.plot(time, vlf_amp_diff_JJI, color='blue')
plt.plot(time, std_amp_JJI, linestyle='--', color='red')
plt.plot(time, (std_amp_JJI-(2*std_amp_JJI)), linestyle='--', color='red')
ax.set_title('VLF dA JJI-PTK')
ax.set_xticks(x_axis_JJI)
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
#plt.xlabel('Month', labelpad=10)
plt.ylabel('dB', labelpad=10)

#Graphing parameters
time = range(len(vlf_amp_diff_JJY))
std_amp_JJY = np.array([])
for i in range(len(time)):
    std_amp_JJY = np.append(std_amp_JJY, vlf_amp_std_JJY)
ax = plt.subplot(3,1,3)
plt.plot(time, vlf_amp_diff_JJY, color='blue')
plt.plot(time, std_amp_JJY, linestyle='--', color='red')
plt.plot(time, (std_amp_JJY-(2*std_amp_JJY)), linestyle='--', color='red')
ax.set_title('VLF dA JJY-PTK')
ax.set_xticks(x_axis_JJY)
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Day', labelpad=10)
plt.ylabel('dB', labelpad=10)
plt.show()

#------------------------Phase plot difference-------------------------------------------
#Setting a general font size for matplotlib
plt.rcParams['font.size'] = '18'
plt.subplots_adjust(hspace=0.4)

#Graphing parameters
time = range(len(vlf_amp_diff_NWC))
std_phase_NWC = np.array([])
for i in range(len(time)):
    std_phase_NWC = np.append(std_phase_NWC, vlf_phase_std_NWC)
ax = plt.subplot(3,1,1)
plt.plot(time, vlf_phase_diff_NWC, color='blue')
plt.plot(time, std_phase_NWC, linestyle='--', color='red')
plt.plot(time, (std_phase_NWC-(2*std_phase_NWC)), linestyle='--', color='red')
ax.set_title('VLF dP NWC-PTK')
ax.set_xticks(x_axis_NWC)
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
#plt.xlabel('Month', labelpad=10)
plt.ylabel('dgr', labelpad=10)

#Graphing parameters
time = range(len(vlf_amp_diff_JJI))
std_phase_JJI = np.array([])
for i in range(len(time)):
    std_phase_JJI = np.append(std_phase_JJI, vlf_phase_std_JJI)
ax = plt.subplot(3,1,2)
plt.plot(time, vlf_phase_diff_JJI, color='blue')
plt.plot(time, std_phase_JJI, linestyle='--', color='red')
plt.plot(time, (std_phase_JJI-(2*std_phase_JJI)), linestyle='--', color='red')
ax.set_title('VLF dP JJI-PTK')
ax.set_xticks(x_axis_JJI)
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
#plt.xlabel('Month', labelpad=10)
plt.ylabel('dgr', labelpad=10)

#Graphing parameters
time = range(len(vlf_amp_diff_JJY))
std_phase_JJY = np.array([])
for i in range(len(time)):
    std_phase_JJY = np.append(std_phase_JJY, vlf_phase_std_JJY)
ax = plt.subplot(3,1,3)
plt.plot(time, vlf_phase_diff_JJY, color='blue')
plt.plot(time, std_phase_JJY, linestyle='--', color='red')
plt.plot(time, (std_phase_JJY-(2*std_phase_JJY)), linestyle='--', color='red')
ax.set_title('VLF dP JJY-PTK')
ax.set_xticks(x_axis_JJY)
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24','26','28','30'])
plt.xlabel('Day', labelpad=10)
plt.ylabel('dgr', labelpad=10)
plt.show()