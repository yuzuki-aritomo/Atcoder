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

N, M = map(int, input().split())


for i in range(M):
  a, b = map(int, input().split())
  A[a].child.append(b)

Ans =  [[0 for i in range(N+1)] for i in range(N+1)]
def dfs(id, Parent):
  Parent.append(id)
  for item in Parent:
    Ans[item][id] = 1
  for item in A[id].child:
    if(path[item] == 0):
      path[item] = 1
      dfs(item, Parent)
  Parent.pop()

for i in range(1, N+1):
  path =[0] * (N+1)
  dfs(i, [])

ans = 0
for i in range(1, N+1):
  for j in range(1, N+1):
    if(Ans[i][j] == 1):
      ans += 1

print(ans)