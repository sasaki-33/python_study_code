import math

def pi(n):
    in_polygons = 2*n*math.sin(math.radians(180/n))
    out_polygons = 2*n*math.tan(math.radians(180/n))

    return [in_polygons/2,out_polygons/2]

i = pi(180)
print('{} < π < {}'.format(i[0],i[1]))