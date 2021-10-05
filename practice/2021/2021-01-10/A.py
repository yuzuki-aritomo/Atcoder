import io
import sys

_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)

x, y = map(int,input().split())

if(abs(x-y)>2):
    print("No")
else:
    print("Yes")