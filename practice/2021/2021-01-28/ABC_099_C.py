import io
import sys
_INPUT = """\
44852
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

# 1,
# 6,36,216,1296, 7776,46656
#9,81,729,6561,59049

A =[1]
k = 1
while(True):
    if(9**k > 100000):
        break
    A.append(9**k)
    k += 1
k = 1
while(True):
    if(6**k > 100000):
        break
    A.append(6**k)
    k += 1
dp = [N+1]*(N+1)
dp[0] = 0

for i in range(1,N+1):
    for item in A:
        if(i-item >= 0):
            dp[i] = min(dp[i],dp[i-item]+1)
            # print("dp[i]:", dp[i])

print(dp[N])