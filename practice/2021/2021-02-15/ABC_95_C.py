import io
import sys
_INPUT = """\
1500 2000 500 90000 100000
"""
sys.stdin = io.StringIO(_INPUT)

A, B, C, X, Y = map(int, input().split())

if(A+B <= C*2):
    ans = A*X + B*Y
    print(ans)
    exit()

ans = 2*C*min(X, Y)
if(max(X, Y)==X):
    tm = A
else:
    tm = B
ans += abs(X-Y)*min(2*C, tm)

print(ans)