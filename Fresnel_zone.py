from math import sqrt
from Haversine_eq import distances

#Function to calculate the nth Fresnel zone
def fresnelzone(n,d1,d2,lambda0,D):
    fresnelzone = sqrt((n*d1*d2*lambda0)/D) / 1000
    return fresnelzone

#Wavelength for VLF transmitters
lambda_JJI = (3*10**8) / (22.2*10**3)
lambda_JJY = (3*10**8) / (40*10**3)
lambda_NWC = (3*10**8) / (19.8*10**3)

#Calling the fresnelzone function to calculate Frensel zones
for i in range(1,6,2):
    fresnelzones_JJI = fresnelzone(i, (distances[0]/2)*(10**3), (distances[0]/2)*(10**3), lambda_JJI, distances[0]*(10**3))
    fresnelzones_JJY = fresnelzone(i, (distances[1]/2)*(10**3), (distances[1]/2)*(10**3), lambda_JJY, distances[1]*(10**3))
    fresnelzones_NWC = fresnelzone(i, (distances[2]/2)*(10**3), (distances[2]/2)*(10**3), lambda_NWC, distances[2]*(10**3))
    print(fresnelzones_JJI)
    print(fresnelzones_JJY)
    print(fresnelzones_NWC)

#def fresnelzone_test(lambda0, x, D):
#    fresnelzone_test = sqrt(((lambda0**2)/4)+(lambda0*x*(1 - (x/D)))) / 1000
#    return fresnelzone_test

#frenselzone2 = fresnelzone_test(lambda0, (distances[1]/2)*(10**3), distances[1]*(10**3))
#print(frenselzone2)
