import io
import sys
_INPUT = """\
7
218 786 704 233 645 728 389
"""
sys.stdin = io.StringIO(_INPUT)

import bisect
N = int(input())
L = list(map(int,input().split()))
L.sort()

Ans = 0
for i in range(N):
    for j in range(i+1, N):
        Mx = L[i] + L[j]
        Mn = L[j] - L[i]
        idMn = bisect.bisect_right(L[j+1:], Mn)
        idMx = bisect.bisect_left(L[j+1:], Mx)
        tmp = idMx - idMn
        Ans += tmp

print(Ans)