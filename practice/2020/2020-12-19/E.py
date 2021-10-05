import io
import sys

_INPUT = """\
4
10 4 3
1000 11 2
998244353 897581057 595591169
10000 6 14
"""
sys.stdin = io.StringIO(_INPUT)

import math

T = int(input())

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

for i in range(T):
    N, S, K = map(int, input().split())
    print(lcm(N, K))
    A = []