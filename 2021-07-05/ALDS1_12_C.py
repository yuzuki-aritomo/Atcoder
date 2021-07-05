import io
import sys
_INPUT = """\
5
0 3 2 3 3 1 1 2
1 2 0 2 3 4
2 3 0 3 3 1 4 1
3 4 2 1 0 1 1 4 4 3
4 2 2 1 3 3
"""
sys.stdin = io.StringIO(_INPUT)

import heapq

def dijkstra(N, M):
  color = [True for _ in range(N)]
  Cost = [float("inf") for _ in range(N)]
  Cost[0] = 0
  H = [(0, 0)]
  heapq.heapify(H)

  while(len(H)>0):
    tmp = heapq.heappop(H)
    u = tmp[1] #node_index
    if(tmp[0] > Cost[u]):
      continue
    color[u] = False
    for i in range(N):
      if(M[u][i] != float("inf") and color[i]):
        if(Cost[u] + M[u][i] < Cost[i]):
          Cost[i] = Cost[u] + M[u][i]
          heapq.heappush(H, (Cost[i], i))

  for i in range(len(Cost)):
    print(i, Cost[i])

def main():
  N = int(input())
  M = [[float("inf") for _ in range(N)] for _ in range(N)]
  for i in range(N):
    A = list(map(int,input().split()))
    for j in range(2, len(A)-1, 2):
      M[i][A[j]] = min(M[i][A[j]], A[j+1])

  dijkstra(N, M)

main()