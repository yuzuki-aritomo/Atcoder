import io
import sys
_INPUT = """\
5 5
"""
sys.stdin = io.StringIO(_INPUT)


a, b = map(int,input().split())

print(32**(a-b))