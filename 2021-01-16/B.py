import io
import sys

_INPUT = """\
20 4
6 2 6 8 4 5 5 8 4 1 7 8 0 3 6 1 1 8 3 0
"""
sys.stdin = io.StringIO(_INPUT)

N, K  = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
A.append(-1)

same = 0

Ans = [-1] * K
const_same = 0
for i in range(N):
    if(A[i] == 0):
        same += 1
        const_same = same
    else:
        break
same = 0
for i in range(N):
    # print(Ans)
    if(A[i] == A[i+1]):
        same += 1
    elif(A[i]+1 == A[i+1]):
        same += 1
        for k in range(same):
            if(k>=K or const_same<=k):
                break
            Ans[k] += 1
        if(const_same>same):
            const_same = same
        same = 0
    elif(i == N-1):
        same += 1
        for k in range(same):
            if(k>=K or const_same<=k):
                break
            Ans[k] += 1
    else:
        break

ans = 0
for item in Ans:
    ans += (item+1)
print(ans)