import io
import sys
_INPUT = """\
10
866111664 178537096 844917655 218662351 383133839 231371336 353498483 865935868 472381277 579910117
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))
mod = 1000000000 + 7

dp = [[0, 0] for i in range(N)]
dp[0][0] = A[0]
dp[0][1] = A[0]

for i in range(1, N):
  if(i == 1):
    dp[i][0] = A[0] - A[1]
    dp[i][1] = A[0] + A[1]
    continue
  dp[i][0] = dp[i-1][1] - A[i]
  dp[i][1] = dp[i-1][0] + A[i] + dp[i-1][1] + A[i]
  
  dp[i][0] %= mod
  dp[i][1] %= mod

print(sum(dp[-1])%mod)
