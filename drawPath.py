import pygame as pg

def drawLoop(path, screen, color, width):
    for i in range(len(path)):
        pg.draw.line(screen, color, path[i], path[(i+1)%len(path)], width)

def drawPath(path, screen, color, width):
    for i in range(len(path)-1):
        pg.draw.line(screen, color, path[i], path[i+1], width)