import io
import sys
_INPUT = """\
3
1 7 1

"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

N = int(input())
A = list(map(int,input().split()))
C = Counter(A)

Ans = 0
for item in A:
  Ans += N - C[item]

print(Ans//2)

