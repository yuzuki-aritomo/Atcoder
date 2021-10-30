import io
import sys
_INPUT = """\
10
414598724 87552841
252911401 309688555
623249116 421714323
605059493 227199170
410455266 373748111
861647548 916369023
527772558 682124751
356101507 249887028
292258775 110762985
850583108 796044319
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = []
for i in range(N):
  A.append(tuple(map(int,input().split())))

# import numpy as np

T = []#座標,[1: s, 0: g], id
S = set()# id

import math
for i in range(N):
  x = A[i][0]
  y = A[i][1]
  if y-1==0:
    T.append([float("inf"), 0, i])
  else:
    T.append([math.atan((y-1)/x), 0, i])
  if x-1==0:
    T.append([0, 1, i])
  else:
    T.append([math.atan(y/(x-1)), 1, i])

T.sort()
ans = 0
tmp = set()
for item in T:
  if item[1]==1:#start
    tmp.add(item[2])
  else:#goal
    if item[2] in S:
      continue
    else:
      ans += 1
      tmp.add(item[2])
      S = S.union(tmp)
      tmp = set()

# print("---")
# for item in T:
#   print(item)
# print("---")
print(ans)
