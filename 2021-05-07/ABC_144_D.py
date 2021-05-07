import io
import sys

from numpy.core.fromnumeric import partition
_INPUT = """\
12 21 10
"""
sys.stdin = io.StringIO(_INPUT)

import math

a, b, x = map(int, input().split())


if(a*a*b/2 > x):
    #下が三角形
    ans = math.degrees(math.atan(2*x/(a*b*b)))
    print(90- ans)
else:
    #上が三角形
    y = 2*(b-x/(a**2))
    ans = math.degrees(math.atan(y/a))
    print(ans)