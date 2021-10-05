import io
import sys
_INPUT = """\
3
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
print(N-1)