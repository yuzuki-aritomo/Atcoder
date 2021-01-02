import io
import sys

_INPUT = """\
100 999
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(str, input().split())

a = 0
b = 0
for i in range(len(A)):
    a += int(A[i])

for i in range(len(B)):
    b += int(B[i])

if(a<b):
    print(b)
else:
    print(a)