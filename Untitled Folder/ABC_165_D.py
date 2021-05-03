import io
import sys
_INPUT = """\
11 10 9
"""
sys.stdin = io.StringIO(_INPUT)

import math
A, B, N = map(int, input().split())

X = min(B-1, N)
print(math.floor(A*X/B) - A*math.floor(X/B))
