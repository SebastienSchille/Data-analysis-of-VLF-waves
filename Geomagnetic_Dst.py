import numpy as np
import os

os.chdir("./Dst Data")
months = ['JAN','FEB','MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
years = [2004, 2005, 2006, 2007]
Dst_events = np.empty(3)

for a in range(4):
    for b in range(len(months)):
        file_name = 'DST_' + months[b] + str(years[a]) + '.txt'
        Dst_values = np.genfromtxt(file_name, usecols=(range(1,25)))
        print(file_name)

        for i in range(np.shape(Dst_values)[0]):
            event_counter = 0
            for z in range(np.shape(Dst_values)[1]):
                if Dst_values[i,z] < -100:
                    event_counter += 1
            if event_counter > 0:
                Dst_avg = np.round(np.mean(Dst_values[i,:], axis=0))
                Dst_min = np.min(Dst_values[i,:])
                Dst_events = np.vstack((Dst_events, [(str(i)+months[b]+str(years[a])), Dst_avg, Dst_min]))

Dst_events = np.delete(Dst_events, 0, axis=0)
np.savetxt('Dst_events.txt', Dst_events, delimiter=',')
#print(Dst_events)