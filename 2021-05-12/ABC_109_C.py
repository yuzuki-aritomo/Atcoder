import io
import sys
_INPUT = """\
1 1
1000000000
"""
sys.stdin = io.StringIO(_INPUT)

def make_divi(n):
    low, up = [], []
    i = 1
    while(i*i <= n):
        if(n%i == 0):
            low.append(i)
            if(n//i != i):
                up.append(n//i)
        i += 1
    return low + up[::-1]

N, X = map(int, input().split())
A = list(map(int,input().split()))
M = []

mn = float("inf")
mn_index = 0
for i in range(N):
    M.append(abs(A[i] - X))
    if(mn > abs(A[i] - X)):
        mn = abs(A[i] - X)
        mn_index = i

Ans = make_divi(M[mn_index])
for item in M:
    while(True):
        if(item%Ans[-1] == 0):
            break
        else:
            Ans.pop()

print(Ans[-1])