import io
import sys
_INPUT = """\
3 4 5
"""
sys.stdin = io.StringIO(_INPUT)

A, B, C = map(int, input().split())
if(A**2+ B**2 < C**2):
    print("Yes")
else:
    print("No")