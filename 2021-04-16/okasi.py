import io
import sys
_INPUT = """\
4 1000
200
20
500
60
"""
sys.stdin = io.StringIO(_INPUT)


N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(int(input()))

Ans = 0
change = 0
for i in range(2**N):
    ans = 0
    S = 0
    for j in range(N):
        if(i>>j & 1):
            ans += 1
            S += A[j]
    if(S > M):
        continue
    else:
        if(Ans < ans):
            Ans = ans
            change = M - S
        elif(Ans == ans):
            change = min(change, M-S)
print(change)

