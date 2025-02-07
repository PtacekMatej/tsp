from constants import *
import pygame as pg
from distance import *


def drawPoints(points, screen):
    for point in points:
            pg.draw.circle(screen, POINT_COLOR, point, POINT_RADIUS)


def handlePointsMove(event, points, dragging_point):
    if event.type == pg.MOUSEBUTTONUP:
        if event.button == 1:
            dragging_point = None
    elif event.type == pg.MOUSEMOTION:
        if dragging_point is not None:
            points[dragging_point] = event.pos
    return points, dragging_point


def handlePointsAddDrag(event, points, dragging_point):
    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        for i, point in enumerate(points):
            if dist(point, event.pos) <= POINT_RADIUS:
                dragging_point = i
                break
        else:
            points.append(event.pos)
    points, dragging_point = handlePointsMove(event, points, dragging_point)
    return points, dragging_point

def handlePointsDelete(event, points):
    if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
        points = [p for p in points if dist(p, event.pos) > POINT_RADIUS]
    return points

def handlePoints(event, points, dragging_point, result):
    pointsNew = handlePointsDelete(event, points)
    pointsNew, dragging_pointNew = handlePointsAddDrag(event, pointsNew, dragging_point)
    return pointsNew, dragging_pointNew, result if (pointsNew == points )and( dragging_pointNew == dragging_point) else None

