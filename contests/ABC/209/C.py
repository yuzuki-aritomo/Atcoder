import io
import sys
_INPUT = """\
10
999999917 999999914 999999923 999999985 999999907 999999965 999999914 999999908 999999951 999999979

"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
C = list(map(int,input().split()))
mod = 10**9 + 7

C.sort()

Ans = 1
for i in range(N):
  Ans *= (C[i]-i)
  Ans %= mod

print(Ans)
