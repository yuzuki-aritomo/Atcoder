
import io
import sys
_INPUT = """\
5 5
3 5 6 5 4
"""
sys.stdin = io.StringIO(_INPUT)

N, X = map(int, input().split())

A = list(map(int,input().split()))
C = []
for i in range(N):
    if(A[i] == X):
        continue
    C.append(A[i])
print(" ".join([str(n) for n in C]))