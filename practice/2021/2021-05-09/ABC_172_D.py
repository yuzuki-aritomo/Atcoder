import io
import sys
_INPUT = """\
10000000
"""
sys.stdin = io.StringIO(_INPUT)

import time
s = time.time()

N = int(input())
Ans = 0
for i in range(1, N+1):
    n = N//i
    Ans += i*(n+1)*n//2
print(Ans)

print(time.time() - s)