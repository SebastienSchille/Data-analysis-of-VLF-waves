import numpy as np
from matplotlib import pyplot as plt
import time
import os

os.chdir("./VLF Data")

months = ['MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
years = [4, 5, 6, 7]

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
        
        np.savetxt(f'vlf_data_NWC_{months[b]}200{years[a]}.txt',vlf_data_NWC, delimiter=',')
        np.savetxt(f'vlf_data_JJI_{months[b]}200{years[a]}.txt',vlf_data_JJI, delimiter=',')
        np.savetxt(f'vlf_data_JJY_{months[b]}200{years[a]}.txt',vlf_data_JJY, delimiter=',')
        print('Data Saved for: ', months[b], ' 200',years[a], sep='')

toc = time.perf_counter()
#np.savetxt('vlf_data_NWC.txt',vlf_data_NWC, delimiter=',')
#np.savetxt('vlf_data_JJI.txt',vlf_data_JJI, delimiter=',')
#np.savetxt('vlf_data_JJY.txt',vlf_data_JJY, delimiter=',')

print('Time to collect data:', (toc-tic), 'seconds')
print(vlf_data_JJY)