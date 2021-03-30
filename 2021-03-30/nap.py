import io
import sys
_INPUT = """\
25 5000
56 20
53 28
54 30
77 48
20 4
14 10
19 25
98 31
1 9
51 22
17 52
24 95
71 53
25 78
16 42
97 88
32 17
4 43
95 49
7 36
2 67
45 63
40 98
96 51
7 67
"""
sys.stdin = io.StringIO(_INPUT)

N, W = map(int, input().split())
dp = [0] * (W+1)
for i in range(N):
    v, w = map(int, input().split())
    for j in range(w, W+1):
        dp[j] = max(dp[j-w] + v, dp[j])
print(dp[W])