import io
import sys
_INPUT = """\
3
1 2 1
"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())
A = list(map(int,input().split()))
mod = 998244353

# N = 5
Np = [1]
for i in range(1, N):
  Np.append(Np[-1]*i%mod)
print(Np)
for i in range(2, N):
  Np[i] = (Np[i] + Np[i-1])%mod




print(Np)
