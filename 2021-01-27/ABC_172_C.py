import io
import sys

_INPUT = """\
5 4 1
1000000000 1000000000 1000000000 1000000000 1000000000
1000000000 1000000000 1000000000 1000000000
"""
sys.stdin = io.StringIO(_INPUT)

N, M, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a, b = [0], [0]
n, m = 0, 0
for i in range(N):
    n += A[i]
    a.append(n)
for i in range(M):
    m += B[i]
    b.append(m)

ans = 0
j = M
for i in range(N+1):
    if(a[i]>K):
        break
    while(b[j] > K -a[i]):
        j -= 1
    ans = max(ans, j+i)
print(ans)
