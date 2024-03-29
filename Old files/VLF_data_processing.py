import numpy as np
from matplotlib import pyplot as plt
import time
import os

from VLF_Data_nighttime import daylight_start, daylight_end

os.chdir("./VLF Data numpy array")
index=[]
anomalies = 0
months = ['MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
years = [4, 5, 6, 7]

tic = time.perf_counter()
vlf_amp_diff = np.array([])
for a in range(len(years)):
    nighttime_counter = 0
    for b in range(len(months)):

        #Loading file + average
        file_name = 'vlf_amp_JJY_' + months[b] + '200' + str(years[a]) + '.txt'
        vlf_amp = np.genfromtxt(file_name, dtype=float, delimiter=',')

        for z in range(np.shape(vlf_amp)[1]):

            #Removing daytime rows
            np.delete(vlf_amp, slice(int(daylight_start[nighttime_counter]), int(daylight_end[nighttime_counter])), 1)
            nighttime_counter += 1

        vlf_amp_avg = np.mean(vlf_amp, axis=1)  
        for z in range(1, np.shape(vlf_amp)[1]):
            diff = vlf_amp[:,z] - vlf_amp_avg
            
            if z == 1:
                vlf_amp_diff = np.array(diff)

            else:
                vlf_amp_diff = np.column_stack((vlf_amp_diff, diff))

        
        vlf_amp_std = np.array([])
        for i in range(1, np.shape(vlf_amp)[1]):
            vlf_amp_std = np.append(vlf_amp_std, (np.std(vlf_amp_diff[:,i-1], axis=0)))
        
        for x in range(np.shape(vlf_amp)[1]-1):
            counter=0
            for y in range(4320):
                if abs(vlf_amp_diff[y, x]) > (2*vlf_amp_std[x]):
                        counter += 1
            if counter > 10:
                index.append([x,months[b],years[a]])
                anomalies += 1

"""
        vlf_amp_std = np.std(vlf_amp_diff, axis=1)
        for x in range(np.shape(vlf_amp)[1]-1):
            counter=0
            for y in range(4320):
                if abs(vlf_amp_diff[y, x]) > abs(2*vlf_amp_std[y]):
                        counter += 1
            if counter != 0:
                index.append([x,months[b],years[a]])
                anomalies += 1
"""
print('Number of days with signal anomalies =', anomalies, '/ 1224')
print(index)