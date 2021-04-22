import numpy as np
import os

os.chdir("./Nighttime data")
months_len = np.array([0,31,59,90,120,151,181,212,243,273,304,334])
months_len_2004 = np.array([0,31,60,91,121,152,182,213,244,274,305,335])

#Function to split the time into hours and minutes
def read_int(char):
    return float(char.strip(b'"').replace(b':',b'.'))

def nighttime (year):
    #Read the csv file and save into 'hour' and 'mins' varriables
    nighttime = np.genfromtxt(f'Nighttime data 200{year}.csv', dtype=float, usecols=(0,1), delimiter=',', converters={a: read_int for a in range(366)})
    hour = np.floor(nighttime)
    mins = np.round((nighttime - hour) * 100)
    #Adjust to UTC+12
    hour1 = hour[:,0] + 12
    hour2 = hour[:,1] - 12
    hour = np.column_stack((hour2, hour1))
    #Convert to a 20s time interval formate
    data_point1  = hour * 180
    data_point2 = mins * 3
    #Save the daylight satrt and end times into a list
    nighttime_start = np.array(data_point1[:,0] + data_point2[:,0])
    nighttime_end = np.array(data_point1[:,1] + data_point2[:,1])
    #Zero end values that go beyond mightnight
    for i in range(len(nighttime_start)):
        if nighttime_start[i] < 0:
            nighttime_start[i] = nighttime_start[i]*-1
    nighttime_times = np.column_stack((nighttime_start, nighttime_end))
    return nighttime_times

nighttime_times = np.array([])
for i in range(4,8):
    times = nighttime(i)
    nighttime_times = np.column_stack((nighttime_times, times))

os.chdir("..")
#np.savetxt('vlf_data_output.txt',nighttime_times, delimiter=',', fmt='%4i')
#print(nighttime_times[months_len_2004[4],1])
#print(np.shape(nighttime_times))