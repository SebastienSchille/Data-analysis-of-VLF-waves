import numpy as np
from matplotlib import pyplot as plt
import time

months = ['MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
years = [4, 5, 6, 7]

"""
for a in range(len(years)):
    for b in range(len(months)):
        for i in range(1,32):
            if i <= 10:
                file_name = 'T0' + str(i) + months[b] + str(years[a]) + 'A.kam'
            else:
                file_name = 'T' + str(i) + months[b] + str(years[a]) + 'A.kam'
            
            vlf_data = np.genfromtxt(file_name, dtype=float)
"""
tic = time.perf_counter()

for a in range(len(years)):
    for b in range(len(months)):
        for i in range(1,32):
            if i==31 and (months[b] == 'APR' or months[b] == 'JUN' or months[b] == 'SEP' or months[b] == 'NOV'):
                break
            elif i < 10:
                file_name = 'T0' + str(i) + months[b] + str(years[a]) + 'A.kam'
            else:
                file_name = 'T' + str(i) + months[b] + str(years[a]) + 'A.kam'

            if i == 1:
                vlf_data_NWC = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(0,1))
                vlf_data_JJI = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(4,5))
                vlf_data_JJY = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(6,7))

            else:
                data_NWC = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(0,1))
                vlf_data_NWC = np.column_stack((vlf_data_NWC, data_NWC))
                data_JJI = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(4,5))
                vlf_data_JJI = np.column_stack((vlf_data_JJI, data_JJI))
                data_JJY = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(6,7))
                vlf_data_JJY = np.column_stack((vlf_data_JJY, data_JJY))
        print('Data completed for: ', months[b], ' 200',years[a], sep='')

toc = time.perf_counter()

tic2 = time.perf_counter()
vlf_data_amplitutde_db = (20*np.log(vlf_data_NWC[:,0]))
vlf_data_phase_db = (20*np.log(vlf_data_NWC[:,1]))
toc2 = time.perf_counter()

print('Time to collect data:', (toc-tic), 'seconds')
print('Time to calculate amp/phase:', (toc2-tic2), 'seconds')
print(vlf_data_JJY)