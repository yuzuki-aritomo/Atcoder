import io
import sys
_INPUT = """\
1 2 0 4 5
"""
sys.stdin = io.StringIO(_INPUT)

A = list(map(int,input().split()))

for i in range(len(A)):
    if(A[i] == 0):
        print(i+1)