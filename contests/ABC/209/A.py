import io
import sys
_INPUT = """\
3 3
"""
sys.stdin = io.StringIO(_INPUT)


a, b = map(int, input().split())

print(max(b-a+1, 0))