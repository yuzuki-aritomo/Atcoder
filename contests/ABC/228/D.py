import io
import sys
_INPUT = """\
4
1 1048575
1 1048575
2 2097153
2 3
"""
sys.stdin = io.StringIO(_INPUT)

import sys
sys.setrecursionlimit(1000*1000)

N = 2**20
Q = int(input())

class Node:
  def __init__(self, id) -> None:
    self.id = id
    self.v = -1
    self.next = (id +1)%N
    self.pre = id - 1

M = [Node(i) for i in range(N)]

def dfs(h):
  if(M[h].v == -1):
    return h
  else:
    M[h].next = dfs(M[h].next%N)
    return M[h].next

def calc(x):
  h = dfs(x%N)
  M[h].v = x
  n = M[h].next
  p = M[h].pre
  M[n].pre = M[p].id
  M[p].next = M[n].id


for i in range(Q):
  c, x = map(int, input().split())
  if c==1:
    calc(x)
  else:
    print(M[x%N].v)