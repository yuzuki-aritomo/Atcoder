import io
import sys
_INPUT = """\
1000000000000000 9.99
"""
sys.stdin = io.StringIO(_INPUT)

import math
A, B = map(float, input().split())

C = str(B) + "0" + "0"
# print("str(B):", str(B))
for i in range(len(C)):
    if(C[i]=="."):
        a = int(C[i+1])
        b = int(C[i+2])
A = int(A)
B = int(B)*100 + a*10 + b
n = A*B
n = n//100
print(n)