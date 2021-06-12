import io
import sys
_INPUT = """\
4
8 9 10 11

"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))
Ans = 0
for i in range(N):
  if(A[i] > 10):
    Ans += A[i] - 10

print(Ans)
