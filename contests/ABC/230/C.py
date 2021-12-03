import io
import sys
_INPUT = """\
5 3 3
4 5 2 5

"""
sys.stdin = io.StringIO(_INPUT)

N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

k0 = max(1-A, 1-B)
k1 = min(N-A, N-B)

k2 = max(1-A, B-N)
k3 = min(N-A, B-1)

Ans = [[0 for i in range(S-R+1)] for i in range(Q-P+1)]

a = (A+k0-P, B+k0-R)
b = (A+k2-P, B-k2-R)

b0 = A+B+k0+k0-P-R
if( b0<0 and b0<S-R ):
  for i in range(S-R+b0+1):
    Ans[i][-b0+i] = 1
elif( b0>=0 and b0<Q-P):
  for i in range(Q-P-b0+1):
    Ans[b0+i][i] = 1

b1 = -A-k2+P +B-k2-R
if( b1<0 and b1<P-Q ):
  for i in range(-b1+1):
    Ans[-i][-b1+i] = 1
elif( b1>=0 and b1<S-R):
  for i in range(b1+1):
    Ans[b1-i][+i] = 1

print(b1)

print(b0)

for item in Ans:
  print(item)
