from convexHull import convexHull
import itertools
from distance import *
import pygame as pg
from constants import *
from drawPath import *
from points import *
from time import sleep


def getPath(memo, last, i, bits, onHull, inside):
    path = []
    while last is not None:
        path.append(onHull[last] if last >= 0 else inside[-last-1])
        _, new_last  = memo[(i, bits, last)]
        if last == i:
            i -= 1
        else:
            bits &= ~(1 << (-last - 1))
        last = new_last
    return path


def tspConvHullVisitorGetter(screen, points):
    def result(path):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN:
                raise Exception
        screen.fill(BG_COLOR)
        drawLoop(path, screen, LINE_COLOR, 4)
        drawPoints(points, screen)
        pg.display.flip()
        sleep(DELAY)
    return result


def tspConvHull(points, visitor):
    onHull = convexHull(points)
    inside = [point for point in points if point not in onHull]

    dp = {}

    dp[(0, 0, 0)] = (0, None) # i, S, x
        

    for i in range(len(onHull)):
        for subset_size in range(len(inside)+1):
            for subset in itertools.combinations(range(len(inside)), subset_size):
                bits = 0
                for bit in subset:
                    bits |= 1 << bit


                if i > 0:
                    dp[(i, bits, i)] = (dp[i-1, bits, i-1][0] + dist(onHull[i], onHull[i-1]), i-1) if i > 1 or bits == 0 else (float("inf"), None)
                    for x in subset:
                        if dp[(i, bits, i)][0] > dp[(i-1, bits, -x-1)][0] + dist(onHull[i], inside[x]):
                            dp[(i, bits, i)] = (dp[(i-1, bits, -x-1)][0] + dist(onHull[i], inside[x]), -x-1)
                    visitor(getPath(dp, i, i, bits, onHull, inside))
                
                for x in subset:
                    newBits = bits & ~(1<<x)
                    dp[(i, bits, -x-1)] = (dp[(i, newBits, i)][0] + dist(onHull[i], inside[x]), i) if i != 0 or newBits == 0 else (float("inf"), None)
                    for y in subset:
                        if x == y:
                            pass
                        elif dp[(i, bits, -x-1)][0] > dp[(i, newBits, -y-1)][0] + dist(inside[y], inside[x]):
                            dp[(i, bits, -x-1)] = (dp[(i, newBits, -y-1)][0] + dist(inside[y], inside[x]), -y-1)
                    visitor(getPath(dp, -x-1, i, bits, onHull, inside))



    bits = 0
    for bit in range(len(inside)):
        bits |= 1 << bit
    opt = dp[(len(onHull)-1, bits, len(onHull)-1)][0] + dist(onHull[-1], onHull[0])
    last = len(onHull)-1


    for x in range(len(inside)):
        if dp[(len(onHull)-1, bits, -x-1)][0] + dist(onHull[0], inside[x]) < opt:
            opt = dp[(len(onHull)-1, bits, -x-1)][0] + dist(onHull[0], inside[x])
            last = -x-1

    return getPath(dp, last, len(onHull)-1, bits, onHull, inside)

                    