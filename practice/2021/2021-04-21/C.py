import io
import sys
_INPUT = """\
1000000
"""
sys.stdin = io.StringIO(_INPUT)

import math
N = int(input())
ans = 0
for i in range(1, N):
    tmp = (N-1)//i
    ans += tmp
print(ans)