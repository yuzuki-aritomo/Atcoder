import io
import sys
_INPUT = """\
60 3
5 8
1 3
10 15
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
L = []
R = []
for i in range(K):
    a, b = map(int,input().split())
    L.append(a)
    R.append(b)
dp = [0 for i in range(N+1)]
dpsum = [0 for i in range(N+1)]
dp[1] = 1
dpsum[1] = 1
for i in range(2, N+1):
    for j in range(K):
        li = i-R[j] 
        ri = i-L[j]
        if(ri<0): continue
        li = max(li, 1)
        dp[i] += dpsum[ri] - dpsum[li-1]
    dp[i] = dp[i]%998244353
    dpsum[i] = (dpsum[i-1] + dp[i])%998244353
print(dp[-1] % 998244353)