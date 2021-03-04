from math import sin,cos,asin,radians

#Radius of the earth
r = 6371

#JJI, JJY, NWC
transmitter_longs = [32.092247, 37.372557, -21.816325]
transmitter_lats = [130.829095, 140.849007, 114.16546]
#PTK
receiver_long = 53.090
receiver_lat = 158.550

def haversine(phi1,phi2,lambda1,lambda2):
    distance = 2*r*asin(((sin((phi2-phi1)/2)**2)+(cos(phi1)*cos(phi2)*(sin((lambda2 - lambda1)/2)**2)))**0.5)
    return distance

distances = []
for i in range(len(transmitter_longs)):
    phi1 = radians(transmitter_lats[i])
    phi2 = radians(receiver_lat)
    lambda1 = radians(transmitter_longs[i])
    lambda2 = radians(receiver_long)
    distance = haversine(phi1,phi2,lambda1,lambda2)
    distances.append(distance)

#print(distances)