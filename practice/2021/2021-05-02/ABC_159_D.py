import io
import sys
_INPUT = """\
8
1 2 1 4 2 1 4 1
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

N = int(input())
A = list(map(int,input().split()))
Cnt = Counter(A)
Ans = [0 for _ in range(2*10**5+1)]

def calc(n):
    return n*(n-1)//2

ans = 0
for item in Cnt:
    Ans[item] = calc(Cnt[item])
    ans += calc(Cnt[item])

for item in A:
    tmp = ans
    tmp -= Ans[item]
    tmp += calc(Cnt[item]-1)
    print(tmp)
