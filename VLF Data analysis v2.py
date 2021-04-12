import numpy as np
from matplotlib import pyplot as plt
import os
from VLF_Data_nighttime import daylight_times

months = ['MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
month_len = [31,]
years = [4, 5, 6, 7]
os.chdir("./VLF Data Raw")

for a in range(1):
    for b in range(len(months)):
        for i in range(len(month_len)):
            avg_days = np.genfromtxt(f'T{}{months[b]}{years[a]}A.kam', dtype=float, delimiter=',')
            for x in range(1,6):
                avg_day = np.genfromtxt(f'T{i-x}{months[b]}{years[a]}A.kam', dtype=float, delimiter=',')
                avg_days = np.columnstack(avg_days, avg_day)
            