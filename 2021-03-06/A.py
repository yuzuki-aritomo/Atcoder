import io
import sys
_INPUT = """\
0 0
"""
sys.stdin = io.StringIO(_INPUT)

a, b = map(int, input().split())
a = a+b
if(a>=15 and b>=8):
    print(1)
    exit()
if(a>=10 and b>=3):
    print(2)
    exit()
if(a>=3):
    print(3)
    exit()
print(4)