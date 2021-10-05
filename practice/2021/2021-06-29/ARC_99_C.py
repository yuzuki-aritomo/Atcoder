import io
import sys
_INPUT = """\
4 3
2 3 1 4
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = list(map(int,input().split()))

import math
print(math.ceil((N-K)/(K-1)) + 1)