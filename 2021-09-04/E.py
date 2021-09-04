import io
import sys
_INPUT = """\
11
1 4
1 3
1 2
1 1
2
3
1 0
2
2
2
2
"""
sys.stdin = io.StringIO(_INPUT)

import heapq

Q = int(input())
A = []
H = []
id = 0
for i in range(Q):
  w = list(map(int,input().split()))
  if(w[0] == 1):
    A.append(w[1])
  elif(w[0] == 2):
    if(len(H)>0):
      print(heapq.heappop(H))
    else:
      print(A[id])
      id += 1
  else:
    for item in A[id:]:
      heapq.heappush(H, item)
    A = []
    id = 0
