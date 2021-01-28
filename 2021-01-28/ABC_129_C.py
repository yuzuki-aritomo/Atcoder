import io
import sys
_INPUT = """\
1 0
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = [-1]*(N+3)
for i in range(M):
    A[int(input())] = 0

if(A[1] != 0 and A[2] != 0):
    A[1] = 1
    A[2] = 2
elif(A[1]==0 and A[2] == 0):
    A[1] = 0
    A[2] = 0
elif(A[2]!=0):
    A[2] = 1
else:
    A[1] =1

for i in range(3, N+1):
    if(A[i] == 0):
        continue
    else:
        A[i] = (A[i-1] + A[i-2])%1000000007

print(A[N]%1000000007)