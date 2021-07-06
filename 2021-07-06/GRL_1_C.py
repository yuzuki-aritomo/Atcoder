import io
import sys
_INPUT = """\
4 6
0 1 1
0 2 5
1 2 2
1 3 4
2 3 1
3 2 7
"""
sys.stdin = io.StringIO(_INPUT)

V, E = map(int, input().split())
M = [[float("inf") for _ in range(V)] for _ in range(V)]
for _ in range(E):
  p0, p1, c = map(int, input().split())
  M[p0][p1] = c

def Warshall(V):
  for i in range(V):
    for j in range(V):
      for k in range(V):
        M[i][j] = min(M[i][j], M[i][k]+ M[k][j])

for i in range(V):
  M[i][i] = 0

Warshall(V)
# print(M)
for i in range(V):
  if(M[i][i] < 0):
    print("NEGATIVE CYCLE")
    exit()
for i in range(len(M)):
  ans = ""
  for j in range(len(M)):
    if(M[i][j]==float("inf")):
      # print("INF", end="")
      ans += "INF "
    else:
      # print(M[i][j], end="")
      ans += str(M[i][j])+ " "
  print(ans[:-1])

