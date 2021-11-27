import io
import sys
_INPUT = """\
8 7
7 8
3 4
5 6
5 7
5 8
6 7
6 8

"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
class Node:
  def __init__(self, id) -> None:
    self.id = id
    self.c = []
A = [Node(i) for i in range(1+N)]
for i in range(M):
  a0, b0 = map(int, input().split())
  a = max(a0, b0)
  b = min(a0, b0)
  A[b].c.append(a)


import sys
p = [i for i in range(N+1)]#have parent node
sys.setrecursionlimit(1000*1000)
def findRoot(x):
  if p[x] == x:
    return x
  else:
    p[x] = findRoot(p[x])
    return p[x]
def same(a, b):
  return findRoot(a)==findRoot(b)
def unite(a, b):
  p[findRoot(a)] = findRoot(b)
  return

Ans = [0 for i in range(N+1)]
ans = 0
for i in range(N):
  id = N-i
  ans += 1
  for child in A[id].c:
    if not same(child, id):
      ans -=1
      unite(child, id)
  Ans[id] = ans

# print(Ans)
for i in range(2, N+1):
  print(Ans[i])
print(0)