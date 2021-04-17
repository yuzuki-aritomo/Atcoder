import io
import sys
_INPUT = """\
45108 2571593
"""
sys.stdin = io.StringIO(_INPUT)

import math

N, P = map(int, input().split())

A = P-1
S = 1
# for i in range(N):
#     S += S*(A-i)

tmp = 10**9 + 7

S = (P-1)*((P-2)**(N-1))
if(S<=0):
    print(0)
    exit()

print(S%tmp)