import io
import sys
_INPUT = """\
6
1 2 2 4
2 1 5
3 2 5 6
4 0
5 1 4
6 1 6
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    B = list(map(int,input().split()))
    for k in range(B[1]):
        A[B[0]-1][B[k+2]-1] = 1

for item in A:
    print(" ".join(map(str, item)))

