import io
import sys
_INPUT = """\
10 998244353
10 9 8 7 5 6 3 4 2 1
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9+7
P = 0
for i in range(N):
  for j in range(i, N):
    if(A[i] > A[j]):
      P += 1
Q = 0
for i in range(N):
  for j in range(N):
    if(A[i] > A[j]):
      Q += 1

print((P*K + Q*K*(K-1)//2)%mod)
