import io
import sys
_INPUT = """\
6
0 6 7 6 7 0
"""
sys.stdin = io.StringIO(_INPUT)


from collections import deque

N = int(input())
A = list(map(int,input().split()))

B = deque()

for i in range(N):
  if(i%2 == 0):
    B.append(A[i])
  else:
    B.appendleft(A[i])

if(N%2 == 0):
  print(" ".join(map(str, B)))
else:
  C = list(B)[::-1]
  print(" ".join(map(str, C)))