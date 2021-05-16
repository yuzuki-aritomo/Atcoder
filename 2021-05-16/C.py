import io
import sys
_INPUT = """\
7
6 7 8
8 8 3
2 5 2
7 8 6
4 6 8
2 3 4
7 5 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
M = []
for i in range(N):
    M.append(list(map(int,input().split())))
dp = [[0 for _ in range(3)] for _ in range(N)]

#dp[i][j] i日目にjを遊んだ時の幸福度0,1,2 =>海、山、家
for i in range(3):
    dp[0][i] = M[0][i]

for i in range(1, N):
    dp[i][0] = max(dp[i-1][1]+M[i][0], dp[i-1][2]+M[i][0])
    dp[i][1] = max(dp[i-1][0]+M[i][1], dp[i-1][2]+M[i][1])
    dp[i][2] = max(dp[i-1][0]+M[i][2], dp[i-1][1]+M[i][2])

print(max(dp[-1]))
