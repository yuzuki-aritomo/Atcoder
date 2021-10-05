import io
import sys
_INPUT = """\
6
30 35
35 15
15 5
5 10
10 20
20 25
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
p = []
inf = float('inf')
M = [[inf]*(N+1)]*(N+1)
for i in range(N):
    a, b = map(int, input().split())
    if(i==0):
        p.append(a)
    p.append(b)

for i in range(1, N):
    M[i][i] = 0

for l in range(2,N+1):
    for i in range(1, N-l+2):
        j = i + l - 1
        M[i][j] = inf
        for k in range(i,j):
            a = M[i][j]
            # print("M[i][k]:", M[i][k])
            # print("M[k+1][j]:", M[k+1][j])
            # print("p[k-1]*p[k]*p[k+1]:", p[k-1]*p[k]*p[k+1])
            b = M[i][k] + M[k+1][j] + p[k-1]*p[k]*p[k+1]
            print("a:", a)
            print("b:", b)
            M[i][j] = min(a, b)

print(M[1][6])
print(M)