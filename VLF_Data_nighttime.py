import numpy as np


def read_int(char):
    return float(char.strip(b'"').replace(b':',b'.'))


nighttime = np.genfromtxt('Nighttime data 2004.csv', dtype=float, usecols=(2,3), delimiter=',', converters={a: read_int for a in range(366)})
hour = np.floor(nighttime)
mins = (nighttime - hour) * 100

data_point1  = hour * 180
data_point2 = mins * 3

daylight_start = data_point1[:,0] + data_point2[:,0]
daylight_end = data_point1[:,1] + data_point2[:,1]

for i in range(len(daylight_end)):
    if daylight_end[i] < 300:
        daylight_end[i] = daylight_end[i]*0

#print(daylight_start)
#print(daylight_end)
