from itertools import permutations
from distance import totalDist
import pygame as pg
from drawPath import *
from time import sleep
from constants import *
from points import *

def tspBrute(points, visitor):
    best = float("inf")
    best_path = []
    for perm in permutations(points):
        currDist = totalDist(list(perm))
        if(currDist < best):
            best = currDist
            best_path = list(perm)
        visitor(perm, best_path)

    return best_path

def tspBruteVisitorGetter(screen):
    def result( path, best_path):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN:
                raise Exception
        screen.fill(BG_COLOR)
        drawLoop(path, screen, LINE_COLOR, 4)
        drawLoop(best_path, screen, RESULT_COLOR, 2)
        drawPoints(path, screen)
        pg.display.flip()
        sleep(DELAY)
    return result