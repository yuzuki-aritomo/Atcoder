import io
import sys
_INPUT = """\
10 3
5 1 3 2 4 1 1 2 3 4
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())

from collections import Counter
Cnt = Counter(map(int,input().split()))

m = len(Cnt)

A = list(Cnt.values())
A.sort()
Ans = sum(A[0:m-K])

print(Ans)
# print(Cnt)
# print(A)
