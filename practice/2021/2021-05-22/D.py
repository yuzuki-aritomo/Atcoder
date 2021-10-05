import io
from itertools import filterfalse
import sys
_INPUT = """\
30 30 118264581564861424
"""
sys.stdin = io.StringIO(_INPUT)


from operator import mul
from functools import reduce

A, B, K = map(int, input().split())
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N = cmb(A+B, A)

import math
Ans = ""
while (True):
    if(K<N):
        Flag = True
        Ans += "a"
    elif(K>N):
        Flag = False
        Ans += "b"
    else:
        break

print(Ans)

