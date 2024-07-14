import math

def obliqueThrow(d, alpha):
  #angle given in degrees
  v0 = (d/math.sin(2*math.radians(alpha))*10)**(1/2)   #g = 10 m/s**2
  return v0

def obliqueThrowAirResistance(d, alpha, k, m):
  #angle given in degrees
  return (d*k)/(m*math.sin(2*math.radians(alpha))*math.exp(-2*math.sin(math.radians(alpha))))