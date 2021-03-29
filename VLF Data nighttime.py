import numpy as np


def read_int(char):
    return float(char.strip(b'"').replace(b':',b'.'))


nighttime = np.genfromtxt('Nighttime data 2004.csv', dtype=float, usecols=(2,3), delimiter=',', converters={a: read_int for a in range(366)})
hour = np.floor(nighttime)
mins = (nighttime - hour) * 100

data_point1  = hour * 180
data_point2 = mins * 4

daylight_start = data_point1[:,0] + data_point2[:,0]
daylight_end = data_point1[:,1] + data_point2[:,1]

print(daylight_start)
print(daylight_end)
