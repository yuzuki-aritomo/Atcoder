import io
import sys
_INPUT = """\
5 12
0 1 4
0 2 3
1 1 2
1 3 4
1 1 4
1 3 2
0 1 3
1 2 4
1 3 0
0 0 4
1 0 2
1 3 0
"""
sys.stdin = io.StringIO(_INPUT)

class Union:
  id = []
  p = []
  rank = []
  def __init__(self, n) -> None:
    self.id = [i for i in range(n)]
    self.p = [i for i in range(n)]
    self.rank = [i for i in range(n)]

  def unite(self, x, y):
    self.linkSet(self.findSet(x), self.findSet(y))
    return

  def linkSet(self, x, y):
    if(self.rank[x] == self.rank[y]):
      self.p[x] = y
      self.rank[x] += 1
    elif(self.rank[x] > self.rank[y]):
      self.p[y] = x
    else:
      self.p[x] = y
    return

  def findSet(self, u):
    parent = self.p[u]
    while(True):
      if(parent == self.p[parent]):
        break
      parent = self.p[parent]
    return parent

  def same(self, x, y):
    return self.findSet(x) == self.findSet(y)


N, Q = map(int, input().split())
Uni = Union(N)
for i in range(Q):
  com,x,y = map(int, input().split())
  if(com == 0):
    Uni.unite(x, y)
  else:
    if Uni.same(x, y):
      print(1)
    else:
      print(0)
