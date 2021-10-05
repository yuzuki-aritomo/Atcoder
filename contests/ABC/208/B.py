import io
import sys
_INPUT = """\
10000000

"""
sys.stdin = io.StringIO(_INPUT)


P = int(input())
A = [1]
for i in range(2, 11):
  A.append(A[-1] * i)


Ans = 0
for i in range(len(A)):
  Ans += P//A[-i-1]
  P %= A[-1-i]

print(Ans)
