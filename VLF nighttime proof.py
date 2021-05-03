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

def raw (month, month_len, year, station_amp, station_phase):
    for i in range(1, (month_len+1)):
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

#-------------------Main code-----------------------------------------------------

vlf_amp_month_1, vlf_phase_month_1 = raw(months[2], months_len_day_2004[6], 4, 4, 5)
vlf_amp_month_2, vlf_phase_month_2 = raw(months[5], months_len_day_2004[5], 4, 4, 5)
vlf_amp_month_3, vlf_phase_month_3 = raw(months[10], months_len_day_2004[10], 4, 0, 1)
vlf_amp_month_4, vlf_phase_month_4 = raw(months[0], months_len_day_2004[0], 7, 6, 7)

#------------------------Magnitude plot difference-------------------------------------------

#Asigning variables to plot
time = range(4320)
#Setting a general font size for matplotlib
plt.rcParams['font.size'] = '18'
plt.subplots_adjust(hspace=0.6)

#Graphing parameters
ax = plt.subplot(2,2,1)
plt.plot(time, vlf_amp_month_1[0:4320], color='blue')
start = nighttime_2004[months_len_2004[2], 0]
end = nighttime_2004[months_len_2004[2], 1]
ymin = np.min(vlf_amp_month_1[0:4320])
ymax = np.max(vlf_amp_month_1[0:4320])
plt.vlines(start, ymin, ymax, color='red', linestyles='--')
plt.vlines(end, ymin, ymax, color='red', linestyles='--')
ax.set_title('March')
ax.set_xticks(list(range(0,4500,360)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24',])
plt.xlabel('Time UTC', labelpad=10)
plt.ylabel('Magnitude', labelpad=10)

#Graphing parameters
ax = plt.subplot(2,2,2)
plt.plot(time, vlf_amp_month_2[0:4320], color='blue')
start = nighttime_2004[months_len_2004[5], 0]
end = nighttime_2004[months_len_2004[5], 1]
ymin = np.min(vlf_amp_month_2[0:4320])
ymax = np.max(vlf_amp_month_2[0:4320])
plt.vlines(start, ymin, ymax, color='red', linestyles='--')
plt.vlines(end, ymin, ymax, color='red', linestyles='--')
ax.set_title('June')
ax.set_xticks(list(range(0,4500,360)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24',])
plt.xlabel('Time UTC', labelpad=10)
plt.ylabel('Magnitude', labelpad=10)

#Graphing parameters
ax = plt.subplot(2,2,3)
plt.plot(time, vlf_phase_month_3[0:4320], color='blue')
start = nighttime_2004[months_len_2004[8], 0]
end = nighttime_2004[months_len_2004[8], 1]
ymin = np.min(vlf_phase_month_3[0:4320])
ymax = np.max(vlf_phase_month_3[0:4320])
plt.vlines(start, ymin, ymax, color='red', linestyles='--')
plt.vlines(end, ymin, ymax, color='red', linestyles='--')
ax.set_title('November')
ax.set_xticks(list(range(0,4500,360)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24',])
plt.xlabel('Time UTC', labelpad=10)
plt.ylabel('Magnitude', labelpad=10)

#Graphing parameters
ax = plt.subplot(2,2,4)
plt.plot(time, vlf_amp_month_4[0:4320], color='blue')
start = nighttime_2007[months_len[0], 0]
end = nighttime_2007[months_len[0], 1]
ymin = np.min(vlf_amp_month_4[0:4320])
ymax = np.max(vlf_amp_month_4[0:4320])
plt.vlines(start, ymin, ymax, color='red', linestyles='--')
plt.vlines(end, ymin, ymax, color='red', linestyles='--')
ax.set_title('December')
ax.set_xticks(list(range(0,4500,360)))
ax.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20','22','24',])
plt.xlabel('Time UTC', labelpad=10)
plt.ylabel('Magnitude', labelpad=10)
plt.show()