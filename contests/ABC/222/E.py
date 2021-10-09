import io
import sys
_INPUT = """\
4 5 0
2 3 2 1 4
1 2
2 3
3 4
"""
sys.stdin = io.StringIO(_INPUT)

n, m, k = map(int, input().split())
M = list(map(int,input().split()))

class Node:
  def __init__(self, id) -> None:
    self.id = id
    self.p = 0
    self.child = []

N = [Node(i) for i in range(n)]
for i in range(n-1):
  a,b = map(int,input().split())
  N[a-1].child.append(b-1)
  N[b-1].child.append(a-1)

from collections import deque
def find(s, g):
  color = [0 for i in range(n)]
  color[s] = 1
  d = deque()
  d.append(s)
  while(True):
    u = d.popleft()
    color[u] = 1
    for item in N[u].child:
      if(item == g):
        N[item].p = u
        return
      if(color[item]==0):
        d.append(item)
        N[item].p = u

def findParent(s, g):
  ans = [g]
  c = g
  while(True):
    ans.append(N[c].p)
    if(s == N[c].p):
      return ans[::-1]
    c = N[c].p


Path = []
for k in range(1, len(M)):
  i,j = M[k-1]-1, M[k]-1
  find(i, j)
  tmp = findParent(i, j)
  # print(tmp)
  if(k==1):
    Path = tmp
  else:
    Path.extend(tmp[1:])
print(Path)

from collections import Counter
Cnt = Counter()

for i in range(1, len(Path)):
  a = min(Path[i-1],Path[i])
  b = max(Path[i-1],Path[i])
  key = str(a)+"+"+str(b)
  Cnt[key] += 1

print(Cnt)
