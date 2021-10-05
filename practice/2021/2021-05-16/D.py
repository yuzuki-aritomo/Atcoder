import io
import sys
_INPUT = """\
6 15
6 5
5 6
6 4
6 6
3 5
7 2
"""
sys.stdin = io.StringIO(_INPUT)

N, W = map(int, input().split())
w = []
v = []
for i in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

dp = [[0 for _ in range(W+1)] for _ in range(N)]

for j in range(W+1):
    if(j-w[0]>=0):
        dp[0][j] = v[0]

for i in range(N-1):
    for j in range(W+1):
        if(j-w[i+1]>=0):
            dp[i+1][j] = max(dp[i][j], dp[i][j - w[i+1]]+ v[i+1])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[-1][-1])


