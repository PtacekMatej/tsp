from tspBrute import *
from tspDP import *
from tspConvHull import *
import random

def test():
    for _ in range(10):
        points = [(random.randint(0, 1000000), random.randint(0, 1000000)) for _ in range(7)]
        brute = tspBrute(points, lambda x , _ : x)
        dp = tspDP(points, lambda x, _ = False : x)
        ch = tspConvHull(points, lambda x : x)
        while dp[0] != brute[0]:
            dp.append(dp[0])
            dp.pop(0)
        if dp[1] != brute[1]:
            dp = list(reversed(dp))
            while dp[0] != brute[0]:
                dp.append(dp[0])
                dp.pop(0)
        while ch[0] != brute[0]:
            ch.append(ch[0])
            ch.pop(0)
        if ch[1] != brute[1]:
            ch = list(reversed(ch))
            while ch[0] != brute[0]:
                ch.append(ch[0])
                ch.pop(0)
        assert(brute == dp)
        assert(brute == ch)
    
    print("all tests passed")
