import numpy as np
from matplotlib import pyplot as plt
import os
from VLF_Data_nighttime import daylight_start, daylight_end

os.chdir("./VLF Data numpy array")

vlf_amp = np.genfromtxt('vlf_amp_JJY_MAR2005.txt', dtype=float, delimiter=',')
vlf_amp_avg = np.mean(vlf_amp, axis=1)



##MK1--------------------------------------------------------------------------------------
"""
for i in range(np.shape(vlf_amp)[1]):
            diff = vlf_amp[:,i] - vlf_amp_avg
            delete_rows = list(range(int(daylight_start[i+60]), int(daylight_end[i+60])))
            diff = np.delete(diff, delete_rows, axis=0)
            
            if i == 0:
                vlf_amp_diff = np.array(diff)

            else:
                vlf_amp_diff = np.column_stack((vlf_amp_diff, diff))


for i in range(np.shape(vlf_amp_diff)[1]):
    for x in range(int(daylight_start[i+60]), int(daylight_end[i+60])):
        print(x)
        np.delete(vlf_amp_diff, x, axis=0)

vlf_amp_std = np.array([])
for i in range(np.shape(vlf_amp_diff)[1]):
    vlf_amp_std = np.append(vlf_amp_std, (np.std(vlf_amp_diff[:,i], axis=0)))
"""
#-----------------------------------------------------------------------------------
##MKII------------------------------------------------------------------------------

vlf_amp_diff = np.array([])
vlf_amp_std = np.array([])
diff_len = np.array([])
for i in range(np.shape(vlf_amp)[1]):
            diff = vlf_amp[:,i] - vlf_amp_avg
            delete_rows = list(range(int(daylight_start[i+60]), int(daylight_end[i+60])))
            diff = np.delete(diff, delete_rows, axis=0)
            diff_len = np.append(diff_len, (len(diff)))
            std_val = (2*np.std(diff)) + np.mean(diff)
            vlf_amp_std = np.append(vlf_amp_std, std_val)


            if i == 18:
                vlf_amp_diff = np.append(vlf_amp_diff, diff)
                mean_val = np.mean(diff)

#Graphing---------------------------------------------------
time = np.array(range(int(diff_len[18])))
signal = vlf_amp_diff

std_line = []
print(vlf_amp_std[18])

for i in range(int(diff_len[18])):
    std_line.append((vlf_amp_std[18]))

std_line_minus = []

for i in range(int(diff_len[18])):
    std_line_minus.append((-1*vlf_amp_std[18])+(2*mean_val))

plt.plot(time, signal, color='blue')
plt.plot(time, std_line, linestyle='--', color='red')
plt.plot(time, std_line_minus, linestyle='--', color='red')

plt.show()

#os.chdir("..")

#np.savetxt('vlf_amp_diff.txt', vlf_amp_diff, delimiter=',')
#np.savetxt('vlf_amp_std.txt', vlf_amp_std, delimiter=',')