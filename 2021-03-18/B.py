import io
import sys
_INPUT = """\
1 2
"""
sys.stdin = io.StringIO(_INPUT)

X, Y = map(int, input().split())

if(Y%2 == 0):
    if(2*X <= Y and Y <= 4*X):
        print("Yes")
        exit()
print("No")