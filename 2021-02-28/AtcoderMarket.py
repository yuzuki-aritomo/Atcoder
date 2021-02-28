import io
import sys
_INPUT = """\
11
15004200 341668840
277786703 825590503
85505967 410375631
797368845 930277710
90107929 763195990
104844373 888031128
338351523 715240891
458782074 493862093
189601059 534714600
299073643 971113974
98291394 443377420
"""
sys.stdin = io.StringIO(_INPUT)

import copy
import math

N = int(input())
Ans = []
C = []
for i in range(N):
    C.append(list(map(int,input().split())))

def CountScore(B):
    global Ans
    tmp = 0
    Start = []
    Goal = []
    for i in range(N):
        Start.append(B[i][0])
        Goal.append(B[i][1])
    Start.sort()
    Goal.sort()
    s = Start[N//2]
    g = Goal[N//2]
    for i in range(N):
        tmp += abs(s-B[i][0])
        tmp += abs(B[i][0]-B[i][1])
        tmp += abs(g-B[i][1])
    Ans.append(tmp)

for bit in range(2**N):
    A = copy.deepcopy(C)
    for i in range(N):
        if((bit>>i) & 1):
            A[i][0] , A[i][1] = A[i][1] , A[i][0]
    CountScore(A)

print(int(min(Ans)))