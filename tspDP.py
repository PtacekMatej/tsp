from distance import *
from constants import *
from drawPath import *
from time import sleep
from points import *
import pygame as pg
import itertools


def tspDP(points, visitor):

    dists = [[dist(x, y) for y in points] for x in points]

    """
    Implementation of Held-Karp, an algorithm that solves the Traveling
    Salesman Problem using dynamic programming with memoization.

    Parameters:
        dists: distance matrix

    Returns:
        A tuple, (cost, path).
    """
    n = len(dists)

    # Maps each subset of the nodes to the cost to reach that subset, as well
    # as what node it passed before reaching this subset.
    # Node subsets are represented as set bits.
    C = {}

    # Set transition cost from initial state
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0) 

    # Iterate subsets of increasing length and store intermediate results
    # in classic dynamic programming manner
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # Set bits for all nodes in this subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Find the lowest cost to get to this subset
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)

                parent = k
                path = []
                bits2 = bits
                while bits2 > 1:
                    path.append(parent)
                    new_bits = bits2 & ~(1 << parent)
                    _, parent = C[(bits2, parent)]
                    bits2 = new_bits
                path.append(0)
                visitor(list(map(lambda x : points[x], path)))

    # We're interested in all bits but the least significant (the start state)
    bits = (2**n - 1) - 1

    # Calculate optimal cost
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    cost, parent = min(res)

    # Backtrack to find full path
    path = []
    for _ in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    # Add implicit start state
    path.append(0)

    visitor(list(map(lambda x : points[x], path)), True)
    return list(map(lambda x : points[x], path))



def tspDPvisitorGetter(screen, points):
    def visitor(path, loop = False):
            screen.fill(BG_COLOR)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                elif event.type == pg.KEYDOWN:
                    raise Exception
            if loop:
                drawLoop(path, screen, (255, 0, 0), 4)
            else:
                drawPath(path, screen, (255, 0, 0), 4)
            drawPoints(points, screen)
            pg.display.flip()
            sleep(DELAY)
    return visitor
