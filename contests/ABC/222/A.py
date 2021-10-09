import io
import sys
_INPUT = """\
1
"""
sys.stdin = io.StringIO(_INPUT)


w = input()
w = "0000" + w
print(w[-4:])
