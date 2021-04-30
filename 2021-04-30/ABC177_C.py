import io
import sys
_INPUT = """\
4
141421356 17320508 22360679 244949
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))
mod = 10**9 + 7
S = [sum(A)]
for i in range(N):
    S.append(S[-1] - A[i])

Ans = 0
for i in range(N):
    Ans += A[i]*S[i+1]
    Ans = Ans % mod

print(Ans)