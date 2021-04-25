import io
import sys
_INPUT = """\
6
200 4 4 9 4 9
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))

Ans = -float("inf")
for L in range(N):
    m = float("inf")
    for R in range(L,N):
        m = min(m, A[R])
        Ans = max(Ans, (R-L+1)*m)

print(Ans)


