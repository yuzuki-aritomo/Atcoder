import io
import sys
_INPUT = """\
4
QCFium 2846
chokudai 2992
kyoprofriends 2432
penguinman 2390
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = []
for i in range(N):
    A.append(list(input().split()))

for i in range(N):
    A[i][1] = int(A[i][1])

A.sort(key=lambda x:x[1])
print(A[-2][0])

