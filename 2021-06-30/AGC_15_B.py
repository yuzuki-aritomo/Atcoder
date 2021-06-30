import io
import sys
_INPUT = """\
UUDUUDUD
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
N = len(S)
Ans = 0
for i in range(1, N+1):
  if(S[i-1] == "U"):
    Ans += N - i
    Ans += 2*(i-1)
  else:
    Ans += 2*(N-i)
    Ans += i - 1

print(Ans)