import numpy as np

#Function to split the time into hours and minutes
def read_int(char):
    return float(char.strip(b'"').replace(b':',b'.'))

#Read the csv file and save into 'hour' and 'mins' varriables
nighttime = np.genfromtxt('Nighttime data 2004.csv', dtype=float, usecols=(2,3), delimiter=',', converters={a: read_int for a in range(366)})
hour = np.floor(nighttime)
mins = np.round((nighttime - hour) * 100)
#Convert to a 20s time interval formate
data_point1  = hour * 180
data_point2 = mins * 3
#Save the daylight satrt and end times into a lidt
daylight_start = np.array(data_point1[:,0] + data_point2[:,0])
daylight_end = np.array(data_point1[:,1] + data_point2[:,1])
#Zero end values that go beyond mightnight
for i in range(len(daylight_end)):
    if daylight_end[i] < 300:
        daylight_end[i] = daylight_end[i]*0
daylight_times = np.column_stack((daylight_start, daylight_end))
#np.savetxt('vlf_data_output.txt',daylight_times, delimiter=',', fmt='%4i')
#print(daylight_times)
#print(np.shape(daylight_times))