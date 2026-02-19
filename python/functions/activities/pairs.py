import math

def distance(a, b):
    return round(math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2), 2)

p1 = (100.768, 50.5)
p2 = (234.78, 80.1)

print(distance(p1, p2))