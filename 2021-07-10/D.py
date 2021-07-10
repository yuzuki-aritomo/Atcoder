import io
import sys
_INPUT = """\
9 9
2 3
5 6
4 8
8 9
4 5
3 4
1 9
3 7
7 9
2 5
2 6
4 6
2 4
5 8
7 8
3 6
5 6

"""
sys.stdin = io.StringIO(_INPUT)

N, C = map(int, input().split())
M = [[] for _ in range(N+1)]
for _ in range(N-1):
  a, b = map(int, input().split())
  M[a].append(b)
  M[b].append(a)

from collections import deque

Q = deque()
path = [0 for i in range(N+1)]
color = [0 for i in range(N+1)]
Q.append(1)
while(len(Q)>0):
  q = Q.popleft()
  color[q] = 1
  for item in M[q]:
    if(color[item]==0):
      Q.append(item)
      path[item] = path[q] + 1

for _ in range(C):
  a, b = map(int, input().split())
  if((path[a]+path[b])%2 == 0):
    print("Town")
  else:
    print("Road")
