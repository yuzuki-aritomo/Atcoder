import io
import sys
_INPUT = """\
2 2 1
"""
sys.stdin = io.StringIO(_INPUT)

A, B, C = map(int, input().split())

if(A<B):
    print("Aoki")
elif(A>B):
    print("Takahashi")
elif(C==0):
    print("Aoki")
else:
    print("Takahashi")