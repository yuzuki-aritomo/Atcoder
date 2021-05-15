import io
import sys
_INPUT = """\
2 4
+++-
-+-+
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
M = []
for i in range(H):
    M.append(list(input()))

for i in range(H):
    for j in range(W):
        if((i+j)%2==0 ):
            if(M[i][j]=="-"):
                M[i][j] = 1
            else:
                M[i][j] = -1
        elif(M[i][j]=="+"):
            M[i][j] = 1
        else:
            M[i][j] = -1
dp = [[0 for i in range(W)] for i in range(H)]

for i in range(H):
    for j in range(W):
        if(i-1<0 and j-1<0):
            continue
        elif(i-1<0):
            dp[i][j] = dp[i][j - 1] + M[i][j]
        elif(j-1<0):
            dp[i][j] = dp[i-1][j] + M[i][j]
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i-1][j]) + M[i][j]


if(dp[-1][-1]>0):
    print("Takahashi")
elif(dp[-1][-1] == 0):
    print("Draw")
else:
    print("Aoki")