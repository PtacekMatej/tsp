from distance import totalDist
from constants import *
from drawPath import *
from time import sleep
from points import *
import pygame as pg
import random



def tspHillClimbVisitorGetter(screen, points):
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

def rotate(l, n):
    return l[n:] + l[:n]


def tspHillClimb(points, visitor):
    bestResult = points
    betterNotFound = 0

    while betterNotFound < 10:
        res = bestResult[:]
        toShuffle = random.randint(0, len(res)-1)
        res = rotate(res, toShuffle)
        subArr = res[0:len(res)//(2*(betterNotFound + 1))]
        random.shuffle(subArr)
        res[0:len(res)//(2*(betterNotFound + 1))] = subArr
        bestDist = totalDist(res)
        notImproved = 0
        while notImproved < 1000:
            swap1 = random.randint(0, len(points)-1)
            swap2 = random.randint(0, len(points)-1)
            if swap1 > swap2:
                swap1, swap2 = swap2, swap1
            res[swap1 : swap2] = reversed(res[swap1 : swap2])
            dist = totalDist(res)
            if dist >= bestDist:
                res[swap1 : swap2] = reversed(res[swap1 : swap2])
                notImproved += 1
            else:
                bestDist = dist
                notImproved = 0
                visitor(res)
        if totalDist(bestResult) > totalDist(res):
            bestResult = res
            betterNotFound = 0
        else:
            betterNotFound += 1


    return bestResult

