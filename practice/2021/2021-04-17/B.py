import io
import sys
_INPUT = """\
4 4
1 2 3 4 8 10 20 40 55
1 2 3 4 65
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

N, M = map(int, input().split())
A = list(map(int,input().split()))
A.extend(list(map(int,input().split())))

Cnt = Counter(A)
Ans = []
for item in Cnt:
    if(Cnt[item] == 1):
        Ans.append(item)
Ans.sort()
print(" ".join(map(str, Ans)))