import io
import sys
_INPUT = """\
10 4
40 10 20 70 80 10 20 70 80 60

"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = list(map(int,input().split()))
dp = [0 for _ in range(N)]
for i in range(1, N):
    tmp = float("inf")
    for k in range(1, K+1):
        if(i-k < 0):
            break
        a = dp[i-k] + abs(A[i-k] - A[i])
        tmp = min(tmp, a)
    dp[i] = tmp

print(dp[-1])