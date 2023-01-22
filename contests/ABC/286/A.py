import io
import sys
_INPUT = """\
10 2 4 7 9
22 75 26 45 72 81 47 29 97 2
"""
sys.stdin = io.StringIO(_INPUT)


n, p, q, r, s = map(int,input().split())
A = list(map(int,input().split()))

a = A[p-1:q]
b = A[r-1:s]

A[r-1:s] = a
A[p-1:q] = b
print(*A)

