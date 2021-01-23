import io
import sys

_INPUT = """\
1
1 2
4
1
3 3
2
4 2
5
0 1
1 1
2 1
3 1
4 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = []
for i in range(N):
    A.append(list(map(int,input())))
M = int(input())
B = []
for i in range(M):
    B.append(list(map(int,input())))
Q = int(input())
C = []
for i in range(M):
    C.append(list(map(int,input())))

for i in range(M):
    if(B[i][0]==1):
        # 90
    elif(B[i][0]==2):
        #-90
    elif(B[i][0]==3):
        A[i][0] = B[i][1] - (A[i][0] - B[i][1])
    elif(B[i][0]==4):

