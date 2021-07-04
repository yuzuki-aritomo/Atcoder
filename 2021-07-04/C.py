import io
import sys
_INPUT = """\
7 1000000000000
99 8 2 4 43 5 3
"""
sys.stdin = io.StringIO(_INPUT)


N, K = map(int, input().split())
A = list(map(int,input().split()))
B = A.copy()
B.sort()

a = K//N
m = K%N

for i in range(N):
  if(A[i]<B[m]):
    print(a + 1)
  else:
    print(a)
