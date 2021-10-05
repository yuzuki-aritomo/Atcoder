import io
import sys
from typing import Match
_INPUT = """\
3 1 4
2 3
"""
sys.stdin = io.StringIO(_INPUT)

N, M , K = map(int,input().split())

road = 0
road1 = 0
for i in range(M):
  a, b = map(int ,input().split())
  if(a == 1 or b ==1 ):
    road1 +=1
  else:
    road += 1

mod = 998244353
import math
S = math.pow((N-1), K-2, mod)
S -= math.pow(N-1, K-3, mod)

tmp = 2*(N-3)*math.pow((N-1), K-4,mod)



