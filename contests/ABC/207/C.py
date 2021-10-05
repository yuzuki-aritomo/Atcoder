import io
import sys
_INPUT = """\
19
4 210068409 221208102
4 16698200 910945203
4 76268400 259148323
4 370943597 566244098
1 428897569 509621647
4 250946752 823720939
1 642505376 868415584
2 619091266 868230936
2 306543999 654038915
4 486033777 715789416
1 527225177 583184546
2 885292456 900938599
3 264004185 486613484
2 345310564 818091848
1 152544274 521564293
4 13819154 555218434
3 507364086 545932412
4 797872271 935850549
2 415488246 685203817
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = []
G = []
M = []
for i in range(N):
  a, b, c = map(int, input().split())
  if(a == 1):
    M.append([b, c])
    # S.append(b)
    # G.append(c)
  elif(a == 2):
    M.append([b, c-0.1])
    # S.append(b)
    # G.append(c-0.1)
  elif(a == 3):
    M.append([b+0.1, c])
    # S.append(b+0.1)
    # G.append(c)
  else:
    M.append([b+0.1, c-0.1])
    # S.append(b+0.1)
    # G.append(c- 0.1)

M.sort()

for i in range(N):
  S.append(M[i][0])
  G.append(M[i][1])

import bisect
Ans = 0
for i in range(N):
  tmp = bisect.bisect_right(S, G[i])
  Ans += tmp - i - 1

print(Ans)