import io
import sys

_INPUT = """\
10
-31 -35
8 -36
22 64
5 73
-14 8
18 -58
-41 -85
1 -88
-21 -85
-11 82
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = []
ans = 0
for i in range(n):
    A.append(input())

for i in range(n):
    x_i, y_i = map(int,A[i].split())
    for k in range(i+1,n):
        x_k, y_k = map(int, A[k].split())
        lad = (y_k - y_i) / (x_i - x_k)
        if(lad>= -1 and lad<=1):
            ans += 1
print(ans)