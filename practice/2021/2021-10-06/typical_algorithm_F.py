import io
import sys
_INPUT = """\
5 7
0 1 10
0 4 30
1 2 10
1 4 20
2 3 30
4 2 20
4 3 10
"""
sys.stdin = io.StringIO(_INPUT)

class Node():
  def __init__(self, id) -> None:
    self.id = id
    self.children = []

n, m = map(int, input().split())
N = [Node(i) for i in range(n)]
for _ in range(m):
  s, g, c = map(int, input().split())
  N[s].children.append((c, g))
  N[g].children.append((c, s))

import heapq
def prim():
  isPath = [0 for _ in range(n)]
  cost = 0
  H = [] # list of (cost, index)

  isPath[0] = 1
  for node in N[0].children:
    heapq.heappush(H, (node))

  while(len(H)>0):
    u = heapq.heappop(H) #(cost, index)
    c = u[0]
    id = u[1]
    if(isPath[id]==1):
      continue
    isPath[id] = 1
    cost += c
    for node in N[id].children: #node = (index, cost)
      if(isPath[node[1]] == 0):
        heapq.heappush(H, (node))
  
  return cost

ans = prim()
print(ans)


