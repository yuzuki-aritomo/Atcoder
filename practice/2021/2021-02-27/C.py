import io
import sys
_INPUT = """\
100000
"""
sys.stdin = io.StringIO(_INPUT)

import math
N = int(input())

n_root = math.floor(math.sqrt(N))
k = 2
ans = 0
ANS = set()
for i in range(n_root,1,-1):
    for k in range(2,N):
        if(i**k>N):
            break
        ANS.add(i**k)
print(N-len(ANS))
