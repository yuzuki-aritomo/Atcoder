import io
import sys
_INPUT = """\
box
"""
sys.stdin = io.StringIO(_INPUT)

N = input()
if(N[-1] == "s"):
    print(N + "es")
else:
    print(N + "s")