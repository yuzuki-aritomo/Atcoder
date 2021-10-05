import io
import sys
_INPUT = """\
6
3 14 159 2 6 53
58 9 79 323 84 6
2643 383 2 79 50 288
"""
sys.stdin = io.StringIO(_INPUT)

import bisect

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort()
B.sort()
C.sort()

ans = 0
for itemB in B:
    index_A = bisect.bisect_left(A, itemB)
    index_C = bisect.bisect_right(C, itemB)
    ans += index_A*(N - index_C)

print(ans)