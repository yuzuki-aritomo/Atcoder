import io
import sys
_INPUT = """\
9 10
0 3 5 7 100 110 200 300 311
"""
sys.stdin = io.StringIO(_INPUT)

N, T = map(int, input().split())
A = list(map(int,input().split()))

Ans = 0
for i in range(N-1):
  Ans += min(T, A[i+1]- A[i])


print(Ans + T)