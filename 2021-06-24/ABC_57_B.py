import io
import sys
_INPUT = """\
5 5
-100000000 -100000000
-100000000 100000000
100000000 -100000000
100000000 100000000
0 0
0 0
100000000 100000000
100000000 -100000000
-100000000 100000000
-100000000 -100000000

"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())

S = []
for i in range(N):
  S.append(list(map(int,input().split())))
C = []
for i in range(M):
  C.append(list(map(int,input().split())))

for i in range(N):
  x = S[i][0]
  y = S[i][1]
  Ans = float("inf")
  ans = 0
  for j in range(M):
    tmpX = abs(x - C[j][0])
    tmpY = abs(y - C[j][1])
    if(Ans > tmpX + tmpY):
      Ans = tmpX + tmpY
      ans = j + 1
  print(ans)
