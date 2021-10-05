import io
import sys

_INPUT = """\
10 3
"""
sys.stdin = io.StringIO(_INPUT)

n , m = map(int, input().split())

print(n//m)n , m = map(int, input().split())

print(n//m)