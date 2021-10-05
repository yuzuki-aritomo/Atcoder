import io
import sys
_INPUT = """\
aab
"""
sys.stdin = io.StringIO(_INPUT)

N = input()
print(N[1:]+ N[0])