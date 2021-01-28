
import io
import sys

_INPUT = """\
5
138 138 138 138 138
"""
sys.stdin = io.StringIO(_INPUT)

import bisect

N = int(input())
A = list(map(int,input().split()))
A.sort()

for i in range(N-1):
    n = A.pop(0)
    m = A.pop(0)
    b = (m+n)/2
    bisect.insort_left(A, b)
print(A[0])

