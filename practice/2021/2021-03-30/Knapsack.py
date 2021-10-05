import io
import sys
_INPUT = """\
2 20
5 9
4 10
"""
sys.stdin = io.StringIO(_INPUT)

N, W = map(int, input().split())
weight = []
value = []
for i in range(N):
    a, b = map(int, input().split())
    value.append(a)
    weight.append(b)

dp = [[0 for i in range(W+1)] for _ in range(N+1)]
for n in range(N):
    for w in range(W+1):
        if(weight[n]<=w):
            #n+1番目の品物を追加するかどうか
            dp[n+1][w] = max(dp[n][w], dp[n][w-weight[n]]+value[n])
        else:
            dp[n+1][w] = dp[n][w]
print(max(max(dp)))
