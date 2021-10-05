import io
import sys
_INPUT = """\
10 10 100 1
"""
sys.stdin = io.StringIO(_INPUT)

N, A, X, Y = map(int, input().split())

if(N<=A):
  print(X*N)
else:
  print(X*A + Y*(N-A))
