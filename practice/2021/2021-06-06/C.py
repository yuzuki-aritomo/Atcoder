import io
import sys
_INPUT = """\
4 4
1 2
2 3
3 4
4 1
"""
sys.stdin = io.StringIO(_INPUT)

import sys
sys.setrecursionlimit(1000*1000)


N, M = map(int, input().split())

R = [[] for i in range(N+1)]
for i in range(M):
  a, b = map(int, input().split())
  R[a].append(b)


def dfs(id):
  if(path[id] == 1): return
  path[id] = 1
  for item in R[id]:
    dfs(item)

ans = 0
for i in range(1, N+1):
  path =[0] * (N+1)
  dfs(i)
  ans += sum(path)

print(ans)