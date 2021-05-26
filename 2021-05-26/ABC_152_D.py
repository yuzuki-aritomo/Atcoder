import io
import sys
_INPUT = """\
2020
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
M = [[0 for _ in range(10)] for _ in range(10)]

for i in range(1, N+1):
    w = str(i)
    M[int(w[0])][int(w[-1])] += 1

Ans = 0
for i in range(1,10):
    for j in range(1,10):
        Ans += M[i][j]*M[j][i]

print(Ans)


