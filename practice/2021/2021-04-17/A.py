import io
import sys
_INPUT = """\
1000 1 1
"""
sys.stdin = io.StringIO(_INPUT)

import math
X, Y , Z = map(int, input().split())

ans = (Z*Y / X)
if(Z*Y % X == 0):
    print(int(ans - 1))
else:
    print(math.floor(ans))