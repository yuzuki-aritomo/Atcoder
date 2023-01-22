import io
import sys
_INPUT = """\
3 100001
1 50
2 50
1 50
1 1
2 1
1 1
2 1
100 10
"""
sys.stdin = io.StringIO(_INPUT)


N, X = map(int, input().split())

M = []
for i in range(N):
  a, b = map(int, input().split())
  for j in range(b):
    M.append(a)

A = {}
A[0] = 0

for i in range(len(M)):
  T = []
  for key in A:
    tmp = key + M[i]
    if(tmp > X):
      continue
    T.append(tmp)
  for t in T:
    A[t] = 0

if(X in A):
  print("Yes")
else:
  print("No")

