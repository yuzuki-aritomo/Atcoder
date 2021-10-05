import io
import sys

_INPUT = """\
6
2 4 4 9 4 9
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
