import io
import sys
_INPUT = """\
6
30 10 60 10 60 50
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))
dp = [0 for _ in range(N)]
for i in range(N):
    if(i == 0):
        continue
    if(i == 1):
        dp[i] = dp[i -1] + abs(A[i-1] - A[i])
        continue
    a = dp[i -1] + abs(A[i-1] - A[i])
    b = dp[i -2] + abs(A[i-2] - A[i])
    dp[i] = min(a, b)

print(dp[-1])