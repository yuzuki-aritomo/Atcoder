import io
import sys
_INPUT = """\
2 3
2 55
2 77
2 99
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

def makeWord(w):
    w = str(w)
    while(len(w)<6):
        w = "0" + w
    return w

N, M = map(int, input().split())
A = []
for i in range(M):
    A.append(list(map(int,input().split())))
Asort = sorted(A, key=lambda x: x[1])
Cnt = Counter()

Ans = dict()
for item in Asort:
    Cnt[item[0]] += 1
    firstW = makeWord(item[0])
    latterW = makeWord(Cnt[item[0]])
    Ans[item[1]] = firstW + latterW

for i in range(M):
    print(Ans[A[i][1]])
