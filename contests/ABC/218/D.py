import io
import sys
_INPUT = """\
7
0 1
1 0
2 0
2 1
2 2
3 0
3 2
"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())
M = []
for i in range(N):
  M.append(tuple(map(int,input().split())))

from collections import defaultdict
A = defaultdict(int)

for i in range(N):
  u = str(M[i][0])+"+"+str(M[i][1])
  A[u] = 1

# print(A)
def solve(i, j):
  x0 = M[i][0]
  y0 = M[i][1]
  x1 = M[j][0]
  y1 = M[j][1]
  if(x0==x1 or y0 ==y1):
    return False
  else:
    u0 = str(x0)+"+" + str(y1)
    u1 = str(x1)+"+" + str(y0)
    if(A[u0] ==1 and A[u1] == 1):
      # print(u0, u1)
      # print(i,j)
      return True

ans = 0
for i in range(N):
  for j in range(i+1, N):
    if solve(i,j):
      ans += 1
print(ans//2)