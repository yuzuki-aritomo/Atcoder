import io
import sys
_INPUT = """\
7 8
1 3
1 4
2 3
2 4
2 5
2 6
5 7
6 7
"""
sys.stdin = io.StringIO(_INPUT)

mod = 10**9+7

N, M = map(int, input().split())
A = [[] for i in range(N+1)]
for i in range(M):
  a, b = map(int, input().split())
  A[a].append(b)
  A[b].append(a)

from collections import deque
from collections import Counter

Q = deque()
color = [0 for i in range(N+1)]
Ans = Counter()
tmp = Counter()
Q.append(1)
Q.append(0)
Flag = False
while(len(Q)>0):
  q = Q.popleft()
  if(q == 0):
    if(len(Q) == 0):
      print(0)
      exit()
    Q.append(0)
    Ans = Ans + tmp
    continue
  color[q] = 1
  for item in A[q]:
    if(item == N):
      Flag = True
      break
    tmp[item] = (tmp[item]+1)%mod
    if(color[item] == 0):
      Q.append(item)
  if Flag:
    if(q == 1):
      ans = 0
      for item in A[1]:
        if(item == N):
          ans += 1
      print(ans)
      exit()
    break

# print(Ans)
# print(A)

ans = 0
for i in range(1, N+1):
  for item in A[i]:
    # print(item)
    if(item == N):
      ans += Ans[i]%mod

print(ans%mod)