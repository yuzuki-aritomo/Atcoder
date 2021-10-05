import io
import sys
_INPUT = """\
9
314 159 265 358 979 323 846 264 338
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))

D = [0]*N

D[0] = 0
D[1] = abs(A[1] - A[0])
for i in range(2, N):
    a = D[i-1] + abs(A[i-1] - A[i])
    b = D[i-2] + abs(A[i-2] - A[i])
    D[i] = min(a, b)

print(D[N-1])




def solve(i):
    if(i==0):
        D[i] = 0
        return 0
    

