import io
import sys
_INPUT = """\
1 1 0
"""
sys.stdin = io.StringIO(_INPUT)

import math

R, X, Y = map(int, input().split())

L = X*X + Y*Y
L = math.sqrt(L)
print(L)
ans = math.ceil(L/R)
print(ans)


