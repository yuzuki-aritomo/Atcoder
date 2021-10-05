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
import itertools
N, K = map(int, input().split())

A = []
for i in range(N):
    A.append(list(map(int,input().split())))

S = dict()
n = 0
for i in range(N):
    for j in range(N):
        if(A[i][j] in S):
            S[A[i][j]].append([i,j])
        else:
            S[A[i][j]] = list([i,j])
            n += 1

M = list(itertools.chain.from_iterable(A))
M.sort()

Ans = [[0 for _ in range(N-K+1)] for i in range(N-K+1)]

for i in range(n):
    for item in S[M[i]]:
        
        Ans[item[0]-1][item[1]-1] += 1
        Ans[item[0]-1][item[1]] += 1
        Ans[item[0]-1][item[1]] += 1
        Ans[item[0]+1][item[1]+1] += 1
        if(Ans[])
