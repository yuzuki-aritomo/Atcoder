import io
import sys
_INPUT = """\
4 3
3 5 6 7
2
5
3
"""
sys.stdin = io.StringIO(_INPUT)


N, Q = map(int, input().split())
A = list(map(int,input().split()))


M = dict()
C = []
tmp = A[0] - 1
M[tmp] = 1
C.append(tmp)
for i in range(1, N):
  tmp += A[i] - A[i - 1] - 1
  if(A[i] - A[i -1] == 1):
    continue
  M[tmp] = A[i-1]
  C.append(tmp)

C.append(tmp + 1)
M[tmp + 1] = A[-1]

# print(M)
# print(C)

import bisect

for i in range(Q):
  id = int(input())
  ind = bisect.bisect_left(C, id)
  if(ind > len(C)-1):
    ind -= 1
  if(ind == 0):
    ans = (id - 0)
  else:
    ans = M[C[ind]] + (id - C[ind-1])
  # print("ind:", ind)
  # print("C[ind]:", C[ind])
  print(ans)