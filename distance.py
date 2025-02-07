from math import sqrt

def dist(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def totalDist(points):
    total = 0
    for i in range(len(points)):
        total += dist(points[i], points[(i+1) % len(points)])
    return total

def pathDist(points):
    return totalDist(points) - dist(points[0], points[-1])
