import io
import sys
_INPUT = """\
6
12
22
16
22
18
12
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = set()
for i in range(N):
  m = int(input())
  if m in S:
    S.remove(m)
  else:
    S.add(m)

print(len(S))