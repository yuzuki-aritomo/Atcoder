import io
import sys
_INPUT = """\
5
1 2
1 3
1 9
2 9
3 9
3 9 2 4 5 6 7 8
"""
sys.stdin = io.StringIO(_INPUT)

class node:
  def __init__(self, id):
    self.id = id
    self.c = []
G = [node(i) for i in range(9)]

M = int(input())
for i in range(M):
  a, b = map(int,input().split())
  G[a-1].c.append(b-1)
  G[b-1].c.append(a-1)
P = list(map(int,input().split()))
for i in range(len(P)):
  P[i] -= 1

print(G)

from collections import deque

def check(n, P):
  Q = deque()
  color = [0 for _ in  range(9)]
  cost = [0 for _ in  range(9)]
  Q.append(n)
  while(len(Q)>0):
    u = Q.popleft()
    color[u] = 1
    for item in G[u].c:
      if(P[item] == u):
        print(cost)
        return 
      if color[item]==0:
        Q.append(u)
        cost[item] = cost[u]+1

print(P)
check(2, P)
