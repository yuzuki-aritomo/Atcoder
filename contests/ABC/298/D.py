import io
import sys
_INPUT = """\
11
1 9
1 9
1 8
1 2
1 4
1 4
1 3
1 5
1 3
2
3
"""
sys.stdin = io.StringIO(_INPUT)

Q = int(input())
cnt = 0
N = [1]
A = 1


for i in range(Q):
  a = list(map(int,input().split()))
  if a[0]==1:
    A = (A*10 + a[1]) % 998244353
    N.append(a[1])
  elif a[0] == 2:
    # tmp = N[cnt] * (10**(len(N)-1-cnt))
    tmp = N[cnt] * pow(10, len(N)-1-cnt, 998244353)
    tmp = tmp % 998244353
    A += 998244353 - tmp
    cnt += 1
  else:
    A = A % 998244353
    print(A)
    # print(int(A[cnt:len(A)]) % 998244353)

