
import io
import sys
_INPUT = """\
0.2 0.8 1.1
"""
sys.stdin = io.StringIO(_INPUT)

import math

X, Y, R = map(float, input().split())
ans = 0
for i in range(int(X-R), int(X+R)+1):
    a = math.sqrt(R**2 - (i-X)**2)
    b = int(a+Y)
    if(Y-a<0):
        c = int(Y-a) - 1
    else:
        c = int(Y-a)
    # if(b==c):
    #     ans += 1
    #     continue
    if(float(c) == Y-a):
        c += -1
    ans += b - c
    # print("i:", i)
    # print(a)
    # print("b:", b)
    # print("c:", c)
    # print("b:", b-c)
print(ans)
