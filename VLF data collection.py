import numpy as np
from matplotlib import pyplot as plt
import time
import os

os.chdir("./VLF Data Raw")

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
                vlf_amp_NWC = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(0))
                vlf_phase_NWC = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(1))
                vlf_amp_JJI = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(4))
                vlf_phase_JJI = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(5))
                vlf_amp_JJY = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(6))
                vlf_phase_JJY = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(7))

            else:
                amp_NWC = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(0))
                vlf_amp_NWC = np.column_stack((vlf_amp_NWC, amp_NWC))
                phase_NWC = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(1))
                vlf_phase_NWC = np.column_stack((vlf_phase_NWC, phase_NWC))
                
                amp_JJI = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(4))
                vlf_amp_JJI = np.column_stack((vlf_amp_JJI, amp_JJI))
                phase_JJI = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(5))
                vlf_phase_JJI = np.column_stack((vlf_phase_JJI, phase_JJI))
                
                amp_JJY = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(6))
                vlf_amp_JJY = np.column_stack((vlf_amp_JJY, amp_JJY))
                phase_JJY = np.genfromtxt(file_name, dtype=float, skip_header=1, usecols=(7))
                vlf_phase_JJY = np.column_stack((vlf_phase_JJY, phase_JJY))
                
        
        np.savetxt(f'vlf_amp_NWC_{months[b]}200{years[a]}.txt',vlf_amp_NWC, delimiter=',')
        np.savetxt(f'vlf_phase_NWC_{months[b]}200{years[a]}.txt',vlf_phase_NWC, delimiter=',')
        np.savetxt(f'vlf_amp_JJI_{months[b]}200{years[a]}.txt',vlf_amp_JJI, delimiter=',')
        np.savetxt(f'vlf_phase_JJI_{months[b]}200{years[a]}.txt',vlf_phase_JJI, delimiter=',')
        np.savetxt(f'vlf_amp_JJY_{months[b]}200{years[a]}.txt',vlf_amp_JJY, delimiter=',')
        np.savetxt(f'vlf_phase_JJY_{months[b]}200{years[a]}.txt',vlf_phase_JJY, delimiter=',')
        print('Data Saved for: ', months[b], ' 200',years[a], sep='')

toc = time.perf_counter()

print('Time to collect data:', (toc-tic), 'seconds')