import numpy as np
from matplotlib import pyplot as plt
import os

os.chdir("./VLF Data numpy array")

vlf_amp = np.genfromtxt('vlf_amp_JJY_MAR2005.txt', dtype=float, delimiter=',')
vlf_amp_avg = np.mean(vlf_amp, axis=1)

for i in range(1, np.shape(vlf_amp)[1]):
            diff = vlf_amp[:,i] - vlf_amp_avg
            
            if i == 1:
                vlf_amp_diff = np.array(diff)

            else:
                vlf_amp_diff = np.column_stack((vlf_amp_diff, diff))

vlf_amp_std = np.std(vlf_amp_diff, axis=0)

time = np.array(range(1,4321))
signal = vlf_amp_diff[:,18]
std_line = []

for i in range(1,4321):
    std_line.append(vlf_amp_std[18])

std_line_minus = []

for i in range(1,4321):
    std_line_minus.append(std_line[18]*-1)

plt.plot(time, signal, color='blue')
plt.plot(time, std_line, linestyle='--', color='red')
plt.plot(time, std_line_minus, linestyle='--', color='red')

plt.show()

#os.chdir("..")

#np.savetxt('vlf_amp_diff.txt', vlf_amp_diff, delimiter=',')
#np.savetxt('vlf_amp_std.txt', vlf_amp_std, delimiter=',')