import io
import sys
_INPUT = """\
6 6 6
"""
sys.stdin = io.StringIO(_INPUT)


A = list(map(int, input().split()))

print(sum(A) - min(A))