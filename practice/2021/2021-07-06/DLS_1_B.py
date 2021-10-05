import io
import sys
from typing import Tuple
_INPUT = """\
6
2 1
2 2
4 2
6 2
3 3
5 4
2
2 4 0 4
4 10 2 5
"""
sys.stdin = io.StringIO(_INPUT)


class Node:
  locationX = 0
  def __init__(self, id) -> None:
    self.id = id
    self.l = -1 #index
    self.r = -1 #index
    # self.locationX = x
    # self.locationY = y

def findSet(v, x0, y0, x1, y1):
  x = T[v].x
  if(x0<=x and x<=x1):
    return v
  return


def makeTree(l, r):
  if not l<r:
    return -1
  mid = (l+r)//2
  # T[mid].x = M[mid][0]
  # T[mid].y = M[mid][1]
  T[mid].x = M[mid]
  T[mid].l = makeTree(l, mid)
  T[mid].r = makeTree(mid+1, r)
  return T[mid].id

N = int(input())
M = []
for _ in range(N):
  # M.append(list(map(int, input().split())))
  a,b = map(int, input().split())
  M.append(a)
M.sort()

T = [Node(i) for i in range(N)]
makeTree(0, N)

for i in range(N):
  print(T[i].id, T[i].l, T[i].r, T[i].x)
print(M)
Q = int(input())
for _ in range(Q):
  x0, x1, y0, y1 = map(int, input().split())
  findSet(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1))

