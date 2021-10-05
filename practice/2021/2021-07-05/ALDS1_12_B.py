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

N = int(input())
M = [[float("inf") for _ in range(N)] for _ in range(N)]
for i in range(N):
  A = list(map(int,input().split()))
  for j in range(2, len(A)-1, 2):
    M[i][A[j]] = min(M[i][A[j]], A[j+1])

color = [0 for _ in range(N)]
Cost = [float("inf") for _ in range(N)]
Cost[0] = 0

while(True):
  minCost = float("inf")
  for i in range(N):
    if(color[i] == 0 and minCost > Cost[i]):
      minCost = Cost[i]
      u = i
  if(minCost == float("inf")):
    break
  color[u] = 1
  for i in range(N):
    if(M[u][i] != float("inf") and color[i] == 0):
      Cost[i] = min(Cost[u] + M[u][i], Cost[i])

# for item in M:
#   print(item)

# print("Cost:", Cost)
for i in range(len(Cost)):
  print(i, Cost[i])