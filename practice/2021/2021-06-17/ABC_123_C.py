import io
import sys
_INPUT = """\
10000000007
2
3
5
7
11
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = []
for i in range(5):
  A.append(int(input()))

F = 0
for i in range(5):
  if(A[i] == min(A)):
    F = i
    break

import math

print(math.ceil(N / A[F]) + 4)