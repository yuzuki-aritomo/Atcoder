import io
import sys
_INPUT = """\
3 3
---
+-+
+--
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
M = []
for i in range(H):
    M.append(list(input()))

for i in range(H):
    for j in range(W):
        if(M[i][j]=="+"):
            M[i][j] = 1
        else:
            M[i][j] = -1

dp = [[0 for i in range(W)] for i in range(H)]

for i in range(H-1, 0, -1):
    for j in range(W-1, 0, -1):
        if(i+1>=H and j+1>=W):
            continue
        elif(i+1>=H):
            dp[i][j] = dp[i][j + 1] + M[i][j]
        elif(j+1>=W):
            dp[i][j] = dp[i+1][j] + M[i][j]
        else:
            if (i+j)%2==1:
                dp[i][j] = max(dp[i][j + 1], dp[i+1][j]) + M[i][j]
            else:
                dp[i][j] = min(dp[i][j + 1], dp[i+1][j]) + M[i][j]

for item in dp:
    print(item)

if(dp[-1][-1]>0):
    print("Takahashi")
elif(dp[-1][-1] == 0):
    print("Draw")
else:
    print("Aoki")