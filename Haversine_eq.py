from math import sin,cos,asin,radians

#Radius of the earth
r = 6371

#JJY, JJI, NWC, NMP, PTK
longitudes = [140.849007, 130.829095, 114.16546, -158.153912, 158.550]
latitudes = [37.372557, 32.092247, -21.816325, 21.420382, 53.090] 

def haversine(phi1,phi2,lambda1,lambda2):
    distance = 2*r*asin(((sin((phi2-phi1)/2)**2)+(cos(phi1)*cos(phi2)*(sin((lambda2 - lambda1)/2)**2)))**0.5)
    return distance

VLF_distances = []
for i in range(len(longitudes)-1):
    phi1 = radians(latitudes[i])
    phi2 = radians(latitudes[4])
    lambda1 = radians(longitudes[i])
    lambda2 = radians(longitudes[4])
    distance = haversine(phi1,phi2,lambda1,lambda2)
    VLF_distances.append(distance)

#print(VLF_distances)