import io
import sys
_INPUT = """\
9
1 1
2 4
1 2
1 3
2 5
1 5
3
3
3
"""
sys.stdin = io.StringIO(_INPUT)


import heapq


Q = int(input())
A = []
tmp = [0 for i in range(Q)]
c = 0
for i in range(Q):
  Com = list(map(int,input().split()))
  # if(i != 0):
    # tmp[i] = tmp[i-1]
  if(Com[0] == 1):
    heapq.heappush(A, Com[1]-c,)
  elif(Com[0] == 2):
    # tmp[i] += Com[1]
    c += Com[1]
  else:
    ans = heapq.heappop(A)
    print(ans + c)

