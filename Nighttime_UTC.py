import numpy as np
import os

os.chdir("./Nighttime data")
#Function to split the time into hours and minutes
def read_int(char):
    return float(char.strip(b'"').replace(b':',b'.'))

def nighttime (year):
    #Read the csv file and save into 'hour' and 'mins' varriables
    nighttime = np.genfromtxt(f'Nighttime data 200{year}.csv', dtype=float, usecols=(2,3), delimiter=',', converters={a: read_int for a in range(366)})
    hour = np.floor(nighttime)
    mins = np.round((nighttime - hour) * 100)
    #Adjust to UTC+12
    hour1 = hour[:,0] + 12
    hour2 = hour[:,1] - 12
    hour = np.column_stack((hour2, hour1))
    #Convert to a 20s time interval format
    data_point1  = hour * 180
    data_point2 = mins * 3
    #Save the daylight satrt and end times into a list
    nighttime_start = np.array(data_point1[:,0] + data_point2[:,0])
    nighttime_end = np.array(data_point1[:,1] + data_point2[:,1])
    #Readjust values that go beyond mightnight
    for i in range(len(nighttime_start)):
        if nighttime_start[i] < 0:
            nighttime_start[i] = nighttime_start[i] + (24*180)
    nighttime_times = np.column_stack((nighttime_start, nighttime_end))
    return nighttime_times

#----------Main code -------------------

nighttime_2004 = nighttime(4)
nighttime_2005 = nighttime(5)
nighttime_2006 = nighttime(6)
nighttime_2007 = nighttime(7)

os.chdir("..")
#np.savetxt('vlf_data_output.txt',nighttime_2004, delimiter=',', fmt='%4i')
#print(nighttime_2004)
#diff = nighttime_2004[:,1] - nighttime_2004[:,0]
#print(np.min(diff)) 
#print(np.shape(nighttime_times))