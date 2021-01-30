import io
import sys
_INPUT = """\
5
-2 1 3 -1 -1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))
ans = 0
all_cum = 0
maxv = 0
a_cum = 0
for i in range(N):
    a_cum += A[i]
    maxv = max(maxv, a_cum)
    ans = max(ans, all_cum+maxv)
    all_cum += a_cum
print(ans)

