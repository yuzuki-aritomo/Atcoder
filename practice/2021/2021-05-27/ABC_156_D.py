import io
import sys
_INPUT = """\
1000000000 141421 173205
"""
sys.stdin = io.StringIO(_INPUT)

mod = 10**9+7
N, a, b = map(int, input().split())

def choose(n, r):
    x = 1
    y = 1
    for i in range(n-r+1, n+1):
        x *= i
        x %= 10**9+7
    for i in range(1, r+1):
        y *= i
        y %= 10**9+7
    return x * pow(y, mod-2, mod) % mod

Ans = pow(2, N, mod) -  1 - choose(N, a) - choose(N, b)

print(Ans % mod)