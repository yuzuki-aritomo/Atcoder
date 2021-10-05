import io
import sys
_INPUT = """\
3 2
"""
sys.stdin = io.StringIO(_INPUT)


N, D = map(int, input().split())

A = [1]
mod = 998244353
for i in range(N):
  A.append(A[i]*2%mod)

ans = 0
ans += (A[max(N-D, 0)]-1) * (A[D-1]*(D+1))

print((A[max(N-D, 0)]-1))


print(ans)