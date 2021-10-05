import io
import sys
_INPUT = """\
37 450
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())

print(A*B/100)