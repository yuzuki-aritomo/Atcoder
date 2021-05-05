import io
import sys
_INPUT = """\
10 4
17 13 13 12 15 20 10 13 17 11
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = list(map(int,input().split()))

S = sum(A[0:K])
tmp = S
ind = 0
for i in range(K, N):
    S -= A[i-K]
    S += A[i]
    if(S > tmp):
        ind = i - K + 1
        tmp = S

sumA = [0]
for i in range(1, 2100):
    sumA.append(sumA[-1] + i)
for i in range(1, 2100):
    sumA[i] /= i
Ans = 0
for i in range(ind, ind+K):
    Ans += sumA[A[i]]
print(Ans)


