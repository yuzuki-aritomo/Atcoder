import io
import sys
_INPUT = """\
5 6 4
"""
sys.stdin = io.StringIO(_INPUT)

a, b,c = map(int, input().split())

print((7-a) + (7-b)+(7-c))