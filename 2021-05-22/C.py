import io
import sys
_INPUT = """\
3
2 3 3
1 3 3
1 1 1
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

N = int(input())
A = Counter(list(map(int,input().split())))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

Ans = 0
for i in range(N):
    Ans += A[B[C[i]-1]]

print(Ans)