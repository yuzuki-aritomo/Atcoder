import io
import sys
_INPUT = """\
3 14 15926535
"""
sys.stdin = io.StringIO(_INPUT)



N, K, M = map(int, input().split())
mod = 998244353

t = pow(K, N, mod)
ans = pow(M, t, mod)
print(ans)