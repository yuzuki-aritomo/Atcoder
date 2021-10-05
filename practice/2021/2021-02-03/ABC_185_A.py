import io
import sys
_INPUT = """\
100 100 1 100
"""
sys.stdin = io.StringIO(_INPUT)

A = list(map(int,input().split()))

print(min(A))