

def orientation(a, b, c):
    res = (b[1]-a[1]) * (c[0]-b[0]) - (c[1]-b[1]) * (b[0]-a[0])
    if res == 0:
        return 0
    if res > 0:
        return 1
    return -1  


def convexHull(points):
    points.sort()
    top = []
    bottom = []
    for point in points:
        while len(top) >= 2 and orientation(top[-2], top[-1], point) < 0:
            top.pop()
        top.append(point)
        while len(bottom) >= 2 and orientation(bottom[-2], bottom[-1], point) > 0:
            bottom.pop()
        bottom.append(point)
    if len(bottom) > 0:
        bottom.pop()
    for point in reversed(bottom):
        top.append(point)
    if len(top) > 0:
        top.pop()
    return top