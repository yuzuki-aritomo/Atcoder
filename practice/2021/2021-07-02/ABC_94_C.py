import io
import sys
_INPUT = """\
6
5 5 4 4 3 3
"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())
M = list(map(int,input().split()))

A = M.copy()
A.sort()
Flag = A[N//2]
for i in range(N):
  if(M[i] < Flag):
    print(A[N//2])
  else:
    print(A[N//2-1])
