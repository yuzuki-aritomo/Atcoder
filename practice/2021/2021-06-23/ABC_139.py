import io
import sys
_INPUT = """\
1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

print(N*(N-1)//2)