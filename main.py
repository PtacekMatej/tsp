import pygame as pg
from distance import *
from drawPath import *
from tspBrute import *
from points import *
from tspDP import *  
from convexHull import *
from tspConvHull import *

from test import test

def main():
    #test()


    pg.init()
    dragging_point = None
    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)
    

    result = None        
    points = []

    while True:

        screen.fill(BG_COLOR)
    
        if result is not None:
            drawLoop(result, screen, RESULT_COLOR, 4)

        drawPoints(points, screen)
        
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    try:
                        result = None
                        result = tspBrute(points, tspBruteVisitorGetter(screen))
                    except:
                        pass
                if event.key == pg.K_w:
                    try:
                        result = None
                        result = tspDP(points, tspDPvisitorGetter(screen, points))
                    except:
                        pass
                if event.key == pg.K_e:
                    try:
                        result = None
                        result = tspConvHull(points, tspConvHullVisitorGetter(screen, points))
                    except:
                        pass
                
            points, dragging_point, result = handlePoints(event, points, dragging_point, result)



        pg.display.flip()


main()