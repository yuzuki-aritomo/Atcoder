import io
import sys
_INPUT = """\
5
0 1 2 3 4
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))
mod = 998244353

dp = [0 for _ in range(10)]
dp[(A[0]+A[1])%10] += 1
dp[(A[0]*A[1])%10] += 1

for i in range(2, N):
  tmp = [0 for _ in range(10)]
  for j in range(10):
    if(dp[j] == 0):
      continue
    tmp[(A[i]+j)%10] += dp[j]%mod
    tmp[(A[i]*j)%10] += dp[j]%mod
  dp = tmp.copy()

for item in dp:
  print(item%mod)
