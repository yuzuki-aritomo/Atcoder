import io
import sys
_INPUT = """\
-100 -100
100 100
"""
sys.stdin = io.StringIO(_INPUT)

a, b = map(int, input().split())
c, d = map(int, input().split())

print(b-c)