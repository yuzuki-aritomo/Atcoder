import io
import sys
_INPUT = """\
17
"""
sys.stdin = io.StringIO(_INPUT)

L = int(input())-1

a = 1
b = 1
for i in range(11):
    a *= L-i
    b *= (i+1)

print(a//b)