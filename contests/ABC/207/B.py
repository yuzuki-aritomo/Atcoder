import io
import sys
_INPUT = """\
5 1 1 1
"""
sys.stdin = io.StringIO(_INPUT)

A, B, C, D =  map(int, input().split())

# A + B*n < (C*n )*D
if(B >= C*D):
  print(-1)
else:
  for i in range(10**6):
    if(A + B*i <= C*i*D):
      print(i)
      exit()
