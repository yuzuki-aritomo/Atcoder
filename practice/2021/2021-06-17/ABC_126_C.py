import io
import sys
_INPUT = """\
100000 5
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())

n = 1/N
Ans = 0
for i in range(1, N+1):
  if(i>= K):
    Ans += n
    continue
  tmp = 1
  while(True):
    if(i*2**tmp >= K):
      break
    tmp += 1
  Ans += n*0.5**tmp

print(Ans)