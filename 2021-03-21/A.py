import io
import sys
_INPUT = """\
7 5
10101
00001
00110
11110
00100
11111
10000
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(input())

ans = 0
for i in range(N):
    for k in range(i+1, N):
        tmp = 0
        for m in range(M):
            if(A[i][m]!=A[k][m]):
                tmp += 1
        if(tmp%2 == 1):
            ans += 1

print(ans)