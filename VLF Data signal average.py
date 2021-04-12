import numpy as np
from matplotlib import pyplot as plt
import os
from VLF_Data_nighttime import daylight_times

os.chdir("./VLF Data raw")
vlf_data_avg = np.empty(8)

def average (loc, station_amp, station_phase):
    for i in range((loc-5),loc):
        amp = np.genfromtxt(f'T{i}OCT4A.kam', dtype=float, skip_header=1, usecols=(station_amp))
        phase = np.genfromtxt(f'T{i}OCT4A.kam', dtype=float, skip_header=1, usecols=(station_phase))
        vlf_amp = np.column_stack((vlf_amp, amp))
        vlf_phase = np.column_stack((vlf_amp, amp))
        vlf_amp_avg = np.mean(vlf_amp, axis=0)
        vlf_phase_avg = np.mean(vlf_phase, axis=0)
        return vlf_amp_avg, vlf_phase_avg

def difference ():

def std ():



print(vlf_data)
print(np.shape(vlf_data))