import io
import sys
_INPUT = """\
5
OR
OR
OR
OR
OR
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
dp = [1, 1]

for i in range(N):
    S = input()
    p = dp.copy()
    if(S == "AND"):
        dp[0] = p[0]*2 + p[1]
    elif(S=="OR"):
        dp[1] = p[0] + p[1]*2

print(dp[1])
