import io
import sys
_INPUT = """\
1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

if(N%100==0):
    Ans = N//100
else:
    Ans = N//100 + 1
print(Ans)