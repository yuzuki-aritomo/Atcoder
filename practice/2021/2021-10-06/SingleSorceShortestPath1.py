import io
import sys
from typing import Deque
_INPUT = """\
5
0 3 2 3 3 1 1 2
1 2 0 2 3 4
2 3 0 3 3 1 4 1
3 4 2 1 0 1 1 4 4 3
4 2 2 1 3 3
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
INF = float("inf")
M = [[INF for _ in range(N)] for _ in range(N)]
for _ in range(N):
  C = list(map(int,input().split()))
  for i in range(C[1]):
    M[C[0]][C[(i+1)*2]] = C[(i+1)*2+1]

for i in range(N):
  M[i][i] = 0

# for item in M:
#   print(item)


def Dijkstra():
  color = [0 for _ in range(N)]
  cost = [INF for _ in range(N)]
  H = []

  color[0] = 1
  for i in range(N):
    cost[i] = M[0][i]

  while(True):
    #訪問していない中で最もコストが小さなノードのindexを取得
    minCost = INF
    for i in range(N):
      if(color[i]==0 and cost[i]<minCost):
        minCost = cost[i]
        id = i
    
    #すべて訪問済み
    if(minCost == INF):
      break
    
    #costに対してidを経由した方がいいのかどうかを更新
    color[id] = 1
    for i in range(N):
      cost[i] = min(cost[i], cost[id]+M[id][i])
  # print(cost)
  for i in range(N):
    print(i, cost[i])
  return

Dijkstra()

