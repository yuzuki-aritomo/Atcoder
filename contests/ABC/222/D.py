import io
import sys
_INPUT = """\
10
1 2 3 4 5 6 7 8 9 10
1 4 9 16 25 36 49 64 81 100
"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
mod = 998244353

dp = [0 for i in range(3004)]

for i in range(A[0], B[0]+1):
  dp[i] = dp[i-1] + 1

maxVal = dp[B[0]]
# print(dp)

for i in range(1, len(A)):
  dp[A[i]-1] = 0
  for j in range(A[i], B[i]+1):
    if(j>B[i-1]):
      dp[j] = (maxVal + dp[j-1])%mod
    else:
      dp[j] = (dp[j] + dp[j-1])%mod
    # print(j, dp, maxVal)
  maxVal = dp[B[i]]
print(maxVal)
