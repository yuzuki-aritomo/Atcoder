import io
import sys
_INPUT = """\
5
1 2 3 4 5
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

def change(w):
    if(len(w)<3):
        w = "00"+ w
    return w


N = int(input())
A = list(map(change ,input().split()))


GL = Counter()
KL = Counter()

for i in range(N):
    if( int(A[i][-3])%2==0 ):
        tmp = (A[i][-2:])
        GL[tmp] += 1
    else:
        tmp = (A[i][-2:])
        KL[tmp] += 1

Ans = 0
for item in GL:
    tmp = GL[item]
    Ans += tmp*(tmp-1)//2

for item in KL:
    tmp = KL[item]
    Ans += tmp*(tmp-1)//2
print(Ans)
