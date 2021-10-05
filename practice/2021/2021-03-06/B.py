import io
import sys
_INPUT = """\
3
11 7
3 2
6 7
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

min_A = min(A)
min_B = min(B)

minA = A.index(min_A)
minB = B.index(min_B)

if(minA != minB):
    print(max(min_A, min_B))
else:
    ans = min_A + min_B
    A.pop(minA)
    B.pop(minB)
    tmpA = min(A)
    tmpB = min(B)
    print(min(ans, max(tmpA, min_B), max(tmpB, min_A)))
