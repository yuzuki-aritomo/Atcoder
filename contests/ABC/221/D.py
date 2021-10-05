import io
import sys
_INPUT = """\
2
1000000000 1000000000
1000000000 1000000000
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = []
for i in range(N):
  a, b = map(int, input().split())
  S.append((a, 1))
  S.append((a+b, 0))
S.sort()
# print(S)
D = [0 for i in range(N+1)]

i = 0
now = 0
while(i<len(S)-1):
  u = S[i]
  g = S[i+1]
  if(u[1] == 0):
    i += 1
    now -= 1
    if(u[0] == g[0]):
      continue
    else:
      D[now] += g[0] - u[0]
      continue
  else:
    now += 1
  if(u[0]==g[0] and g[1]==1):
    i += 1
    continue
  else:
    D[now] += g[0] - u[0]
  i += 1


print(" ".join(map(str, D[1:])))