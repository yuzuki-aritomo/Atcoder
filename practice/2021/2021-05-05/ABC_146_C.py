import io
import sys
_INPUT = """\
1234 56789 314159265
"""
sys.stdin = io.StringIO(_INPUT)

import math
A, B, X = map(int, input().split())

n = math.floor(X/A)
n = min(n, 10**9)
if(n>1001):
    for i in range(n, -1, -1000):
        if(A*i + B*len(str(i)) <= X):
            a = min(i+1000, n)
            for j in range(a, -1, -1):
                if(A*j + B*len(str(j)) <= X):
                    print(j)
                    exit()
else:
    for j in range(n, -1, -1):
        if(A*j + B*len(str(j)) <= X):
            print(j)
            exit()
print(0)