import io
import sys
_INPUT = """\
1000000000
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

A = [0]
i = 1
while(True):
  A.append(A[-1] + i)
  if(A[i] >= N):
    print(i)
    break
  i += 1