import io
import sys
_INPUT = """\
10 1
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000

"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = list(map(int,input().split()))
A.sort()

import bisect
for _ in range(M):
  u = A.pop()
  u //= 2
  bisect.insort_right(A, u)
  # print(A)


print(sum(A))