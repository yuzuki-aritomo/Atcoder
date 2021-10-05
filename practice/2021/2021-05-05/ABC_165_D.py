import io
import sys
_INPUT = """\
11 10 9
"""
sys.stdin = io.StringIO(_INPUT)

import math
A, B, N = map(int, input().split())
ans = min(N, B-1)

print(math.floor(A*ans/B) - A*math.floor(ans/B))