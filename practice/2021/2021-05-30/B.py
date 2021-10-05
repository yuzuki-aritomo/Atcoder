import io
import sys
_INPUT = """\
3 3
"""
sys.stdin = io.StringIO(_INPUT)


N, K = map(int, input().split())
Ans = 0
for i in range(1, N+1):
    for k in range(1, K+1):
        Ans += i*100
        Ans += k
print(Ans)
