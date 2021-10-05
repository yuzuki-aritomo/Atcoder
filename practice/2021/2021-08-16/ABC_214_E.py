import io
import sys
_INPUT = """\
1
5
1 1
1 2
4 4
4 4
5 5
"""
sys.stdin = io.StringIO(_INPUT)

import heapq
def solve():
  n = int(input())
  A = []
  MustFinish = []
  x = 1
  for _ in range(n):
    _a = tuple(map(int, input().split()))
    A.append(_a)
  A.sort()
  INF = 100100100
  A.append((INF, INF))
  print(A)
  for i in range(n+1):
    l = A[i][0]
    r = A[i][1]
    print(l,r)
    while(len(MustFinish)>0 and x<l):
      # print(MustFinish)
      if(MustFinish[0]<x):
        return False
      heapq.heappop(MustFinish)
      # print(MustFinish)
      x += 1
    x = l
    heapq.heappush(MustFinish ,r)
    # print(MustFinish)
  return True

N = int(input())
for _ in range(N):
  if(solve()):
    print("Yes")
  else:
    print("No")