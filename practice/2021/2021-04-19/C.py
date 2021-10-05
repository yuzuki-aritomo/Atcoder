import io
import sys
_INPUT = """\
5
2 3 5 6 8
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))

Ans = float("inf")
for i in range(2**(N-1)):
    tmp = [A[0]]
    test  = [A[0]]
    for j in range(0, N-1):
        if((i>>j) &1):
            tmp[-1] |= A[j+1]
        else:
            tmp.append(A[j+1])
    ans = tmp[0]
    for j in range(len(tmp)-1):
        ans ^= tmp[j+1]
    Ans = min(Ans, ans)

print(Ans)