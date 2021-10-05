import io
import sys
_INPUT = """\
1
99999

"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

N = int(input())
A = list(map(int,input().split()))
C = Counter()

for i in range(N):
  C[A[i]] += 1
  C[A[i]-1] += 1
  C[A[i]+1] += 1

Ans = 0
for item in C:
  Ans = max(Ans, C[item])

print(Ans)