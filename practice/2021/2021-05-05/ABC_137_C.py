import io
import sys
_INPUT = """\
5
abaaaaaaaa
oneplustwo
aaaaaaaaba
twoplusone
aaaabaaaaa
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

N = int(input())
C = Counter()

for i in range(N):
    Cnt = Counter(input())
    A = list(Cnt)
    A.sort()
    w = ""
    for item in A:
        w += item + str(Cnt[item])
    C[w] += 1

Ans = 0
for item in C:
    if(C[item]>=2):
        Ans += C[item]*(C[item]-1)//2
print(Ans)

