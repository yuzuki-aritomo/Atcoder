import io
import sys
_INPUT = """\
8
2 2 3 1 2 3 2 2
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))

Ans = 0
i = 0
while(i<N):
  if(i == N-1):
    Ans += 1
    break
  if(A[i] == A[i+1]):
    i += 1
    continue
  elif(A[i] < A[i+1]):
    while(i<N-1 and A[i] <= A[i+1]):
      i += 1
    i += 1
    Ans += 1
  elif(A[i] > A[i+1]):
    while(i<N-1 and A[i] >= A[i+1]):
      i += 1
    i += 1
    Ans += 1

print(Ans)