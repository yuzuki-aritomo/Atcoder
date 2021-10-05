import io
import sys
_INPUT = """\
2 4
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())

Ans = 0
if(N*2<= M):
  Ans = N + (M-N*2)//4
else:
  Ans = M//2

print(Ans)