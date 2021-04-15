import io
import sys
_INPUT = """\
3 2
9
5
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
for i in range(M):
    mikan = int(input())
    A = mikan//N
    if(A == 0):
        print(N)
    elif(mikan - A*N < (A+1)*N - mikan):
        print(A*N)
    else:
        print((A+1)*N)