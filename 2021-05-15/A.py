import io
import sys
_INPUT = """\
5 5 5

"""
sys.stdin = io.StringIO(_INPUT)

A = list(map(int,input().split()))
A.sort()
if(A[2] - A[1] == A[1] - A[0]):
    print("Yes")
else:
    print("No")
