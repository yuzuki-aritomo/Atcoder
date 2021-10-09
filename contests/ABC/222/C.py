import io
import sys
_INPUT = """\
2 3
GCP
PPP
CCC
PPC
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
H = []
for i in range(2*N):
  H.append(input())

A = [[0, i] for i in range(2*N)]

for j in range(M):
  for i in range(N):
    a, b = A[2*i], A[2*i+1]
    ah = H[a[1]][j]
    bh = H[b[1]][j]
    if(ah == bh):
      continue
    elif(
      (ah=="G" and bh=="C")or
      (ah=="C" and bh=="P")or
      (ah=="P" and bh=="G")
      ):
      A[2*i][0] -= 1
    else:
      A[2*i+1][0] -= 1
  A.sort()

for item in A:
  print(item[1]+1)
# print(A)
