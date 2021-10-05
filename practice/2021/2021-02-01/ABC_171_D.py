import io
import sys
_INPUT = """\
2
1 2
3
1 100
2 100
100 1000
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

N = int(input())
A = list(map(int,input().split()))
cnt = Counter(A)
M = int(input())

ans = 0
for item in cnt:
    ans += item*cnt[item]

for i in range(M):
    a, b = map(int, input().split())
    if not b in cnt:
        cnt[b] = 0
    tmp = cnt.pop(a, 0)
    cnt[b] += tmp
    ans += (b-a)*tmp
    print(ans)
