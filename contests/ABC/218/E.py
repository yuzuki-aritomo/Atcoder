import io
import sys
_INPUT = """\
4 5
1 2 1
1 3 1
1 4 1
3 2 2
4 2 2
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = [0 for i in range(N)]
E = []
for i in range(M):
  a, b, c = map(int, input().split())
  A[a-1] += 1
  A[b-1] += 1
  E.append([c, a-1, b-1])
E.sort(reverse=True)
ans = 0
for i in range(M):
  x = E[i][1]
  y = E[i][2]
  if(E[i][0]<=0):
    break
  if(A[x]>1 and A[y]>1):
    A[x] -= 1
    A[y] -= 1
    ans += E[i][0]

print(ans)
