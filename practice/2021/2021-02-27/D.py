import io
import sys
_INPUT = """\
2
1144#
2233#
"""
sys.stdin = io.StringIO(_INPUT)

import collections

N = int(input())

S = input()
T = input()

s,t = [],[]
for i in range(4):
    s.append(S[i])
    t.append(T[i])
ST = s + t
Count = collections.Counter(ST)
S_Count = collections.Counter(s)
T_Count = collections.Counter(t)

A = [0 for i in range(10)]
for i in range(1,10):
    A[i] = 0
    if(Count[i]+1>N):
        A[i] = 1
        if(Count[i]+2>N):
            A[i] = 2



print(Count[8])


for i in range(1,10):
    for k in range(1,10):
        S_score = 0
        for j in range(1,10):
            S_score += j*(10**S_Count[j])
        print(S_score)