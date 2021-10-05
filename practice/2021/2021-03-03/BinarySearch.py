import io
import sys
_INPUT = """\
5
1 1 2 2 3
2
1 2
"""
sys.stdin = io.StringIO(_INPUT)

import bisect

n = int(input())
A = list(map(int,input().split()))
q = int(input())
B = list(map(int,input().split()))

ans = 0
for item in B:
    tmp = bisect.bisect_left(A, item)
    if(tmp==n):
        continue
    elif(A[tmp]==item):
        ans += 1
print(ans)
