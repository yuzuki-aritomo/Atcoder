import io
import sys
_INPUT = """\
3
10
20
30

"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = []
for i in range(N):
  A.append(int(input()))
S = set()

for item in A:
  tmp = set()
  for w in S:
    tmp.add(w + item)
  tmp.add(item)
  S |= tmp


C = list(S)
C.append(0)
C.sort()

for i in range(len(C)):
  if(C[len(C) - i -1] %10 == 0):
    continue
  else:
    print(C[len(C) - i -1])
    exit()
print(0)


