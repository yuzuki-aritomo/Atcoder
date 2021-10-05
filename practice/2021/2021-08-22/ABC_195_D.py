import io
import sys
_INPUT = """\
3 4 3
1 9
5 3
7 8
1 8 6 9
4 4
1 4
1 3
"""
sys.stdin = io.StringIO(_INPUT)


N, M ,Q = map(int, input().split())
A = []
for _ in range(N):
  _a, _b = map(int,input().split())
  A.append([_b, _a])
B = list(map(int,input().split()))
A.sort(key=lambda x:(x[0], -x[1]), reverse=True)
# print(A)

def solve(l, r):
  b = B[0:l-1].copy() + B[r:len(B)].copy()
  b.sort()
  # print(b)
  i = 0
  ans = 0
  while(len(b)>0):
    if(i==len(A)):
      return ans
    for j in range(len(b)):
      if(b[j]>=A[i][1]):
        ans += A[i][0]
        del b[j]
        break
    i += 1
  return ans

for _ in range(Q):
  l, r = map(int,input().split())
  ans = solve(l, r)
  print(ans)


