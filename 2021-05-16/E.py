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
V =0
for i in range(N):
    a, b = map(int, input().split())
    V += b
    w.append(a)
    v.append(b)

dp = [[float("inf") for _ in range(V+1)] for _ in range(N)]

for j in range(V+1):
    if(v[0]-j>=0):
        dp[0][j] = w[0]

for i in range(N-1):
    for j in range(V+1):
        if(v[i+1]-j>=0):
            dp[i+1][j] = min(dp[i][j], w[i+1])
        elif(j-v[i+1]>=0):
            dp[i+1][j] = min(dp[i][j], dp[i][j - v[i+1]]+ w[i+1])
        else:
            dp[i+1][j] = dp[i][j]

for i in range(1, V+1):
    if(dp[-1][-i]<=W):
        print(V+1-i)
        exit()
