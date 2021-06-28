import io
import sys
_INPUT = """\
6
2 7 1 8 2 8
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))

M = [0, 0, 0]
for i in range(N):
  if(A[i]%4 == 0):
    M[2] += 1
  elif(A[i]%2 == 0):
    M[1] += 1
  else:
    M[0] += 1

if(M[1] > 0):
  M[0] += 1

if(M[0] <= M[2]+1):
  print("Yes")
else:
  print("No")
