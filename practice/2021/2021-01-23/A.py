import io
import sys

_INPUT = """\
WVW
"""
sys.stdin = io.StringIO(_INPUT)

n = input()
a,b,c = n[0],n[1],n[2]
if(a==b and b==c):
    print("Won")
else:
    print("Lost")