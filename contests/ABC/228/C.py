import io
import sys
from typing import Tuple
_INPUT = """\
4 2
127 235 78
192 134 298
28 56 42
96 120 250
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = []
for i in range(N):
  s = sum(list(map(int,input().split())))
  A.append(s)

B = sorted(A)
# print(B)

import bisect
# print(A)

for i in range(N):
  id = bisect.bisect_right(B, A[i]+300)
  id = N-id+1
  # print(id)
  if(id <= K):
    print("Yes")
  else:
    print("No")