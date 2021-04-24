import io
import sys
_INPUT = """\
3
3 2 5
6 9 8
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ansA = -float("inf")
ansB = float("inf")
for i in range(N):
    a = A[i]
    b = B[i]
    ansA = max(ansA, a)
    ansB  = min(ansB, b)

if(ansA>ansB):
    print(0)
else:
    print(ansB-ansA+1)
