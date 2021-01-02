import io
import sys

_INPUT = """\
2 3 100
"""
sys.stdin = io.StringIO(_INPUT)

import math

A,B,M = map(int,input().split())





lcm = A*B / math.gcd(A,B)
print(int(lcm%M))

