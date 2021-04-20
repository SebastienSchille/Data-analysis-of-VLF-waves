from math import sqrt
from Haversine_eq import VLF_distances

#Function to calculate the nth Fresnel zone
def fresnelzone(n,d1,d2,lambda0,D):
    fresnelzone = sqrt((n*d1*d2*lambda0)/D) / 1000
    return fresnelzone

#Function to calculate wavelengths for VLF signals
wavelengths = [40, 22.2, 19.8, 21.4] #JJY, JJI, NWC, NPM (KHz)
def wavelength(wavelengths):
    VLF_lambda = (3*10**8) / (wavelengths*10**3)
    return VLF_lambda

#Calling the fresnelzone function to calculate Frensel zones
fresnelzones = []
for a in range(1,7,2):
    print(a)
    for i in range(len(VLF_distances)):
        VLF_lambda = wavelength(wavelengths[i])
        fresnel = fresnelzone(a, (VLF_distances[i]/2)*(10**3), (VLF_distances[i]/2)*(10**3), VLF_lambda, VLF_distances[i]*(10**3))
        fresnelzones.append(fresnel)

print(fresnelzones)


#THE CODE BELOW USES THE FIRST FRENSEL ZONE EQ ONLY
#-----------------------------------------------------
"""
def fresnelzone_test(lambda0, x, D):
    fresnelzone_test = sqrt(((lambda0**2)/4)+(lambda0*x*(1 - (x/D)))) / 1000
    return fresnelzone_test

frenselzone2 = fresnelzone_test(lambda0, (distances[1]/2)*(10**3), distances[1]*(10**3))
print(frenselzone2)
"""
#--------------------------------------------------------------
