import io
import sys
_INPUT = """\
3 4 4
"""
sys.stdin = io.StringIO(_INPUT)

import math
R, X, Y = map(int, input().split())

n = 3.1
L = math.sqrt(X**2 + Y**2)
if(L<R):
    print(2)
    exit()
else:
    print(math.ceil(L/R))


