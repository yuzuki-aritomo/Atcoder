import io
import sys

_INPUT = """\
3
abcbdab
bdcaba
abc
abc
abc
bc
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

for k in range(N):
    x = input()
    y = input()
    n = len(x)
    m = len(y)
    C = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                C[i][j] = 0
            elif(y[i-1]==x[j-1]):
                C[i][j] = C[i-1][j-1] + 1
            elif(y[i-1]!=x[j-1]):
                C[i][j] = max(C[i][j-1],C[i-1][j])
    print(C[m][n])
    # print(C)