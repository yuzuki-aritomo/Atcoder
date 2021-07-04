import io
import sys
_INPUT = """\
5 20
1 2 6
1 3 10
1 4 4
1 5 1
2 1 5
2 3 9
2 4 8
2 5 6
3 1 5
3 2 1
3 4 7
3 5 9
4 1 4
4 2 6
4 3 4
4 5 8
5 1 2
5 2 5
5 3 6
5 4 5
"""
sys.stdin = io.StringIO(_INPUT)

import sys
sys.setrecursionlimit(1000*1000)
import itertools
from collections import defaultdict

class Node:
  def __init__(self, id):
    self.id = id
    self.child = []
    self.cost = defaultdict(lambda: float("inf"))

N, M = map(int, input().split())
A = [Node(i) for i in range(N+1)]

for _ in range(M):
  a,b,c = map(int, input().split())
  A[a].child.append(b)
  A[a].cost[b] = min(A[a].cost[b], c)


Cost = []
M = []
m = []
# i から j
def dfs(i, j, c):
  global Cost
  if(i == j):
    Cost.append(c)
    M.append(m.copy())
  for item in A[i].child:
    if item in m:
      continue
    m.append(item)
    dfs(item, j, c +A[i].cost[item])
    m.pop()

# m.append(1)
# dfs(1, 3, 0)
# print(M)
# print(Cost)

L = [i for i in range(1, N+1)]
Ans = 0
for v in itertools.combinations_with_replacement(L, 2):
  if(v[0] == v[1]):
    continue
  Cost = []
  M = []
  m = []
  dfs(v[0], v[1], 0)
  tmp = defaultdict(lambda: float("inf"))
  # print("M:", M)
  # print("Cost:", Cost)
  for i in range(len(Cost)):
    # ans.append([max(M[i]), Cost[i]])
    M[i].pop()
    if(M[i] == []):
      M[i] = [1]
    tmp[max(M[i])] = min(Cost[i], tmp[max(M[i])])
  ans = []
  for item in tmp:
    ans.append([item, tmp[item]])
  ans.sort()
  # print("v:", v)
  # print("ans:", ans)
  tmp = 0
  for i in range(len(ans)):
    if(tmp > ans[i][1]):
      continue
    Ans += (N+1-ans[i][0])*(ans[i][1] - tmp)
    tmp = ans[i][1]
  # print("Ans:", Ans)
  Cost = []
  M = []
  m = []
  dfs(v[1], v[0], 0)
  tmp = defaultdict(lambda: float("inf"))
  # print("M:", M)
  # print("Cost:", Cost)
  for i in range(len(Cost)):
    # ans.append([max(M[i]), Cost[i]])
    M[i].pop()
    if(M[i] == []):
      M[i] = [1]
    tmp[max(M[i])] = min(Cost[i], tmp[max(M[i])])
  ans = []
  for item in tmp:
    ans.append([item, tmp[item]])
  ans.sort()
  # print("v:", v)
  # print("ans:", ans)
  tmp = 0
  for i in range(len(ans)):
    if(tmp > ans[i][1]):
      continue
    Ans += (N+1-ans[i][0])*(ans[i][1] - tmp)
    tmp = ans[i][1]

print(Ans)

# A = [[1,1],[3, 2], [3, 1], [1, 2]]
# A.sort()
# print(A)