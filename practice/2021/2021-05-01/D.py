import io
import sys
_INPUT = """\
10
6 7 5 18 2
3 8 1 6 3
7 2 8 7 7
6 3 3 4 7
12 8 9 15 9
9 8 6 1 10
12 9 7 8 2
10 3 17 4 10
3 1 3 19 3
3 14 7 13 1
"""
sys.stdin = io.StringIO(_INPUT)

def calc(A, B, C):
    tmp = [0 for i in range(5)]
    for i in range(5):
        tmp[i] = max(A[i], B[i], C[i])
    return min(tmp)

N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
Ans = calc(A, B ,C)

for i in range(N-3):
    D = list(map(int,input().split()))
    tmpC =  calc(A, B, D)
    tmpB =  calc(A, B, C)
    tmpA = calc(D, B, C)
    print(Ans)
    if(tmpC >= tmpB and tmpC>=tmpA and Ans<tmpC):
        Ans = tmpC
        C = D
    elif(tmpB >= tmpA and tmpB >=tmpC and Ans<tmpB):
        Ans = tmpB
        B = D
    elif(tmpA >= tmpB and tmpA >=tmpC and Ans<tmpA):
        Ans = tmpA
        A = D

print(Ans)
    