import io
import sys
_INPUT = """\
5
-1 2 3 1 -1
2 -1 -1 4 -1
3 -1 -1 1 1
1 4 1 -1 3
-1 -1 1 3 -1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
INF = float("inf")
M = []
for _ in range(N):
  M.append(list(map(int,input().split())))
for i in range(N):
  for j in range(N):
    if(M[i][j] == -1):
      M[i][j] = INF

import heapq
def prim():
  color = [0 for _ in range(N)]
  D = [] #list of [cost, index]
  cost = 0
  
  #first node
  for i in range(N):
    heapq.heappush(D, (M[0][i], i))
  color[0] = 1

  #calc cost
  while(len(D)>0):
    u = heapq.heappop(D) #[cost, index]
    if(color[u[1]]==1): #is pathed
      continue
    color[u[1]] = 1
    cost += u[0]
    for i in range(N):
      if(color[i] == 0):
        heapq.heappush(D, (M[u[1]][i], i))
  return cost

ans = prim()
print(ans)

