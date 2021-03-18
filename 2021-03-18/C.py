import io
import sys
_INPUT = """\
100 0
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

X, N = map(int, input().split())
A = []
if(N!=0):
    A = list(map(int,input().split()))
A.sort()

B = []
Cnt = Counter(B)
for item in A:
    tmp = abs(item-X)
    Cnt[tmp] += 1
    B.append([tmp, item])
B.sort()
if(Cnt[0]== 0):
    print(X)
    exit()
for i in range(1, 100):
    if(Cnt[i] < 2):
        # print(i)
        if (X-i) in A:
            print(X+i)
        else:
            print(X-i)
        break
