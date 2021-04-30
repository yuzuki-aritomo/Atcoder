import io
import sys
_INPUT = """\
7
1 1 1 1 1 1 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))
A = sorted(A, reverse=True)

Ans = 0
for i in range(1, N):
    Ans  += A[i//2]
print(Ans)