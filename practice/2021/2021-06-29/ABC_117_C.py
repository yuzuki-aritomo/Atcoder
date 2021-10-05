import io
import sys
_INPUT = """\
100 1
-100000
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
X = list(map(int,input().split()))

if(N>=M):
  print(0)
  exit()

X.sort()
Nex = []
for i in range(M-1):
  Nex.append(X[i+1] - X[i])
Nex.sort()
for i in range(N-1):
  Nex.pop()


print(sum(Nex))