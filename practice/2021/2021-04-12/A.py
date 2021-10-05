import io
import sys
_INPUT = """\
1000
"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())
print(100 - (N%100))