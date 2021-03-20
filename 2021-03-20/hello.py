import io
import sys
_INPUT = """\
1000000000000000 9.99
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(float, input().split())

A = int(A*100)
B = int(B*100)

print((A*B)//10000)
