import io
import sys
_INPUT = """\
13 1 4 3000
"""
sys.stdin = io.StringIO(_INPUT)

R, G, B, N = map(int, input().split())

Ans  = 0
i = 0
while(N >= i*R):
  tmpN = N - i*R
  j = 0
  while(tmpN >= j*G):
    if((tmpN - j*G) % B == 0):
      Ans += 1
    j += 1
  i += 1

print(Ans)