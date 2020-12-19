import io
import sys

_INPUT = """\
3 2
4 4
4 4
4 4
"""
sys.stdin = io.StringIO(_INPUT)

H,W = map(int, input().split())

minu = 100
su = 0
A = []

for i in range(H):
    A.append(list(map(int, input().split())))
    for k in range(W):
        if(A[i][k]<minu):
            minu = A[i][k]

for i in range(H):
    for k in range(W):
        su += A[i][k] - minu

print(su)

