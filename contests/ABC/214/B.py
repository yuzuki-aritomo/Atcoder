import io
import sys
_INPUT = """\
30 100


"""
sys.stdin = io.StringIO(_INPUT)

S, T = map(int, input().split())

ans = 0
for i in range(101):
  for j in range(101):
    for k in range(101):
      if(i+j+k<= S and i*j*k<=T):
        ans += 1

print(ans)