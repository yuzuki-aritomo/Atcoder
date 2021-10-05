import io
import sys
from typing import Tuple
_INPUT = """\
3
8 8
4 4
5 4
3 3
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
x, y = map(int, input().split())
A = []
for _ in range(N):
  A.append(tuple(map(int,input().split())))
dp = [[0 for _ in range(300)] for _ in range(300)]
H = [[[] for _ in range(300)] for _ in range(300)]

for i in range(10):
  for j in range(10):
    if(i==0 and j==0):
      continue
    for id in range(len(A)):
      if not(id in H[i][j]):
        print(id)
        dp[i][j] = dp[max(i-1,0)][max(j-1,0)]+1
        H[i][j].append(id)
        break
    for id in range(len(A)):
      a = max(i - A[id][0], 0)
      b = max(j - A[id][1], 0)
      if(dp[a][b]+1 <  dp[i][j] and not(id in H[i][j])):
        dp[i][j] = dp[a][b]+1
        H[i][j].append(id)
      # dp[i][j] = min(dp[a][b]+1, dp[i][j])

ans = 301
for i in range(x, 300):
  for j in range(y, 300):
    ans = min(dp[i][j], ans)
print(dp)
print(H)
print(dp[9][9])
print(H[8][8])
print(ans)
