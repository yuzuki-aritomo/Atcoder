import io
import sys
_INPUT = """\
6
5 3
7 4
"""
sys.stdin = io.StringIO(_INPUT)

import math
N = int(input())
p0 = list(map(int,input().split()))
pn = list(map(int,input().split()))

O = [ (p0[0] + pn[0])/2 , (p0[1] + pn[1])/2 ]
Theta = math.radians(360/N)

p0_O = [p0[0] - O[0], p0[1] - O[1]]

x = p0_O[0]*math.cos(Theta) - p0_O[1]*math.sin(Theta)
y = p0_O[0]*math.sin(Theta) + p0_O[1]*math.cos(Theta)

X = x + O[0]
Y = y + O[1]

print(X, Y)