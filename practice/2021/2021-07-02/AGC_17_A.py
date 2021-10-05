import io
import sys
_INPUT = """\
1 1
50
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter
import math

N, P  = map(int, input().split())
A = list(map(int,input().split()))

for i in range(N):
  A[i] %= 2

Cnt = Counter(A)

def permutations_count(n, r):
  return math.factorial(n) // math.factorial(n - r) // math.factorial(r)

a = 2**Cnt[0]
# if(a == 0):
#   a = 1
b_0 = 1
b_1 = 0
for i in range(1, Cnt[1]+1):
  if(i%2 == 0):
    b_0 += permutations_count(Cnt[1], i)
    # print(Cnt[1], i)
  else:
    b_1 += permutations_count(Cnt[1], i)

if(P%2 == 0):
  print(a*b_0)
else:
  print(a*b_1)