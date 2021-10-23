import io
import sys
_INPUT = """\
20
224 433
987654321 987654321
2 0
6 4
314159265 358979323
0 0
-123456789 123456789
-1000000000 1000000000
124 233
9 -6
-4 0
9 5
-7 3
333333333 -333333333
-9 -1
7 -10
-1 5
324 633
1000000000 -1000000000
20 0
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = []
for i in range(N):
  A.append(tuple(map(int,input().split())))

def check(item):
  (ax, ay), (bx, by), (cx, cy) = item[0], item[1], item[2]
  tmp = abs((ax - cx) * (by - ay) - (ax - bx) * (cy - ay)) / 2
  if(tmp == 0):
    return False
  return True

import itertools 
ans = 0
for item in itertools.combinations(A, 3):
  # print(item)
  if check(item):
    ans += 1

print(ans)

