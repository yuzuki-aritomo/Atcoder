import io
import sys
_INPUT = """\
1 1
-
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
N = [[0 for i in range(W)] for i in range(H)]
for i in range(H):
    for j in range(W):
        if((i+j)%2==0 ):
            if(M[i][j]==-1):
                N[i][j] = 1
            else:
                N[i][j] = -1
        elif(M[i][j]==1):
            N[i][j] = 1
        else:
            N[i][j] = -1

dp = [[0 for i in range(W)] for i in range(H)]
Ans = [[0 for i in range(W)] for i in range(H)]
for i in range(H):
    for j in range(W):
        if(i-1<0 and j-1<0):
            continue
        elif(i-1<0):
            dp[i][j] = dp[i][j - 1] + M[i][j]
            Ans[i][j] = Ans[i][j - 1] + N[i][j]
        elif(j-1<0):
            dp[i][j] = dp[i-1][j] + M[i][j]
            Ans[i][j] = Ans[i-1][j] + N[i][j]
        else:
            if(dp[i][j-1]>dp[i-1][j]):
                dp[i][j] = dp[i][j - 1] + M[i][j]
                Ans[i][j] = Ans[i][j-1]+ N[i][j]
            else:
                dp[i][j] = dp[i-1][j] + M[i][j]
                Ans[i][j] = Ans[i-1][j]+ N[i][j]


if(Ans[-1][-1]>0):
    print("Takahashi")
elif(Ans[-1][-1] == 0):
    print("Draw")
else:
    print("Aoki")