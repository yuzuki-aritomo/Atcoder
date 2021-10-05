import io
import sys

_INPUT = """\
2
1 4 2 5
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())

A = list(map(int,input().split()))

a = 2**n
b = a//2

B = A[:b]
C = A[b:]

max_b = max(B)
max_c = max(C)

if(max_b<max_c):
    print(A.index(max_b) + 1)
else:
    print(A.index(max_c) + 1)


