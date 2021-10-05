import io
import sys
_INPUT = """\
99999 99998
"""
sys.stdin = io.StringIO(_INPUT)

x, y = map(int, input().split())

print(((x-y)/x)*100)