import io
import sys
_INPUT = """\
3 3
1 2 3
4 5 6
7 8 9
"""
sys.stdin = io.StringIO(_INPUT)

import math
N, K = map(int, input().split())

A = []
for i in range(N):
    A.append(list(map(int,input().split())))

def calc(L):
    L.sort()
    return L[math.ceil(K**2/2)-1]

from collections import deque

Ans = float("inf")

for k in range(N-K+1):
    List_R = deque()
    for n in range(K):
        for m in range(K):
            List_R.append(A[n][m+k])
    
    for i in range(N-K+1):
        Ans = min(calc(list(List_R)), Ans)
        # print("List_R:", List_R)
        # print("Ans:", Ans)
        if(i == N-K):
            break
        for j in range(K):
            List_R.popleft()
            List_R.append(A[i+K][j+k])

print(Ans)
