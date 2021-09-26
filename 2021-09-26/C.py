import io
import sys
_INPUT = """\
4
12 34 56 78
1000
"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())
A = list(map(int,input().split()))
X = int(input())

S = sum(A)
tmp = X//S
T = X%S
t = 0
for i in range(N):
  t += A[i]
  if(t>T):
    ans = tmp*N + i+1
    print(ans)
    break
