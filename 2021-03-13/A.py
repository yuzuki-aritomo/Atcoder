import io
import sys
_INPUT = """\
10 120
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())

if(B%A==0):
    print("Yes")
else:
    print("No")
