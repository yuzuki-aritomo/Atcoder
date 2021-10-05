import io
import sys
_INPUT = """\
8 2
31000000 41000000
59000000 26000000
53000000 58000000
97000000 93000000
23000000 84000000
62000000 64000000
33000000 83000000
27000000 95000000
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int,input().split())))

Ans = 0
for t1 in range(M):
    for t2 in range(t1+1, M):
        ans = 0
        for i in range(N):
            ans += max(A[i][t1], A[i][t2])
        Ans = max(Ans, ans)
print(Ans)
