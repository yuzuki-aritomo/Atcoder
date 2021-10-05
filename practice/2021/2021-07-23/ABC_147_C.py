import io
import sys
from typing import Tuple
_INPUT = """\
3
2
2 1
3 0
2
3 1
1 0
2
1 1
2 0

"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())
A = [dict()]

for i in range(N):
  k = int(input())
  A.append(dict())
  for j in range(k):
    a,b = map(int, input().split())
    A[i][a-1] = b


def checkLie(bit):
  global N
  for i in range(N):
    if(bit[i] == 1):
      for item in A[i]:
        if(A[i][item] != bit[item]):
          return False
  return True

from itertools import product
Ans = 0
for bit in product([0, 1], repeat=N):
  if(bit.count(1) <= Ans):
    continue
  if(checkLie(bit)):
    tmp = bit.count(1)
    Ans = max(Ans, tmp)

print(Ans)
