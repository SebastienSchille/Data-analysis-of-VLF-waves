import numpy as np
from matplotlib import pyplot as plt
import os
from VLF_Data_nighttime import daylight_times

os.chdir("./VLF Data numpy array")

vlf_amp = np.genfromtxt('vlf_amp_JJY_AUG2005.txt', dtype=float, delimiter=',')

for i in range (3,(len(vlf_amp))):
    vlf_avg = np.mean(vlf_amp[:,[i-3,i]])