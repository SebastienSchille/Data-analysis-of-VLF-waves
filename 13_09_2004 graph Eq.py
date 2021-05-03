import numpy as np
from matplotlib import pyplot as plt
import os

os.chdir("./VLF Data raw")
months_len_day = [31,28,31,30,31,30,31,31,30,31,30,31]
months_len = np.array([0,31,59,90,120,151,181,212,243,273,304,334])
months_len_2004 = np.array([0,31,60,91,121,152,182,213,244,274,305,335])
months = ['JAN','FEB','MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
vlf_data_avg = np.empty(8)

def raw (month, month_len, year, station_amp, station_phase):
    for i in range(1,(month_len+1)):
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
    vlf_phase_month[vlf_phase_month == 0] = float('nan')
    return vlf_amp_month, vlf_phase_month
    

def average (month, month_len, bmonth, bmonth_len, year, station_amp, station_phase):
    for a in range(1,(month_len+1)):
        for i in range((a-5), a+1):
            if i < 1:
                amp = np.genfromtxt(f'T{bmonth_len+i}{bmonth}{year}A.kam', dtype=float, skip_header=1, usecols=(station_amp))
                phase = np.genfromtxt(f'T{bmonth_len+i}{bmonth}{year}A.kam', dtype=float, skip_header=1, usecols=(station_phase))
            elif i > 0 and i < 10:
                amp = np.genfromtxt(f'T0{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_amp))
                phase = np.genfromtxt(f'T0{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_phase))
            else:
                amp = np.genfromtxt(f'T{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_amp))
                phase = np.genfromtxt(f'T{i}{month}{year}A.kam', dtype=float, skip_header=1, usecols=(station_phase))
            if i == (a-5):
                vlf_amp = amp
                vlf_phase = phase
            else:
                vlf_amp = np.column_stack((vlf_amp, amp))
                vlf_phase = np.column_stack((vlf_phase, phase))
        vlf_amp[vlf_amp == 0] = float('nan')
        vlf_phase[vlf_phase == 0] = float('nan')
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
vlf_amp_month_NWC, vlf_phase_month_NWC = raw(months[8], months_len_day[8], 4, 0, 1)
vlf_amp_month_JJI, vlf_phase_month_JJI = raw(months[8], months_len_day[8], 4, 4, 5) 
vlf_amp_month_JJY, vlf_phase_month_JJY = raw(months[8], months_len_day[8], 4, 6, 7) 

#----------------Main code (Average)------------------------

# NWC (0,1) JJI (4,5) JJY(6,7)
vlf_amp_avg_NWC, vlf_phase_avg_NWC = average(months[8], months_len_day[8], months[7], months_len_day[7], 4, 0, 1)
vlf_amp_avg_JJI, vlf_phase_avg_JJI = average(months[8], months_len_day[8], months[7], months_len_day[7], 4, 4, 5) 
vlf_amp_avg_JJY, vlf_phase_avg_JJY = average(months[8], months_len_day[8], months[7], months_len_day[7], 4, 6, 7)  

#------------Amplitude + Phase plot (JJY)-----------------------------------

#Asigning variables to plot
time = range(4320)

#Setting a general font size for matplotlib
plt.rcParams['font.size'] = '18'
plt.subplots_adjust(wspace=0.25)

#Graphing parameters
ax = plt.subplot(5,2,1)
plt.plot(time, vlf_amp_month_JJY[38880:43200], color='blue')
plt.plot(time, vlf_amp_avg_JJY[38880:43200], linestyle='--', color='red')
plt.title('JJY-PTK Amplitude')
ax.set_xticks([])


ax = plt.subplot(5,2,2)
plt.plot(time, vlf_phase_month_JJY[38880:43200], color='blue')
plt.plot(time, vlf_phase_avg_JJY[38880:43200], linestyle='--', color='red')
plt.title('JJY-PTK Phase')
ax.set_xticks([])


ax = plt.subplot(5,2,3)
plt.plot(time, vlf_amp_month_JJY[43200:47520], color='blue')
plt.plot(time, vlf_amp_avg_JJY[43200:47520], linestyle='--', color='red')
ax.set_xticks([])


ax = plt.subplot(5,2,4)
plt.plot(time, vlf_phase_month_JJY[43200:47520], color='blue')
plt.plot(time, vlf_phase_avg_JJY[43200:47520], linestyle='--', color='red')
ax.set_xticks([])


ax = plt.subplot(5,2,5)
plt.plot(time, vlf_amp_month_JJY[47520:51840], color='blue')
plt.plot(time, vlf_amp_avg_JJY[47520:51840], linestyle='--', color='red')
ax.set_xticks([])


ax = plt.subplot(5,2,6)
plt.plot(time, vlf_phase_month_JJY[47520:51840], color='blue')
plt.plot(time, vlf_phase_avg_JJY[47520:51840], linestyle='--', color='red')
ax.set_xticks([])


ax = plt.subplot(5,2,7)
plt.plot(time, vlf_amp_month_JJY[51840:56160], color='blue')
plt.plot(time, vlf_amp_avg_JJY[51840:56160], linestyle='--', color='red')
ax.set_xticks([])


ax = plt.subplot(5,2,8)
plt.plot(time, vlf_phase_month_JJY[51840:56160], color='blue')
plt.plot(time, vlf_phase_avg_JJY[51840:56160], linestyle='--', color='red')
ax.set_xticks([])

ax = plt.subplot(5,2,9)
plt.plot(time, vlf_amp_month_JJY[56160:60480], color='blue')
plt.plot(time, vlf_amp_avg_JJY[56160:60480], linestyle='--', color='red')
ax.set_xticks(list(range(0,4500,360)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24'])
plt.xlabel('Time UTC')
plt.ylabel('Amplitude')

ax = plt.subplot(5,2,10)
plt.plot(time, vlf_phase_month_JJY[56160:60480], color='blue')
plt.plot(time, vlf_phase_avg_JJY[56160:60480], linestyle='--', color='red')
ax.set_xticks(list(range(0,4500,360)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24'])
plt.xlabel('Time UTC')
plt.ylabel('Degrees')
plt.show()