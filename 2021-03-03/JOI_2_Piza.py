import io
import sys
_INPUT = """\
20
4
4
12
8
16
7
7
11
8
"""
sys.stdin = io.StringIO(_INPUT)

import bisect

d = int(input())#環状線の全長
n = int(input())#店舗の数
m = int(input())#注文の個数

Store = [0,d]
for i in range(n-1):
    Store.append(int(input()))
Store.sort()

ans = 0
for i in range(m):
    goal = int(input())
    tmp = bisect.bisect(Store, goal)
    ans += min(abs(Store[tmp]-goal), abs(Store[tmp-1]-goal))
print(ans)
