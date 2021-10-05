import io
import sys
_INPUT = """\
6 9
3 2
2 1
6 3
1 2
3 1
85 5
"""
sys.stdin = io.StringIO(_INPUT)
#値の受け取り
N, W = map(int, input().split())

#dpの初期化
dp = [[0 for i in range(W+1)] for k in range(N+1)]

# 初期値の受け取り
value = []
weight = []
for i in range(N):
    v, w = map(int, input().split())
    value.append(v)
    weight.append(w)
#ナップサックDP
for i in range(N):
    for k in range(W+1):
        if(k >= weight[i]):
            dp[i+1][k] = max( dp[i][k-weight[i]]+value[i], dp[i][k])
        else:
            dp[i+1][k] = dp[i][k]
print(max(dp[N]))