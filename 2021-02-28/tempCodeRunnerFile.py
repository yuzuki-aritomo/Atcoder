import copy
import numpy as np
import math

N = int(input())
Ans = []
C = []
for i in range(N):
    C.append(list(map(int,input().split())))

def CountScore(B):
    global Ans
    tmp = 0
    ave = np.median(B, axis=0)
    ave = [int(n) for n in ave]
    for i in range(N):
        tmp += abs(ave[0]-B[i][0])
        tmp += abs(B[i][0]-B[i][1])
        tmp += abs(ave[1]-B[i][1])
    Ans.append(tmp)

for bit in range(2**N):
    A = copy.deepcopy(C)
    for i in range(N):
        if((bit>>i) & 1):
            A[i][0] , A[i][1] = A[i][1] , A[i][0]
    CountScore(A)

print(int(min(Ans)))