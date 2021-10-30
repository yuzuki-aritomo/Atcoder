import io
import sys
_INPUT = """\
7 14
1 6 3
1 4 1
1 5 2
1 2 7
1 3 5
3 2
3 4
3 6
2 3 5
2 4 1
1 1 5
3 2
3 4
3 6
"""
sys.stdin = io.StringIO(_INPUT)

class Node:
  def __init__(self, id) -> None:
    self.id = id
    self.left = -1
    self.right = -1

N, Q = map(int, input().split())
M = [Node(i) for i in range(N+1)]

from collections import deque
def put(u):
  ans = deque()
  id = u
  while(True):
    ans.append(id)
    if M[id].right == -1:
      break
    id = M[id].right
  ans.popleft()
  id = u
  while(True):
    ans.appendleft(id)
    if M[id].left == -1:
      break
    id = M[id].left
  print(len(ans)," ".join(map(str, ans)))

for i in range(Q):
  C = list(map(int,input().split()))
  if C[0] == 1:
    M[C[1]].right = C[2]
    M[C[2]].left = C[1]
  elif C[0]==2:
    M[C[1]].right = -1
    M[C[2]].left = -1
  else:
    put(C[1])