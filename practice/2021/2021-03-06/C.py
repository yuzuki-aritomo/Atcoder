import io
import sys
_INPUT = """\
5
-5 8 9 -4 -3
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

sumA = [sum(A)]
for i in range(N):
    sumA.append(sumA[i] - A[i])

ans = 0

for i in range(N):
    ans += (N-1)*A[i]*A[i]

for i in range(N):
    ans -= 2*A[i]*sumA[i+1]

print(ans)