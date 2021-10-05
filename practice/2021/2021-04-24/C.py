from A import C
import io
import sys
_INPUT = """\
2
FLIP
6
1 1 3
2 0 0
1 1 2
1 2 3
2 0 0
1 1 4
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = list(input())
Q = int(input())

Com = []
Flag = 0
for i in range(Q):
    A = list(map(int,input().split()))
    if(A[0]==1):
        A.append(Flag%2)
        Com.append(A)
    else:
        Flag += 1

for com in Com:
    if(com[3] == 0):
        S[com[1]-1], S[com[2]-1] = S[com[2]-1], S[com[1]-1]
    else:
        com[1] -= 1
        com[2] -= 1
        if(com[1]>=N):
            com[1] -= N
        else:
            com[1] += N
        if(com[2]>=N):
            com[2] -= N
        else:
            com[2] += N
        S[com[1]], S[com[2]] = S[com[2]], S[com[1]]

if(Flag %2 == 0):
    print("".join(S))
else:
    S[:N],S[N:] = S[N:],S[:N]
    print("".join(S))
